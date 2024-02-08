from src.views.http_types.http_response import HttpResponse
from .error_handler import handle_errors
from .error_types.http_bad_request import HttpBadRequestError

def test_handle_errors_bad_request():
    error = HttpBadRequestError("Invalid Input")
    response = handle_errors(error)
    response_body = {
        'errors': [{
            'title': 'BadRequest', 
            'detail': 'Invalid Input'
        }]
    }
    
    assert isinstance(response, HttpResponse)
    assert response.status_code == 400
    assert response.body == response_body

def test_handle_errors_generic():
    generic_error = Exception("Internal Server Error")
    response = handle_errors(generic_error)
    response_body = {
        'errors': [{
            'title': 'Server Error', 
            'detail': 'Internal Server Error'
        }]
    }
    
    assert isinstance(response, HttpResponse)
    assert response.status_code == 500
    assert response.body == response_body
