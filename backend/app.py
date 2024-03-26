from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
    return jsonify({"message": "Register successful"}), 201

@app.route('/login', methods=['POST'])
def login():
    return jsonify({"message": "Login successful"}), 200

@app.route('/user', methods=['GET'])
def get_user_profile():
    return 200

@app.route('/notebooks', methods=['POST'])
def create_notebook():
    return jsonify({"message": "Notebook created"}), 201

@app.route('/notebooks/<int:notebook_id>', methods=['PUT'])
def rename_notebook(notebook_id):
    return jsonify({"message": "Notebook renamed"}), 200

@app.route('/notebooks/<int:notebook_id>', methods=['DELETE'])
def delete_notebook(notebook_id):
    return jsonify({"message": "Notebook deleted"}), 200

@app.route('/notes', methods=['POST'])
def create_note():
    return jsonify({"message": "Note created"}), 201

@app.route('/notes/<int:note_id>', methods=['PUT'])
def update_note(note_id):
    return jsonify({"message": "Note updated"}), 200

@app.route('/notes/<int:note_id>', methods=['DELETE'])
def delete_note(note_id):
    return jsonify({"message": "Note deleted"}), 200

@app.route('/notes/<int:note_id>/versions', methods=['GET'])
def get_note_versions(note_id):
    return 200

if __name__ == '__main__':
    app.run(debug=True)
