import pytest
import requests
from api_client.client import GitHubAPI

@pytest.fixture(scope="module")
def github():
    return GitHubAPI()

def test_status_code_for_existing_user(github):
    response = github.get_user("torvalds")  # Linus Torvalds
    assert response.status_code == 200

def test_user_has_public_repos(github):
    response = github.get_user("torvalds")
    data = response.json()
    assert data["public_repos"] > 0



