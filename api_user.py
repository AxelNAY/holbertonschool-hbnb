from flask import Flask, request, jsonify
from flask_restx import Api, Resource, fields
from models.user import User
import re

app = Flask(__name__)
api = Api(app)

# Load existing users from JSON file
User.load_all()

# User model for request parsing and response marshalling
user_model = api.model('User', {
    'email': fields.String(required=True, description='Email address of the user'),
    'password': fields.String(required=True, description='Password of the user'),
    'first_name': fields.String(required=True, description='First name of the user'),
    'last_name': fields.String(required=True, description='Last name of the user'),
    'status': fields.String(required=True, description='Status of the user')
})

@api.route('/users')
class UserList(Resource):
    @api.doc('list_users')
    def get(self):
        """List all users"""
        return jsonify(User.user_object_list)

    @api.doc('create_user')
    @api.expect(user_model)
    def post(self):
        """Create a new user"""
        data = request.json
        email = data.get('email')
        
        # Validate email format
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return {"message": "Invalid email format"}, 400
        
        # Check for duplicate email
        if any(user['_User__email'] == email for user in User.user_object_list):
            return {"message": "Email already exists"}, 409
        
        user = User(
            email=email,
            password=data.get('password'),
            first_name=data.get('first_name'),
            last_name=data.get('last_name'),
            status=data.get('status')
        )
        user.save()
        return jsonify(user.__dict__), 201

@api.route('/users/<string:user_id>')
class UserResource(Resource):
    @api.doc('get_user')
    def get(self, user_id):
        """Fetch a user given its identifier"""
        user = next((user for user in User.user_object_list if user['_User__id'] == user_id), None)
        if not user:
            return {"message": "User not found"}, 404
        return jsonify(user)

    @api.doc('update_user')
    @api.expect(user_model)
    def put(self, user_id):
        """Update a user given its identifier"""
        data = request.json
        user = next((user for user in User.user_object_list if user['_User__id'] == user_id), None)
        if not user:
            return {"message": "User not found"}, 404
        user_obj = User(
            email=user['_User__email'],
            password=user['_User__password'],
            first_name=user['_User__first_name'],
            last_name=user['_User__last_name'],
            status=user['status']
        )
        user_obj.__dict__ = user
        user_obj.update(data)
        user_obj.save_all()
        return jsonify(user_obj.__dict__)

    @api.doc('delete_user')
    def delete(self, user_id):
        """Delete a user given its identifier"""
        user = next((user for user in User.user_object_list if user['_User__id'] == user_id), None)
        if not user:
            return {"message": "User not found"}, 404
        user_obj = User(
            email=user['_User__email'],
            password=user['_User__password'],
            first_name=user['_User__first_name'],
            last_name=user['_User__last_name'],
            status=user['status']
        )
        user_obj.__dict__ = user
        user_obj.delete()
        return '', 204

if __name__ == '__main__':
    app.run(debug=True)

