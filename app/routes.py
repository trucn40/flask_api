from flask import Blueprint, jsonify, request
import os

# Path to your user data file
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Base directory of the project
USER_DATA_FILE = os.path.join(BASE_DIR, 'data', 'users.txt')

# Utility function to read users from the file
def read_users_from_file():
    users = {}
    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, 'r') as file:
            for line in file:
                user_id, name, email = line.strip().split(',')
                users[int(user_id)] = {'name': name, 'email': email}
    return users

api_blueprint = Blueprint('api', __name__)

@api_blueprint.route('/hello', methods=['GET'])
def hello():
    return jsonify({'message': 'Hello, World!'})

@api_blueprint.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    a = data.get('a')
    b = data.get('b')
    result = a + b
    return jsonify({'result': result})

@api_blueprint.route('/multiply', methods=['POST'])
def multiply():
    data = request.get_json()
    a = data.get('a')
    b = data.get('b')
    result = a * b
    return jsonify({'result': result})


# API route to get a specific user by ID
# API route to get all users
@api_blueprint.route('/users', methods=['GET'])
def get_all_users():
    users = read_users_from_file()  # Read users from the file
    return jsonify({'users': users})

# Define a new route, for example to fetch user data
@api_blueprint.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    # For example, return a mock user object based on user_id
    users = {
        1: {'name': 'John Doe', 'email': 'john@example.com'},
        2: {'name': 'Jane Smith', 'email': 'jane@example.com'}
    }
    
    user = users.get(user_id)
    
    if user:
        return jsonify({'user': user})
    else:
        return jsonify({'error': 'User not found'}), 404

# API route to add a new user (optional)
@api_blueprint.route('/user', methods=['POST'])
def add_user():
    data = request.get_json()
    user_id = data.get('id')
    name = data.get('name')
    email = data.get('email')
    
    # Append the new user to the file in the data folder
    with open(USER_DATA_FILE, 'a') as file:
        file.write(f'{user_id},{name},{email}\n')
    
    return jsonify({'message': 'User added successfully'}), 201