from flask import Flask, jsonify, request
from database_operations import *
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
from flask_cors import CORS
import pytz

import jwt
import re

app = Flask(__name__)
CORS(app)

load_dotenv()
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

@app.route('/register', methods=['POST'])
def register():
    try:
        data = request.json
        email = data.get('email')
        password = data.get('password')
        name = data.get('name')
        bio = ""

        if not email or not password:
            return jsonify({"message": "Email and password are required"}), 400

        if not is_valid_email(email):
            return jsonify({"message": "Invalid email format"}), 400

        if user_exists(email, name):
            return jsonify({"message": "Email or username already in use"}), 400

        hashed_password = generate_password_hash(password)
        user_id = register_user(email, hashed_password, name, bio)

        token = jwt.encode({
            'user_id': user_id
        }, app.config['SECRET_KEY'])

        return jsonify({"message": "User registered", "token": token}), 201
    except Exception as e:
        return jsonify({"message": f"Registration failed: {str(e)}"}), 500

@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.json
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            return jsonify({"message": "Email and password are required"}), 400

        if not is_valid_email(email):
            return jsonify({"message": "Invalid email format"}), 400

        user = get_user_by_email(email)
        if user and check_password_hash(user['passwordHash'], password):
            token = jwt.encode({
                'user_id': user['id']
            }, app.config['SECRET_KEY'])

            return jsonify({"token": token}), 200
        else:
            return jsonify({"message": "Invalid email or password"}), 401
    except Exception as e:
        return jsonify({"message": f"Login failed: {str(e)}"}), 500

@app.route('/user/<int:user_id>/name', methods=['PUT'])
def set_user_name(user_id):
    try:
        data = request.json
        name = data.get('name')

        if not name:
            return jsonify({"message": "Name is required"}), 400

        update_user_name(user_id, name)
        return jsonify({"message": "Username updated"}), 201
    except Exception as e:
        return jsonify({"message": f"Set username failed: {str(e)}"}), 500


@app.route('/user/<int:user_id>/bio', methods=['PUT'])
def set_user_bio(user_id):
    try:
        data = request.json
        bio = data.get('bio')

        if bio is None:
            return jsonify({"message": "Bio is required"}), 400

        update_user_bio(user_id, bio)
        return jsonify({"message": "User bio updated"}), 200
    except Exception as e:
        return jsonify({"message": f"Set user bio failed: {str(e)}"}), 500


@app.route('/user/<int:user_id>', methods=['GET'])
def get_user_profile(user_id):
    try:
        user = get_user_profile_details(user_id)
        if user:
            return jsonify(user), 200
        else:
            return jsonify({"message": "User not found"}), 404
    except Exception as e:
        return jsonify({"message": f"Get user profile failed: {str(e)}"}), 500


@app.route('/user/<int:user_id>/notes', methods=['GET'])
def get_user_notes(user_id):
    try:
        notes = get_notes_of_user(user_id)
        return jsonify(notes), 200
    except Exception as e:
        return jsonify({"message": f"Get user notes failed: {str(e)}"}), 500


@app.route('/<int:user_id>/notebooks', methods=['POST'])
def create_notebook(user_id):
    try:
        data = request.json
        title = data.get('title')

        if not title:
            return jsonify({"message": "Title is required"}), 400

        notebook_id = insert_notebook(title, user_id)
        return jsonify({"message": "Notebook created successfully", "notebook_id": notebook_id}), 201
    except Exception as e:
        return jsonify({"message": f"Create notebook failed: {str(e)}"}), 500



@app.route('/<int:user_id>/notebooks', methods=['GET'])
def get_notebooks(user_id):
    try:
        notebooks = get_notebooks_of_user(user_id)
        return jsonify(notebooks), 200
    except Exception as e:
        return jsonify({"message": f"Get notebooks failed: {str(e)}"}), 500


@app.route('/notebooks/<int:notebook_id>', methods=['GET'])
def get_notebook(notebook_id):
    try:
        notebook = get_notebook_details(notebook_id)
        return jsonify(notebook), 200
    except Exception as e:
        return jsonify({"message": f"Get notebook failed: {str(e)}"}), 500


@app.route('/notebooks/<int:notebook_id>', methods=['PUT'])
def rename_notebook(notebook_id):
    try:
        data = request.json
        new_title = data.get('title')

        if not new_title:
            return jsonify({"message": "New title is required"}), 400

        if update_notebook_title(notebook_id, new_title):
            return jsonify({"message": "Notebook renamed"}), 200
        else:
            return jsonify({"message": "Notebook not found"}), 404
    except Exception as e:
        return jsonify({"message": f"Rename notebook failed: {str(e)}"}), 500


