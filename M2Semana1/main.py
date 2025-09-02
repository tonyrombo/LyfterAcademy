from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)
DATA_FILE = 'M2Semana1/tasks.json'

# List of valid status for the tasks
VALID_STATUSES = ["Pending", "In Progress", "Completed"]

# Read tasks stored in the JSON file
def read_tasks():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as file:
        return json.load(file)

# Save tasks into the JSON file
def save_tasks(tasks):
    with open(DATA_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

# Endpoint to get tasks with optional filter for status
@app.route('/tasks', methods=['GET'])
def get_tasks():
    status = request.args.get('status')
    tasks = read_tasks()

    if status:
        if status not in VALID_STATUSES:
            return jsonify({'error': 'Invalid Status.'}), 400
        tasks = [t for t in tasks if t['status'] == status]

    return jsonify(tasks), 200

# Endpoint to create new tasks
@app.route('/tasks', methods=['POST'])
def create_task():
    new_task = request.get_json()

    # Validation
    required_fields = ['id', 'title', 'description', 'status']
    for field in required_fields:
        if field not in new_task or not new_task[field]:
            return jsonify({'error': f'Required field: {field}'}), 400

    if new_task['status'] not in VALID_STATUSES:
        return jsonify({'error': 'Invalid status.'}), 400

    tasks = read_tasks()

    # Validation for repeated Id
    if any(task['id'] == new_task['id'] for task in tasks):
        return jsonify({'error': 'There is an existing tasks with this ID.'}), 400

    tasks.append(new_task)
    save_tasks(tasks)

    return jsonify({'message': 'Task created successfully.'}), 201

# Endpoint to edit existing tasks
@app.route('/tasks/<int:id>', methods=['PUT']) #Sending ID as integer to avoid type errors
def edit_task(id):
    edit_data = request.get_json() #Converting the JSON in the request to dictionary
    tasks = read_tasks()

    for task in tasks:
        if task['id'] == id: #If Id exists in JSON file
            if 'title' in edit_data:
                task['title'] = edit_data['title']
            if 'description' in edit_data:
                task['description'] = edit_data['description']
            if 'status' in edit_data:
                if edit_data['status'] not in VALID_STATUSES:
                    return jsonify({'error': 'Invalid status.'}), 400
                task['status'] = edit_data['status']

            save_tasks(tasks)
            return jsonify({'message': 'Task updated successfully.'}), 200

    return jsonify({'error': 'Task was not found.'}), 404

# Endpoint to delete tasks
@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    tasks = read_tasks()
    new_tasks = [task for task in tasks if task['id'] != id] #Con esta funcion se crea una nueva lista new_tasks que contiene solo los elementos que no tienen el id indicado para sobrescribir el archivo JSON

    if len(new_tasks) == len(tasks):
        return jsonify({'error': 'Task was not found.'}), 404

    save_tasks(new_tasks)
    return jsonify({'message': 'Task deleted successfully.'}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5050)