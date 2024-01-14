from flask_sqlalchemy import SQLAlchemy
import hashlib

db =  SQLAlchemy()

class Users(db.Model):
    userId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)


    def __str__(self):
        return f"name: {self.name}. email:{self.email}"


    ## solo prueba
    def check_password(self, password):
        return self.password == password