from flask import Flask, request, jsonify, make_response, send_from_directory, render_template, redirect, url_for
from models import db, Auto, Usuario #se pueden importar mas cosas 
import os

app = Flask(__name__, template_folder='../front/HTML', static_folder='../static')
port = 5000
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db' ## crear base de datos


@app.route('/')
def home():
    return render_template('main.html')

@app.route('/<usuario_id>')
def main(usuario_id):
    usuario = Usuario.query.get(usuario_id)
    if not usuario:
        return redirect(url_for('login_page'))
    return render_template('main.html', usuario=usuario)

@app.route('/disenar')
def disenar():
    return render_template('disena_auto.html')

@app.route('/disenar/guardar-auto', methods=['POST']) 
def guardar_auto():
    data = request.get_json()  
    auto_nuevo = Auto(color = data.get("color"), nombre = data.get("nombre"), modelo = data.get("modelo"))
    db.session.add(auto_nuevo)
    db.session.commit()
    
    return jsonify({'mensaje': 'Auto actualizado exitosamente'})

@app.route('/register_page')
def register_page():
    return render_template('register.html')

@app.route('/register_page/registrarse', methods=['POST']) 
def register():
    data = request.get_json()  
    usuario_existente = Usuario.query.filter_by(usuario=data.get("usuario")).first()
    if usuario_existente:
        return jsonify({'error': 'Este usuario ya existe!'})
    usuario_nuevo = Usuario(usuario = data.get("usuario"), password = data.get("password"))
    db.session.add(usuario_nuevo)
    db.session.commit()
    return jsonify({'mensaje': 'Usuario registrado!'})

@app.route('/login_page')
def login_page():
    return render_template('inicio.html')

@app.route('/login_page/login', methods=['POST'])
def login():
    data = request.get_json()
    usuario = Usuario.query.filter_by(usuario=data.get("usuario"), password=data.get("password")).first()
    if not usuario:
        return jsonify({'error': 'Credenciales inválidas'})
    return jsonify({'usuario_id': usuario.id})





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
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(debug=True)
