from flask import Flask, jsonify, request
import uuid
from datetime import datetime
import json
import os

app = Flask(__name__)

# In-memory data store
users = []

# Load data from file (optional)
DATA_FILE = "users.json"
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as f:
        try:
            users = json.load(f)
        except json.JSONDecodeError:
            users = []


# SAVE TO FILE (after any update)
def save_data():
    with open(DATA_FILE, "w") as f:
        json.dump(users, f, indent=4)



@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    age = data.get('age')

    if not name or not email:
        return jsonify({'error': 'Name and email are required'}), 400

   
    if any(u['email'] == email for u in users):
        return jsonify({'error': 'Email already exists'}), 409

    new_user = {
        'id': str(uuid.uuid4()),
        'name': name,
        'email': email,
        'age': age,
        'created_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    users.append(new_user)
    save_data()
    return jsonify(new_user), 201



@app.route('/api/users', methods=['GET'])
def get_all_users():
    filtered = users


    age = request.args.get('age')
    if age:
        filtered = [u for u in filtered if str(u.get('age')) == age]

 
    search = request.args.get('search')
    if search:
        filtered = [u for u in filtered if search.lower() in u['name'].lower() or search.lower() in u['email'].lower()]

 
    sort = request.args.get('sort')
    if sort in ['name', 'age', 'created_at']:
        filtered.sort(key=lambda x: x.get(sort))

  
    page = int(request.args.get('page', 1))
    limit = int(request.args.get('limit', 5))
    start = (page - 1) * limit
    end = start + limit
    paginated = filtered[start:end]

    return jsonify({
        'page': page,
        'total_users': len(filtered),
        'users': paginated
    }), 200



@app.route('/api/users/<string:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in users if u['id'] == user_id), None)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(user), 200


@app.route('/api/users/<string:user_id>', methods=['PUT'])
def update_user(user_id):
    user = next((u for u in users if u['id'] == user_id), None)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    data = request.get_json()
    user['name'] = data.get('name', user['name'])
    user['email'] = data.get('email', user['email'])
    user['age'] = data.get('age', user['age'])
    save_data()

    return jsonify({'message': 'User updated', 'user': user}), 200



@app.route('/api/users/<string:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    before = len(users)
    users = [u for u in users if u['id'] != user_id]
    if len(users) == before:
        return jsonify({'error': 'User not found'}), 404

    save_data()
    return jsonify({'message': 'User deleted'}), 200



@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to the User Management API 🚀",
        "endpoints": {
            "POST": "/api/users",
            "GET": "/api/users",
            "GET (one)": "/api/users/<id>",
            "PUT": "/api/users/<id>",
            "DELETE": "/api/users/<id>"
        }
    }), 200


if __name__ == '__main__':
    app.run(debug=True)
