from pyramid.httpexceptions import HTTPNotFound

class NotFound(HTTPNotFound):
    def __init__(self, item_type, ident):
        super().__init__(f'Could not find {item_type} with id: {ident}')

class JobNotFound(NotFound):
    def __init__(self, ident):
        super().__init__('Job', ident)

class EmployeeNotFound(NotFound):
    def __init__(self, ident):
        super().__init__('Employee', ident)

class DepartmentNotFound(NotFound):
    def __init__(self, ident):
        super().__init__('Department', ident)
