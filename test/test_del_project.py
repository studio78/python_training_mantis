from datahelpers.stringhelper import get_random_project
import random
from model.project import Project


def test_delete_some_project(app):
    if len(app.project.get_project_list()) == 0:
        app.project.create(get_random_project())
    old_projects = app.project.get_project_list()
    project = random.choice(old_projects)
    app.project.delete_by_id(project.id)
    new_projects = app.project.get_project_list()
    assert len(old_projects) - 1 == app.project.count()
    old_projects.remove(project)
    assert sorted(new_projects, key=Project.id_or_max) == sorted(app.project.get_project_list(), key=Project.id_or_max)
