import json
from llama_index.core.tools import BaseTool, FunctionTool

with open('data.json') as f:
    data = json.load(f)
    

class AsanaFunctions:
    def __init__(self, file_path:str):
        self.file_path = file_path
        self.data = self._load_data()
        
    def _load_data(self):
        with open(self.file_path) as f:
            data = json.load(f)
        return data
    
    def get_number_of_projects(self) -> int:
        """Get the number of projects and returns the number of projects as an integer"""
        return len(self.data['Projects'])
    
    def get_project_names(self) -> list:
        """Get the names of the projects and returns the names of the projects as a list"""
        return [project['project_name'] for project in self.data['Projects']]
    
    def get_tasks(self, project_name:str) -> list:
        """Get the tasks of a project and returns the tasks as a list"""
        for project in self.data['Projects']:
            if project['project_name'] == project_name:
                return project['tasks']
        return []
    
    def get_number_of_tasks(self, project_name:str) -> int:
        """Get the number of tasks of a project and returns the number of tasks as an integer"""
        for project in self.data['Projects']:
            if project['project_name'] == project_name:
                return len(project['tasks'])
        return 0
    
    def get_completed_tasks(self):
        """Get the completed tasks of a project and returns the completed tasks as a dictionary"""
        tasks = {}
        for project in self.data['Projects']:
            for task in project['tasks']:
                if task['completed']:
                    if project['project_name'] in tasks:
                        tasks[project['project_name']].append(task)
                    else:
                        tasks[project['project_name']] = [task]
                    
        return tasks
    
    def get_uncompleted_tasks(self):
        """Get uncompleted tasks from all projects and returns the uncompleted tasks as a dictionary"""
        tasks = {}
        for project in self.data['Projects']:
            for task in project['tasks']:
                if not task['completed']:
                    if project['project_name'] in tasks:
                        tasks[project['project_name']].append(task)
                    else:
                        tasks[project['project_name']] = [task]
                    
        return tasks
    
    def get_uncompleted_task_for_project(self, project_name:str):
        """Get uncompleted tasks of a project and returns the uncompleted tasks as a list"""
        for project in self.data['Projects']:
            if project['project_name'] == project_name:
                return [task for task in project['tasks'] if not task['completed']]
        return []
    
    def get_task_information(self, task_name:str):
        """Get the information/data of a task given a task name and returns the information as a dictionary"""
        for project in self.data['Projects']:
            for task in project['tasks']:
                if task['name'] == task_name:
                    return task
        return {}
    
    def get_all_tasks(self):
        """Get all tasks from all projects and returns all tasks as a list"""
        tasks = []
        for project in self.data['Projects']:
            tasks.extend(project['tasks'])
        return tasks
    
    @property
    def function_tools(self):
        get_num_of_projects_tool = FunctionTool.from_defaults(fn=self.get_number_of_projects)
        get_project_names_tool = FunctionTool.from_defaults(fn=self.get_project_names)
        get_tasks_tool = FunctionTool.from_defaults(fn=self.get_tasks)
        get_number_of_tasks_tool = FunctionTool.from_defaults(fn=self.get_number_of_tasks)
        get_completed_tasks_tool = FunctionTool.from_defaults(fn=self.get_completed_tasks)
        get_uncompleted_tasks_tool = FunctionTool.from_defaults(fn=self.get_uncompleted_tasks)
        get_uncompleted_task_for_project_tool = FunctionTool.from_defaults(fn=self.get_uncompleted_task_for_project)
        get_all_tasks_tool = FunctionTool.from_defaults(fn=self.get_all_tasks)
        get_task_information_tool = FunctionTool.from_defaults(fn=self.get_task_information)
        return [
            get_num_of_projects_tool, 
            get_project_names_tool,
            get_tasks_tool,
            get_number_of_tasks_tool,
            get_completed_tasks_tool,
            get_uncompleted_tasks_tool,
            get_uncompleted_task_for_project_tool,
            get_all_tasks_tool,
            get_task_information_tool
            ]
        