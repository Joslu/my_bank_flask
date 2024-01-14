
import requests
import base64
from flask_cors import CORS
import sqlite3 as sqlite3
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, jsonify 
from models import db, Users
import os

app = Flask(__name__)

# Obtén la ruta absoluta al archivo de la base de datos
database_path = os.path.abspath("database/users.db")
print(database_path)
# Configura la URI de la base de datos en tu aplicación Flask
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{database_path}"

app.config["SQLALCHEMY_TRACK_NOTIFICATIONS"] = False

# Conectar db
db.init_app(app)
CORS(app)


# Belvo credentials
api_url = 'https://sandbox.belvo.com/api/'

secret_id = "57ba7cfd-73fc-4668-84ec-2acedbf810b7"
secret_password = "izfIPkq8p#bsYimSlqIt1U3EbmqD2PYfW7iRqZX0AuAS3VvS9NtiCrHd_o6Ap2WE"
credentials = f"{secret_id}:{secret_password}"

#codificamos base64
encoded_credentials = base64.b64encode(credentials.encode()).decode()
headers = {'Authorization': f'Basic {encoded_credentials}',}

# Routes
@app.route("/")
def home():
    return "Wrlcome to my server"

@app.route('/logout', methods = ['POST'])
def logOut():
    print("Se ha cerrado sesion byeeee")
    return jsonify({'message': 'Log out successfully'}), 200


@app.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('user_email')
    password = data.get('user_password')

    user = Users.query.filter_by(email=email).first()

    if user and user.check_password(password):
        return jsonify({'message': 'Welcome'}), 200
    else:
        return jsonify({'message': 'Wrong credentials'}), 401
    
    
@app.route('/create-user', methods=['POST'])
def create_user():
    data = request.json
    name = data.get('user_name')
    email = data.get('user_email')
    password = data.get('user_password')

    if name or email or password == "":
       return jsonify({'message': 'Complete'}), 400

    available_user = Users.query.filter_by(email=email).first()
    if available_user:
        return jsonify({'message': 'User already exists'}), 400

    
    new_user = Users(name=name, email=email, password=password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User created succesfully'}), 201


#GET INFO BELVO
@app.route('/get-data', methods=['GET'])
def get_data():
    try:
        response = requests.get(f"{api_url}institutions/?page_size=100", headers=headers)

        if response.status_code == 200:

            dataJson = response.json()

            # Utiliza map paa crear la lista de diccionarios
            banks_info = map(lambda bank: {
            "bankId": bank.get('id'),
            "bankName": bank.get('display_name'),
            "bankLogo": bank.get('icon_logo')
            }, dataJson['results'])

            return jsonify({"data": list(banks_info)})
        else:
            return jsonify({'error': f'Error on external APi. Code: {response.status_code}'}), 500
    except Exception as e:
        return jsonify({'error': f'Error while asking to external API: {str(e)}'}), 500
    

if __name__ == "__main__":
    app.run(debug=True)