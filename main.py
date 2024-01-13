from flask import Flask, request, jsonify 
import requests
import base64
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

api_url = 'https://sandbox.belvo.com/api/'

secret_id = "57ba7cfd-73fc-4668-84ec-2acedbf810b7"
secret_password = "izfIPkq8p#bsYimSlqIt1U3EbmqD2PYfW7iRqZX0AuAS3VvS9NtiCrHd_o6Ap2WE"
credentials = f"{secret_id}:{secret_password}"

#codificamos base64
encoded_credentials = base64.b64encode(credentials.encode()).decode()
headers = {'Authorization': f'Basic {encoded_credentials}',}

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
            return jsonify({'error': f'Error en la solicitud a la API externa. Código de estado: {response.status_code}'}), 500
    except Exception as e:
        return jsonify({'error': f'Error durante la solicitud a la API externa: {str(e)}'}), 500
    


@app.route('/login', methods=['POST'])
def login():
    data = request.json
    print(data)
    email = data.get('user_email')
    password = data.get('user_password')

   # Logic para el inicio de sesion

    if email == 'usuario' and password == '1234':
        return jsonify({'message': 'Inicio de sesión exitoso'}), 200
    else:
        return jsonify({'message': 'Credenciales incorrectas'}), 401

@app.route('/logout', methods = ['POST'])
def logOut():
    print("Se ha cerrado sesion byeeee")
    return jsonify({'message': 'Cierre de sesión exitoso'}), 200



@app.route("/get-user/<user_id>")
def getUser(user_id):
    user_data = {
        "user_id" : user_id,
        "email" : "user1@email.com",
        "age" : 25
    }

    extra = request.args.get("extra")

    if extra:
        user_data["extra"] = extra
    return jsonify(user_data), 200

@app.route("/create-user", methods = ["POST"])
def create_user():
    data = request.get_json()
    return jsonify(data), 201

### HTTP METHODS 

## GET
'''Request data from a specific resource'''

## POST
'''Create a resource'''

## PUT
'''Update a resource'''

## DELETE
'''Delete a resource'''

if __name__ == "__main__":
    app.run(debug=True)