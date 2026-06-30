import requests


class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, path, params=None):
        return requests.get(f"{self.base_url}{path}", params=params)

    def post(self, path, json=None):
        return requests.post(f"{self.base_url}{path}", json=json)

    def put(self, path, json=None):
        return requests.put(f"{self.base_url}{path}", json=json)

    def delete(self, path):
        return requests.delete(f"{self.base_url}{path}")
