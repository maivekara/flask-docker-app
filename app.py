from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = [
    {"id": 1, "title": "Docker öğren", "done": False},
    {"id": 2, "title": "GitHub Actions kur", "done": False}
]

@app.route("/")
def index():
    return "Görev API'sine Hoş Geldin!"

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)

@app.route("/tasks", methods=["POST"])
def add_task():
    new_task = request.get_json()
    new_task["id"] = len(tasks) + 1
    tasks.append(new_task)
    return jsonify(new_task), 201

@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]
    return jsonify({"result": True})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
