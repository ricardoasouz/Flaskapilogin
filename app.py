from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'your-secret-key'
jwt = JWTManager(app)

# Simulated user database
users = {
    'username': 'password'
}

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username in users and users[username] == password:
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401

@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    return jsonify(message="Access granted to protected resource"), 200

if __name__ == '__main__':
    app.run(debug=True)
