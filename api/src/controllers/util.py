from pyramid.view import view_config
from pyramid.response import Response
import cattr

from models import Envelope

def json_endpoint(func):
    @view_config(renderer='json')
    def wrapped(request):
        raw_response = func(request)
        
        if type(raw_response) is Response:
            return raw_response
            
        if type(raw_response) is not Envelope:
            raw_response = Envelope(raw_response)
            
        return cattr.unstructure(raw_response)
    return wrapped
