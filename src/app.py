
from flask import Flask, jsonify, request

app = Flask(__name__)

# Declarar la variable global todos como una lista con al menos un elemento de ejemplo
todos = [
    {"label": "Sample Todo 1", "done": True}
]

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos), 200

# Declarar la función add_new_todo
@app.route('/todos', methods=['POST'])
def add_new_todo():
    new_todo = request.get_json()
    todos.append(new_todo)
    return jsonify(todos), 200

# Declarar la función delete_todo
@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    if 0 <= position < len(todos):
        todos.pop(position)
    else:
        return jsonify({"error": "Invalid position"}), 400
    return jsonify(todos), 200

if __name__ == '__main__':
    app.run(debug=True)