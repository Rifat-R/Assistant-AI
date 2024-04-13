import asana
from config import ACCESS_TOKEN
import datetime

from typing import List

configuration = asana.Configuration()
configuration.access_token = ACCESS_TOKEN
api_client = asana.ApiClient(configuration)

# create an instance of the API class
projects_api_instance = asana.ProjectsApi(api_client)
tasks_api_instance = asana.TasksApi(api_client)
stories_api_instance = asana.StoriesApi(api_client)
portfolios_api_instance = asana.PortfoliosApi(api_client)



# Need to convert the date string to a more readable format
def convert_date(date_str: str) -> str:
    date_format = "%Y-%m-%dT%H:%M:%S.%fZ"
    # Define the format of the input string
    input_format = "%Y-%m-%dT%H:%M:%S.%fZ"
    # Define the desired output format
    output_format = "%Y-%m-%d %H:%M:%S"    
    
    datetime_obj = datetime.datetime.strptime(date_str, input_format)

    # Format the datetime object into the desired string format
    formatted_string = datetime_obj.strftime(output_format)
    return formatted_string

class Projects:
    def __init__(self, workspace_gid: str):
        self.workspace_gid = workspace_gid
        self.projects_raw = self._set_projects()
          
            
    def _set_projects(self) -> list[str]: 
        opts = {
            'limit': 50, # int | Results per page. The number of objects to return per page. The value must be between 1 and 100.
            'workspace': self.workspace_gid, # str | Globally unique identifier for the workspace or organization.
            'archived': False, # bool | Only return projects whose `archived` field takes on the value of this parameter.
        }

        # Get multiple projects
        api_response = projects_api_instance.get_projects(opts)
        return list(api_response)
    
    
    # Dunder method called everytime you want to iterate over the object (So we can do for project in projects: print(project))
    def __iter__(self):
        # Return the instance itself as the iterator
        self.index = 0
        return self

    # Converts the object into an iterator and into Project objects
    def __next__(self):
        # If there are more projects to yield, return the next one
        if self.index < len(self.projects_raw):
            project = self.projects_raw[self.index]
            self.index += 1
            return Project(project["gid"])
        # If there are no more projects, raise StopIteration
        raise StopIteration
    
    # Return a list of project ids
    @property
    def id_list(self) -> list[str]:
        project_ids = [data['gid'] for data in self.projects_raw]
        return project_ids
    


class Project:
    def __init__(self, project_gid:str):
        self.project_gid = project_gid
        self.project_raw_data = self._set_project()

        self.name = self.project_raw_data['name']
        self.assignee = self.project_raw_data['assignee']
        self.created_at = convert_date(self.project_raw_data['created_at'])     
    
    def _set_project(self) -> dict:
        opts = {
            'opt_fields': 'name,assignee,assignee.name,created_at'
        }
        api_response = projects_api_instance.get_project(self.project_gid, opts)
        return api_response

    @property
    def tasks(self):
        opts = {
            'limit': 100, # int | Results per page. The number of objects to return per page.
        }

        api_response = tasks_api_instance.get_tasks_for_project(self.project_gid, opts)
        tasks = [Task(data["gid"]) for data in api_response]
        return tasks
        
        
class Task:
    def __init__(self, task_gid: str):
        self.task_gid = task_gid
        self.task_raw_data = self._set_task()
        
        self.name = self.task_raw_data['name']
        self.due_on = self.task_raw_data['due_on']
        self.description = self.task_raw_data['notes'] if not " " else "No description available"
        self.assignee_data = self.task_raw_data['assignee']
        self.assignee_name:str = self.assignee_data["name"] if self.assignee_data else "No assignee"
        self.completed:bool = self.task_raw_data['completed']
        self.created_at = convert_date(self.task_raw_data['created_at'])
        
    def _set_task(self) -> dict:
        opts = {
            'opt_fields': 'name,due_on,notes,created_at,assignee,assignee.name,approval_status,completed'
        }
        api_response = tasks_api_instance.get_task(self.task_gid, opts)
        return api_response

    @property
    def stories(self):
        opts = {
            'limit':50,
            'opt_fields': 'created_at,created_by,created_by.name,html_text,resource_subtype,source,source.name,target,target.name,text,type'
        }
        api_response = stories_api_instance.get_stories_for_task(self.task_gid, opts)
        return api_response
    
    
    @property
    def comments(self) -> List[str]:
        comments = []
        for story in self.stories:
            comment = story['text']
            comments.append(comment)
        return comments