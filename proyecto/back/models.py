from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Auto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    marca = db.Column(db.String(80), nullable=False)
    color = db.Column(db.String(50), nullable=False)
    motor = db.Column(db.String(50), nullable=False)

class Marca(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    pais = db.Column(db.String(50), nullable=False)

def obtener_marcas_disponibles():
    # Suponiendo que tienes una clase Marca que representa una tabla de marcas en tu base de datos
    marcas =   Marca.query.all()  # Obtiene todas las marcas de la base de datos
    marcas_disponibles = [marca.nombre for marca in marcas]  # Convierte los objetos Marca en una lista de nombres
    return marcas_disponibles
