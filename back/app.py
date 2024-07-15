from flask import Flask, request, jsonify, render_template
from models import db, Auto  # Asegúrate de importar db y Auto correctamente
from models import obtener_marcas_disponibles

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///autos.db'
db.init_app(app)


@app.route('/')
def main():
    return render_template('main.html')

@app.route('/disena_auto')
def disena_auto():
    autos = Auto.query.all() 
    marcas = obtener_marcas_disponibles() 
    return render_template('disena_auto.html', autos=autos, marcas=marcas)

@app.route('/autos', methods=['POST'])
def crear_auto():
    data = request.json
    nuevo_auto = Auto(marca=data['marca'])
    db.session.add(nuevo_auto)
    db.session.commit()
    return jsonify({'mensaje': 'Auto creado exitosamente'}), 201

@app.route('/ver_autos')
def ver_autos():
    autos = Auto.query.all()  # Recupera todos los autos de la base de datos
    return render_template('disena_auto.html', autos=autos)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)