@app.route('/notebooks/<int:notebook_id>', methods=['DELETE'])
def delete_notebook(notebook_id):
    try:
        if remove_notebook(notebook_id):
            return jsonify({"message": "Notebook deleted successfully"}), 204
        else:
            return jsonify({"message": "Notebook not found"}), 404
    except Exception as e:
        return jsonify({"message": f"Delete notebook failed: {str(e)}"}), 500


@app.route('/notebooks/<int:notebook_id>/notes', methods=['GET'])
def get_notes_from_notebook(notebook_id):
    try:
        notes = get_notes_in_notebook(notebook_id)
        return jsonify(notes), 200
    except Exception as e:
        return jsonify({"message": f"Get notes from notebook failed: {str(e)}"}), 500


@app.route('/notebooks/<int:notebook_id>/notes/<int:note_id>', methods=['POST'])
def add_note_to_notebook(notebook_id, note_id):
    try:
        add_note_to_a_notebook(note_id, notebook_id)
        return jsonify({"message": "Note added to notebook successfully"}), 201
    except Exception as e:
        return jsonify({"message": f"Add note to notebook failed: {str(e)}"}), 500


@app.route('/<int:user_id>/notes', methods=['POST'])
def create_note(user_id):
    try:
        data = request.json
        title = data.get('title')

        if not title:
            return jsonify({"message": "Title is required"}), 400

        note_id = insert_note(title, user_id)
        return jsonify({"message": "Note created", "note_id": note_id}), 201
    except Exception as e:
        return jsonify({"message": f"Create note failed: {str(e)}"}), 500


@app.route('/notes/<int:note_id>', methods=['GET'])
def get_note(note_id):
    try:
        note = get_note_details(note_id)
        if note:
            return jsonify(note), 200
        else:
            return jsonify({"message": "Note not found"}), 404
    except Exception as e:
        return jsonify({"message": f"Get note failed: {str(e)}"}), 500


@app.route('/notes/<int:note_id>', methods=['DELETE'])
def delete_note(note_id):
    try:
        remove_note(note_id)
        return jsonify({"message": "Note deleted"}), 204
    except Exception as e:
        return jsonify({"message": f"Delete note failed: {str(e)}"}), 500


@app.route('/<int:user_id>/notes/<int:note_id>/versions', methods=['POST'])
def save_note_content(user_id, note_id):
    try:
        data = request.json
        content = data.get('content')

        if content is None:
            return jsonify({"message": "Content is required"}), 400

        create_note_version(note_id, content, user_id)
        return jsonify({"message": "Note version saved"}), 201
    except Exception as e:
        return jsonify({"message": f"Save note content failed: {str(e)}"}), 500


@app.route('/notes/<int:note_id>/versions', methods=['GET'])
def get_note_versions(note_id):
    try:
        versions = get_versions_of_note(note_id)
        if versions:
            return jsonify(versions), 200
        else:
            return jsonify({"message": "No versions found for this note"}), 404
    except Exception as e:
        return jsonify({"message": f"Get note versions failed: {str(e)}"}), 500


@app.route('/notes/<int:note_id>/versions/date', methods=['GET'])
def get_note_version_by_date(note_id):
    data = request.json
    date_str = data.get('date')

    if not date_str:
        return jsonify({"message": "Date is required"}), 400

    try:
        date_obj = datetime.strptime(date_str, '%a, %d %b %Y %H:%M:%S GMT').replace(tzinfo=pytz.UTC)
    except ValueError:
        return jsonify({"message": "Date format should be 'Day, DD Mon YYYY HH:MM:SS GMT'"}), 400

    try:
        version = get_version_of_note_by_date(note_id, date_obj)
        if version:
            return jsonify(version), 200
        else:
            return jsonify({"message": "No version found for this date"}), 404
    except Exception as e:
        return jsonify({"message": f"Get note version by date failed: {str(e)}"}), 500


@app.route('/<int:current_user_id>/notes/<int:note_id>/owners', methods=['GET'])
def get_note_owners(current_user_id, note_id):
    try:
        if not current_user_id:
            return jsonify({"message": "Current user id required"}), 404

        owners = get_note_access_users(note_id, current_user_id)
        return jsonify(owners), 200
    except Exception as e:
        return jsonify({"message": f"Get note owners failed: {str(e)}"}), 500


@app.route('/notes/<int:note_id>/owners', methods=['POST'])
def add_note_owner(note_id):
    try:
        data = request.json
        email = data.get('email')

        if not email:
            return jsonify({"message": "Email is required"}), 400

        if not is_valid_email(email):
            return jsonify({"message": "Invalid email format"}), 400

        give_user_access_to_note(note_id, email)
        return jsonify({"User given access to note"}), 201
    except ValueError as e:
        return jsonify({"message": str(e)}), 404
    except Exception as e:
        return jsonify({"message": f"Add note owner failed: {str(e)}"}), 500


def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None

if __name__ == '__main__':
    app.run(debug=True)
