from flask import Flask, request, jsonify, make_response, send_from_directory, render_template
from models import db, Auto, Marca #se pueden importar mas cosas 
import os

app = Flask(__name__, template_folder='../front/HTML')
port= 5000
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tu_base_de_datos.db' ## crear base de datos
## crear base de datos con posgrest y poner la url de la base de datos arriba 

@app.route('/')
def home():
    return render_template('main.html')

@app.route('/disenar')
def disenar():
    return render_template('disena_auto.html')

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

@app.route('/css/<path:filename>')
def enviar_css(filename):
    css_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'front', 'css'))
    return send_from_directory(css_dir, filename)

@app.route('/javascript/<path:filename>')
def enviar_js(filename):
    js_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'front', 'java_script'))
    return send_from_directory(js_dir, filename)

@app.route('/modelos/<path:filename>')
def enviar_modelos(filename):
    models_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'front', 'modelos'))
    return send_from_directory(models_dir, filename)

#investigar esto si estas viendo este comentario
# Asegúrate de tener una función initialize_app() definida en algún lugar
# initialize_app()

if __name__ == '__main__':
    app.run(debug=True)


    
    