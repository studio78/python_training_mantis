from selenium.webdriver.support.ui import Select
from model.project import Project


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def create(self, project):
        wd = self.app.wd
        self.open_manage_projects_page()
        wd.find_element_by_css_selector("input[value='Create New Project']").click()
        self.fill_all_fields(project)
        wd.find_element_by_css_selector("input[value='Add Project']").click()
        wd.find_element_by_link_text("Proceed").click()
        self.project_cache = None

    def open_manage_projects_page(self):
        wd = self.app.wd
        if "manage" not in wd.current_url:
            wd.find_element_by_link_text("Manage").click()
        if not (wd.current_url.endswith("manage_proj_page.php")):
            wd.find_element_by_link_text("Manage Projects").click()

    def fill_all_fields(self, project):
        wd = self.app.wd
        self.app.fill_field_by_name("name", project.project_name)
        Select(wd.find_element_by_name("status")).select_by_visible_text(project.status)
        inherit_global_categories = wd.find_element_by_name("inherit_global")
        if ((not inherit_global_categories and project.inherit_global_categories) or
                (inherit_global_categories and not project.inherit_global_categories)):
            wd.find_element_by_name("inherit_global").click()
        Select(wd.find_element_by_name("view_state")).select_by_visible_text(project.view_status)
        self.app.fill_field_by_name("description", project.description)

    def delete_by_id(self, id):
        wd = self.app.wd
        self.open_manage_projects_page()
        wd.find_element_by_css_selector(".width100 a[href$='%s']" % id).click()
        wd.find_element_by_xpath('//input[@value="Delete Project"]').click()
        wd.find_element_by_xpath('//input[@value="Delete Project"]').click()
        self.project_cache = None

    def count(self):
        wd = self.app.wd
        self.open_manage_projects_page()
        return len(wd.find_elements_by_css_selector(".width100 tr[class*='row']:not([class='row-category'])"))

    project_cache = None

    def get_project_list(self):
        if self.project_cache is None:
            wd = self.app.wd
            self.open_manage_projects_page()
            self.project_cache = []
            for element in wd.find_elements_by_css_selector(".width100 tr[class*='row']:not([class='row-category'])"):
                link = element.find_element_by_tag_name("a").get_attribute("href")
                index = link.find('=') + 1
                id = link[index:]
                column = element.find_elements_by_tag_name("td")
                self.project_cache.append(Project(project_name=column[0].text, status=column[1].text, id=id,
                                                  view_status=column[3].text, description=column[4].text))
        return list(self.project_cache)
