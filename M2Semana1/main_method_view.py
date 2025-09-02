from flask import Flask, request, jsonify
from flask.views import MethodView
import json
import os

app = Flask(__name__)
DATA_FILE = 'M2Semana1/tasks.json'
VALID_STATUSES = ["Pending", "In Progress", "Completed"]

#Functions to read and store tasks in the JSON file
def read_tasks():
    if not os.path.exists(DATA_FILE): #Adding  validation to confirm JSON file exists else create one
        with open(DATA_FILE, 'w') as json_file:
            json.dump([], json_file)
        return []
    with open(DATA_FILE, 'r') as json_file:
        return json.load(json_file)

def save_tasks(task_list):
    with open(DATA_FILE, 'w') as json_file:
        json.dump(task_list, json_file, indent=4)

class TaskAPI(MethodView):

    def get(self, task_id=None): #Adding default None to task_id to avoid type error when calling
        tasks = read_tasks()
        if task_id is not None:
            for task in tasks:
                if task['id'] == task_id:
                    return jsonify(task), 200
            return jsonify({'error': 'Task not found.'}), 404

        status_filter = request.args.get('status')
        if status_filter:
            if status_filter not in VALID_STATUSES:
                return jsonify({'error': 'Invalid status.'}), 400
            tasks = [task for task in tasks if task['status'] == status_filter]

        return jsonify(tasks), 200

    def post(self, task_id=None):
        new_task = request.get_json()
        required_fields = ['id', 'title', 'description', 'status']

        for field in required_fields:
            if field not in new_task or not new_task[field]:
                return jsonify({'error': f'Required field: {field}'}), 400

        if new_task['status'] not in VALID_STATUSES:
            return jsonify({'error': 'Invalid status.'}), 400

        tasks = read_tasks()
        if any(task['id'] == new_task['id'] for task in tasks):
            return jsonify({'error': 'There is an existing task with this ID.'}), 400

        tasks.append(new_task)
        save_tasks(tasks)
        return jsonify({'message': 'Task created successfully.'}), 201

    def put(self, task_id):
        tasks = read_tasks()
        update_data = request.get_json()

        for task in tasks:
            if task['id'] == task_id:
                if 'title' in update_data:
                    task['title'] = update_data['title']
                if 'description' in update_data:
                    task['description'] = update_data['description']
                if 'status' in update_data:
                    if update_data['status'] not in VALID_STATUSES:
                        return jsonify({'error': 'Invalid status.'}), 400
                    task['status'] = update_data['status']

                save_tasks(tasks)
                return jsonify({'message': 'Task updated successfully.'}), 200

        return jsonify({'error': 'Task not found.'}), 404

    def delete(self, task_id):
        tasks = read_tasks()
        updated_tasks = [task for task in tasks if task['id'] != task_id]

        if len(updated_tasks) == len(tasks):
            return jsonify({'error': 'Task not found.'}), 404

        save_tasks(updated_tasks)
        return jsonify({'message': 'Task deleted successfully.'}), 200

task_view = TaskAPI.as_view('task_api') #Creating new instance of the class to be used in FLASK

app.add_url_rule('/tasks', defaults={'task_id': None}, view_func=task_view, methods=['GET', 'POST']) #Creating endpoints that does not need a parameter
app.add_url_rule('/tasks/<int:task_id>', view_func=task_view, methods=['GET', 'PUT', 'DELETE']) #Endpoints that recquire a parameter

# ---------- Run App ----------
if __name__ == '__main__':
    app.run(debug=True, port=5050)
