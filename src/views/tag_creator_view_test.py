from unittest.mock import patch
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.controller.tag_creator_controller import TagCreatorController
from .tag_creator_view import TagCreatorView

@patch.object(TagCreatorController, 'create')
def test_validate_and_create(mock_create):
    mock_request_body = {
        "product_code": "cod-test"
    }
    
    mock_create_result = {
        "data": {
            "type": "Tag Image", 
            "count": 1, 
            "path": f'{mock_request_body['product_code']}.png'
            }
        }
    mock_create.return_value = mock_create_result
    mock_http_request = HttpRequest(body=mock_request_body)
    
    tag_creator_view = TagCreatorView()
    result = tag_creator_view.validate_and_create(mock_http_request)
    
    assert isinstance(result, HttpResponse)
    assert "data" in result.body
    assert "type" in result.body["data"]
    assert "count" in result.body["data"]
    assert "path" in result.body["data"]
    
    assert result.body == mock_create_result    
    assert result.body["data"]["type"] == "Tag Image"
    assert result.body["data"]["count"] == 1
    assert result.body["data"]["path"] == f'{mock_request_body['product_code']}.png'
    
