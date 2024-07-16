from flask import Flask, request, jsonify, make_response
from models import db, Auto, Marca #se pueden importar mas cosas 

app = Flask(__name__)
port= 5000
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tu_base_de_datos.db' ## crear base de datos
## crear base de datos con posgrest y poner la url de la base de datos arriba 

@app.route('/')
def home():
    with open('/proyecto/front/HTML/main.html', 'r') as html_file:
        html_content = html_file.read()
    return make_response(html_content, 200, {'Content-Type': 'text/html'})

@app.route('/crear-auto', methods=['POST']) 
def crear_auto():
    data = request.json
    nueva_marca = Marca(nombre=data['marca'])
    db.session.add(nueva_marca)
    db.session.commit()
    
    nuevo_auto = Auto(marca=nueva_marca, color=data['color'], motor=data['motor'])
    db.session.add(nuevo_auto)
    db.session.commit()

    return jsonify({'mensaje': 'Auto creado exitosamente', 'id': nuevo_auto.id}), 201

@app.route('/autos/<int:auto_id>', methods=['PUT'])
def actualizar_auto(auto_id):
    auto = Auto.query.get_or_404(auto_id)
    data = request.json
    # Asumiendo que Marca es una relación y necesitamos actualizarla por separado
    if 'marca' in data:
        auto.marca.nombre = data['marca']
        db.session.add(auto.marca)  # Asegurarse de que la marca también se actualiza si es necesario
    if 'color' in data:
        auto.color = data['color']
    if 'motor' in data:
        auto.motor = data['motor']
    db.session.commit()
    return jsonify({'mensaje': 'Auto actualizado exitosamente'})

@app.route('/autos/<int:auto_id>', methods=['DELETE'])
def eliminar_auto(auto_id):
    auto = Auto.query.get_or_404(auto_id)
    db.session.delete(auto)
    db.session.commit()
    return jsonify({'mensaje': 'Auto eliminado exitosamente'})

#investigar esto si estas viendo este comentario
# Asegúrate de tener una función initialize_app() definida en algún lugar
# initialize_app()

if __name__ == '__main__':
    app.run(debug=True)