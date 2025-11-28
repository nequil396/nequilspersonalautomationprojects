import re
from playwright.sync_api import expect

from playwright.sync_api import sync_playwright

def test_get_users():
    with sync_playwright() as p:
        request = p.request.new_context(
            extra_http_headers={
                "Authorization": "Bearer your_token_here",
                "Accept": "application/json",
                "X-Api-Key" : "reqres-free-v1"
                }
            )
        
        response = request.get("https://reqres.in/api/users")
        
        assert response.status == 200
        data = response.json()
        
        assert data["page"] == 1
        assert len(data["data"]) > 0


