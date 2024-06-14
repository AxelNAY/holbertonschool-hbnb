from flask import Flask, request, jsonify
from flask_restx import Api, Resource, fields
from user import User  # Assuming User class is in user.py

app = Flask(__name__)
api = Api(app, version='1.0', title='User API',
          description='A simple User API',)

ns = api.namespace('users', description='User operations')

user_model = api.model('User', {
    'email': fields.String(required=True, description='The user email'),
    'password': fields.String(required=True, description='The user password'),
    'first_name': fields.String(required=True, description='The user first name'),
    'last_name': fields.String(required=True, description='The user last name'),
    'status': fields.String(required=True, description='The user status', enum=['host', 'commenter'])
})

users = {}  # This will act as our in-memory database

@ns.route('/')
class UserList(Resource):
    @ns.doc('list_users')
    def get(self):
        """List all users"""
        return [user.__dict__ for user in User.user_object_list], 200

    @ns.doc('create_user')
    @ns.expect(user_model)
    @ns.response(201, 'User created')
    @ns.response(400, 'Bad Request')
    @ns.response(409, 'Conflict')
    def post(self):
        """Create a new user"""
        data = request.json
        try:
            user = User(**data)
            user.save()
            return user.__dict__, 201
        except ValueError as e:
            return {'message': str(e)}, 400
        except Exception as e:
            return {'message': str(e)}, 409

@ns.route('/<string:user_id>')
@ns.response(404, 'User not found')
@ns.param('user_id', 'The user identifier')
class User(Resource):
    @ns.doc('get_user')
    def get(self, user_id):
        """Fetch a user given its identifier"""
        user = next((u for u in User.user_object_list if u['_User__id'] == user_id), None)
        if user:
            return user, 200
        else:
            return {'message': 'User not found'}, 404

    @ns.doc('delete_user')
    @ns.response(204, 'User deleted')
    def delete(self, user_id):
        """Delete a user given its identifier"""
        user = next((u for u in User.user_object_list if u['_User__id'] == user_id), None)
        if user:
            user_obj = User(**user)
            user_obj.delete()
            return '', 204
        else:
            return {'message': 'User not found'}, 404

    @ns.doc('update_user')
    @ns.expect(user_model)
    def put(self, user_id):
        """Update a user given its identifier"""
        data = request.json
        user = next((u for u in User.user_object_list if u['_User__id'] == user_id), None)
        if user:
            user_obj = User(**user)
            user_obj.update(data)
            return user_obj.__dict__, 200
        else:
            return {'message': 'User not found'}, 404

if __name__ == '__main__':
    app.run(debug=True)
