from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data (in-memory storage)
todos = [
    {"id": 1, "title": "Learn REST", "completed": False},
    {"id": 2, "title": "Build a REST API", "completed": False},
]


@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)


@app.route('/todos', methods=['POST'])
def add_todo():
    new_todo = request.get_json()
    new_todo['id'] = len(todos) + 1
    todos.append(new_todo)
    return jsonify(new_todo), 201


@app.route('/todos/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    todo = next((item for item in todos if item['id'] == todo_id), None)
    if todo is None:
        return jsonify({"error": "Todo not found"}), 404
    return jsonify(todo)


@app.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    todo = next((item for item in todos if item['id'] == todo_id), None)
    if todo is None:
        return jsonify({"error": "Todo not found"}), 404

    updated_todo = request.get_json()
    todo.update(updated_todo)
    return jsonify(updated_todo)


@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    global todos
    todos = [item for item in todos if item['id'] != todo_id]
    return jsonify({"message": "Todo deleted"}), 200


if __name__ == '__main__':
    app.run(debug=True)
