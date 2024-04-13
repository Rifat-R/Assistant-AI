from asana_utils import Projects
import json
import os
from dotenv import load_dotenv

load_dotenv()
projects = Projects(os.getenv("ASANA_WORKSPACE_GID"))

data = {"Projects": []}
results = []
for project in projects:
    print(f"Project Name: {project.name}\n")
    data["Projects"].append({"project_name": project.name, "tasks": []})
    tasks = project.tasks
    for index, task in enumerate(tasks):
        task_metadata = {
            "task_id": task.task_gid,
            "name": task.name,
            "due_on" : task.due_on,
            "description": task.description,
            "assignee": task.assignee_name,
            "completed": task.completed,
            "comments": task.comments,
        }
        data["Projects"][-1]["tasks"].append(task_metadata)
        print(f"Task Name: {task.name}")
        

print(data)
with open("data.json", "w") as file:
    file.write(json.dumps(data, indent=4))