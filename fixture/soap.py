from suds.client import Client
from suds import WebFault
from model.project import Project


class SoapHelper:

    def __init__(self, app):
        self.app = app
        self.client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")

    def can_login(self, username, password):
        try:
            self.client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_project_list(self, username, password):
        return self.convert_projects_to_model(self.client.service.mc_projects_get_user_accessible(username, password))

    def convert_projects_to_model(self, projects):
        def convert(project):
            return Project(id=str(project.id), project_name=project.name, status=project.status.name,
                           view_status=project.view_state.name,
                           inherit_global_categories=None,
                           description=project.description)
        return list(map(convert, projects))
