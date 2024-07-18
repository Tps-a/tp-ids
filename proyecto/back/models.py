from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()



class Auto(db.Model):
    __tablename__ = 'autos'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    color = db.Column(db.String(50), nullable=False)
    nombre = db.Column(db.String(50), nullable=False)
    modelo = db.Column(db.String(50), nullable=False)

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    usuario = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(50), nullable=False)

"""
class Marca(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    # Relación con Auto (si es necesario)
    autos = db.relationship('Auto', backref='marca', lazy=True)
"""