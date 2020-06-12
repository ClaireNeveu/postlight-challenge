from waitress import serve
from pyramid.config import Configurator
from pyramid.response import Response

from controllers.employees import *

def hello_world(request):
    print('Incoming request')
    return Response('<body><h1>Hello World!</h1></body>')


def run_app():
    with Configurator() as config:
        
        config.add_route('get_employee', '/employees/{id}', request_method='GET')
        config.add_view(get_employee, route_name='get_employee')
        
        config.add_route('patch_employee', '/employees/{id}', request_method='PATCH')
        config.add_view(patch_employee, route_name='patch_employee')
        
        config.add_route('post_employee', '/employees', request_method='POST')
        config.add_view(post_employee, route_name='post_employee')
        
        config.add_route('get_employees', '/employees', request_method='GET')
        config.add_view(get_employees, route_name='get_employees')

        # add_exception_view() # TODO
        
        app = config.make_wsgi_app()
        
        
    serve(app, host='0.0.0.0', port=6543)
