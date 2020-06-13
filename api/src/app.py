from waitress import serve
from pyramid.config import Configurator
from pyramid.events import NewRequest
from pyramid.response import Response

from controllers.employees import *

def add_cors_callback(event):
    def cors_headers(request, response):
        response.headers.update({
            'Access-Control-Allow-Origin': 'localhost:4000',
            'Access-Control-Allow-Methods': 'POST,GET,DELETE,PUT,OPTIONS',
            'Access-Control-Allow-Headers': 'Origin, Content-Type, Accept, Authorization',
            'Access-Control-Allow-Credentials': 'true'
        })
    event.request.add_response_callback(cors_headers)


def run_app():
    with Configurator() as config:

        # Some duplicate configuration here until I move to a distributed config
        config.add_route('get_employee', '/employees/{id}', request_method='GET')
        config.add_view(get_employee, route_name='get_employee', renderer='json')
        
        config.add_route('patch_employee', '/employees/{id}', request_method='PATCH')
        config.add_view(patch_employee, route_name='patch_employee', renderer='json')
        
        config.add_route('post_employee', '/employees', request_method='POST')
        config.add_view(post_employee, route_name='post_employee', renderer='json')
        
        config.add_route('get_employees', '/employees', request_method='GET')
        config.add_view(get_employees, route_name='get_employees', renderer='json')

        # add_exception_view() # TODO

        config.add_subscriber(add_cors_callback, NewRequest)
        
        app = config.make_wsgi_app()
        
        
    serve(app, host='0.0.0.0', port=4010)
