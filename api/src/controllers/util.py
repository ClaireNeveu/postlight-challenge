from pyramid.view import view_config
import cattr

from models import Envelope

def json_endpoint(func):
    @view_config(renderer='json')
    def wrapped(request):
        raw_response = func(request)
        return cattr.unstructure(Envelope(raw_response))
    return wrapped
