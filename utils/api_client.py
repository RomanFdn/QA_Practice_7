from playwright.sync_api import APIRequestContext

class APIClient:
    def __init__(self, request_context: APIRequestContext):
        self.request = request_context

    def get_data(self, endpoint: str):
        return self.request.get(endpoint)

    def post_data(self, endpoint: str, payload: dict):
        return self.request.post(endpoint, data=payload)

    def put_data(self, endpoint: str, payload: dict):
        return self.request.put(endpoint, data=payload)

    def delete_data(self, endpoint: str):
        return self.request.delete(endpoint)