from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    n_usuario = db.Column(db.String(50), primary_key=True)
    password = db.Column(db.String(50), nullable=False)

class Auto(db.Model):
    __tablename__ = 'garage'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    color = db.Column(db.String(50), nullable=False)
    nombre = db.Column(db.String(50), nullable=False)
    modelo = db.Column(db.String(100), nullable=False)



