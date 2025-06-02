import requests
from config.settings import BASE_URL

class GitHubAPI:
    def __init__(self):
        self.base_url = BASE_URL

    def get_root(self):
        url = f"{self.base_url}/"
        response = requests.get(url)
        return response

    def get_user(self, username):
        url = f"{self.base_url}/users/{username}"
        response = requests.get(url)
        return response
