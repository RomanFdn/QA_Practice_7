from utils.api_client import APIClient

def test_get_post_by_id(api_context):
    client = APIClient(api_context)

    response = client.get_data("/posts/1")
    
    assert response.status == 200
    data = response.json()
    assert data["id"] == 1
    assert "title" in data

def test_create_new_post(api_context):
    client = APIClient(api_context)
    payload = {"title": "QA Test", "body": "Integration testing", "userId": 1}
    
    response = client.post_data("/posts", payload)
    
    assert response.status == 201
    data = response.json()
    assert data["title"] == "QA Test"
    assert "id" in data

def test_update_post(api_context):
    client = APIClient(api_context)
    payload = {"id": 1, "title": "Updated Title", "body": "Updated body", "userId": 1}
    
    response = client.put_data("/posts/1", payload)
    
    assert response.status == 200
    data = response.json()
    assert data["title"] == "Updated Title"

def test_delete_post(api_context):
    client = APIClient(api_context)
    
    response = client.delete_data("/posts/1")
    
    assert response.status == 200