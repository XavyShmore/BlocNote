from flask import Flask, jsonify, request
from database_operations import *
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    name = data.get('name', '')
    bio = data.get('bio', '')

    if not email or not password:
        return jsonify({"message": "Email and password are required"}), 400

    hashed_password = generate_password_hash(password)
    user_id = register_user(email, hashed_password, name, bio)

    return jsonify({"message": "User registered", "user_id": user_id}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({"message": "Email and password are required"}), 400

    hashed_password = get_hashed_password(email)
    if hashed_password and check_password_hash(hashed_password, password):
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"message": "Invalid email or password"}), 401

@app.route('/user/<int:user_id>/name', methods=['POST'])
def set_user_name(user_id):
    data = request.json
    name = data.get('name')

    if not name:
        return jsonify({"message": "Name is required"}), 400

    update_user_name(user_id, name)
    return jsonify({"message": "Username updated"}), 201

@app.route('/user/<int:user_id>/bio', methods=['POST'])
def set_user_bio(user_id):
    data = request.json
    bio = data.get('bio')

    if bio is None:
        return jsonify({"message": "Bio is required"}), 400

    update_user_bio(user_id, bio)
    return jsonify({"message": "User bio updated"}), 200

@app.route('/user/<int:user_id>', methods=['GET'])
def get_user_profile(user_id):
    user = get_user_profile(user_id)
    if user:
        return jsonify(user), 200
    else:
        return jsonify({"message": "User not found"}), 404

@app.route('/user/<int:user_id>/notes', methods=['GET'])
def get_user_notes(user_id):
    notes = get_notes_of_user(user_id)
    return jsonify(notes), 200

@app.route('/notebooks', methods=['POST'])
def create_notebook():
    data = request.json
    title = data.get('title')
    owner_id = data.get('owner_id')

    if not title or not owner_id:
        return jsonify({"message": "Title and owner ID are required"}), 400

    notebook_id = insert_notebook(title, owner_id)
    return jsonify({"message": "Notebook created successfully", "notebook_id": notebook_id}), 201

@app.route('/notebooks/<int:notebook_id>', methods=['PUT'])
def rename_notebook(notebook_id):
    data = request.json
    new_title = data.get('title')

    if not new_title:
        return jsonify({"message": "New title is required"}), 400

    if update_notebook_title(notebook_id, new_title):
        return jsonify({"message": "Notebook renamed"}), 200
    else:
        return jsonify({"message": "Notebook not found"}), 404

@app.route('/notebooks/<int:notebook_id>', methods=['DELETE'])
def delete_notebook(notebook_id):
    if remove_notebook(notebook_id):
        return jsonify({"message": "Notebook deleted successfully"}), 204
    else:
        return jsonify({"message": "Notebook not found"}), 404

@app.route('/notebooks/<int:notebook_id>/notes', methods=['GET'])
def get_notes_from_notebook(notebook_id):
    notes = get_notes_in_notebook(notebook_id)
    return jsonify(notes), 200

@app.route('/notebooks/<int:notebook_id>/notes/<int:note_id>', methods=['POST'])
def add_note_to_notebook(notebook_id, note_id):
    add_note_to_a_notebook(note_id, notebook_id)
    return jsonify({"message": "Note added to notebook successfully"}), 201

@app.route('/notes', methods=['POST'])
def create_note():
    data = request.json
    title = data.get('title')

    if not title:
        return jsonify({"message": "Title is required"}), 400

    note_id = insert_note(title)
    return jsonify({"message": "Note created", "note_id": note_id}), 201

@app.route('/notes/<int:note_id>', methods=['GET'])
def get_note(note_id):
    note = get_note_details(note_id)
    if note:
        return jsonify(note), 200
    else:
        return jsonify({"message": "Note not found"}), 404

@app.route('/notes/<int:note_id>', methods=['DELETE'])
def delete_note(note_id):
    remove_note(note_id)
    return jsonify({"message": "Note deleted"}), 204

@app.route('/notes/<int:note_id>/versions', methods=['POST'])
def save_note_content(note_id):
    data = request.json
    content = data.get('content')
    editor_id = data.get('editor_id')

    if content is None or editor_id is None:
        return jsonify({"message": "Content and editor ID are required"}), 400

    create_note_version(note_id, content, editor_id)
    return jsonify({"message": "Note version saved"}), 201

@app.route('/notes/<int:note_id>/versions', methods=['GET'])
def get_note_versions(note_id):
    versions = get_versions_of_note(note_id)
    if versions:
        return jsonify(versions), 200
    else:
        return jsonify({"message": "No versions found for this note"}), 404

@app.route('/notes/<int:note_id>/versions/<string:date>', methods=['GET'])
def get_note_version_by_date(note_id, date):
    try:
        date_obj = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S')
    except ValueError:
        return jsonify({"message": "Date format should me Y-m-dT"}), 400

    version = get_version_of_note_by_date(note_id, date_obj)
    if version:
        return jsonify(version), 200
    else:
        return jsonify({"message": "No version found for this date"}), 404

@app.route('/notes/<int:note_id>/owners', methods=['GET'])
def get_note_owners(note_id):
    data = request.json
    current_user_id = data.get('current_user_id')

    if not current_user_id:
        return jsonify({"message": "Current user id required"}), 404

    owners = get_note_access_users(note_id, current_user_id)
    return jsonify(owners), 200

@app.route('/notes/<int:note_id>/owners/<int:user_id>', methods=['POST'])
def add_note_owner(note_id, user_id):
    give_user_access_to_note(note_id, user_id)
    return 201

if __name__ == '__main__':
    app.run(debug=True)
