from flask import Flask, jsonify, request
from flask_cors import CORS, cors_origin
import db_requests

app = Flask(__name__)
cors = CORS(app)

@app.route('/registration', methods=['POST'])
def registration():
    data = request.json

    email = data.get('email')
    password = data.get('password')
    user_type = data.get('user_type')

    if email and password:

        try:
            id = db_requests.registration(user_type, (email, password))
            return jsonify({'message': 'Success registration',
                            'id': id}), 200

        except Exception as e:
            if 'UNIQUE constraint failed: users.email' in repr(e):
                return jsonify({'message': 'Already registered email'}), 403

            return jsonify({'message': 'Something is wrong'}), 403

    return jsonify({'message': 'Something is wrong'}), 403


@app.route('/log_in', methods=['POST'])
def auth_user():
    data = request.json

    email = data.get('email')
    password = data.get('password')
    user_type = data.get('user_type')

    if email and password:
        result = db_requests.auth_user(user_type, (email, password))

        if result:
            return jsonify({'message': 'Success log in',
                            'id': id}), 200

        return jsonify({'message': 'Invalid email or password'}), 403

    return jsonify({'message': 'Something is wrong'}), 403


@app.route('/update_profile', methods=['PATCH'])
def update_profile():
    data = request.json

    phone = data.get('phone')
    id = data.get('id')
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    user_type = data.get('user_type')

    if (phone or first_name or last_name) and id:
        db_requests.update_profile(user_type, (phone, first_name, last_name, id))
        return jsonify({'message': 'Success updated'}), 200

    return jsonify({'message': 'Nothing to change'}), 403


if __name__ == '__main__':
    app.run()
