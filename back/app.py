from flask import Flask, request, jsonify
from models import db, Auto  # Asegúrate de importar db y Auto correctamente

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///autos.db'
db.init_app(app)

@app.route('/autos', methods=['POST'])
def crear_auto():
    data = request.json
    nuevo_auto = Auto(marca=data['marca'])
    db.session.add(nuevo_auto)
    db.session.commit()
    return jsonify({'mensaje': 'Auto creado exitosamente'}), 201

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)