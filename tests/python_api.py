import re
from playwright.sync_api import expect

from playwright.sync_api import sync_playwright

def test_get_users():
    with sync_playwright() as p:
        request = p.request.new_context()
        
        response = request.get("https://reqres.in/api/users?page=2")
        
        assert response.status == 200
        data = response.json()
        
        assert data["page"] == 2
        assert len(data["data"]) > 0


def test_create_user():
    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        request = p.request.new_context()

        response = request.post(
            "https://reqres.in/api/users",
            data = {
                "name": "Tua",
                "job": "QA Tester"
            }
        )

        assert response.status == 201
        data = response.json()

        assert data["name"] == "Tua"
        assert data["job"] == "QA Tester"      


def test_update_user():
    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        request = p.request.new_context()

        response = request.put(
            "https://reqres.in/api/users/2",
            data={"job": "Senior QA"}
        )

        assert response.status == 200
        data = response.json()

        assert data["job"] == "Senior QA"  


def test_delete_user():
    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        request = p.request.new_context()

        response = request.delete("https://reqres.in/api/users/2")

        assert response.status == 204