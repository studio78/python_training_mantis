from datahelpers.stringhelper import get_random_project
from model.project import Project


'''
def test_add_project(app):
    project = get_random_project()
    old_projects = app.project.get_project_list()
    app.project.create(project)
    new_projects = app.project.get_project_list()
    old_projects.append(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
'''


def test_add_project(app):
    username = app.config['webadmin']['username']
    password = app.config['webadmin']['password']
    project = get_random_project()
    old_projects = app.soap.get_project_list(username, password)
    app.project.create(project)
    new_projects = app.soap.get_project_list(username, password)
    old_projects.append(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
