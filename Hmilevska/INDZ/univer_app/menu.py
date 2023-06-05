from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

users = []

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    username = data.get('username')
    password = data.get('password')

    # Перевірка, чи юзер вже зареєстрований за заданим email
    for user in users:
        if user['email'] == email:
            return 'Email already exists', 400

    # Збереження даних користувача
    user_data = {
        'email': email,
        'username': username,
        'password': password
    }
    users.append(user_data)

    return 'User registered successfully', 200

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Перевірка, чи існує користувач з введеним username та password
    for user in users:
        if user['username'] == username and user['password'] == password:
            return 'Login successful', 200

    return 'Invalid username or password', 401

if __name__ == '__main__':
    app.run(port=8000)
