from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Auto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    marca = db.Column(db.String(80), nullable=False)
    color = db.Column(db.String(50), nullable=False)
    motor = db.Column(db.String(50), nullable=False)