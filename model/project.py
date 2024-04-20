from sys import maxsize


class Project:

    def __init__(self, project_name=None, status=None, inherit_global_categories=None, view_status=None,
                 description=None, id=None):
        self.id = id
        self.project_name = project_name
        self.status = status
        self.inherit_global_categories = inherit_global_categories
        self.view_status = view_status
        self.description = description

    def __repr__(self):
        return "%s:%s %s" % (self.id, self.project_name, self.status)

    def __eq__(self, other):
        return ((self.id is None or other.id is None or self.id == other.id) and self.project_name == other.project_name
                and self.status == other.status
                # and self.inherit_global_categories == other.inherit_global_categories
                and self.view_status == other.view_status and self.description == other.description)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
