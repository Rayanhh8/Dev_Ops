import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from app import app
import mongomock

# --- Fixture pour remplacer MongoDB ---
@pytest.fixture
def client(monkeypatch):
    mock_client = mongomock.MongoClient()
    monkeypatch.setattr("app.client", mock_client)
    monkeypatch.setattr("app.db", mock_client.blog_db)
    monkeypatch.setattr("app.messages_col", mock_client.blog_db.messages)
    return app.test_client()

# --- Test 1 : route /messages GET retourne 200 et liste vide initialement ---
def test_get_messages_empty(client):
    response = client.get("/messages")
    assert response.status_code == 200
    assert response.get_json() == []

# --- Test 2 : route /messages POST ajoute un message ---
def test_post_message(client):
    data = {"text": "Bonjour Test"}
    response = client.post("/messages", json=data)
    assert response.status_code == 201
    json_data = response.get_json()
    assert json_data["status"] == "success"

# --- Test 3 : route /messages GET retourne le message ajouté ---
def test_get_messages_after_post(client):
    # Ajouter un message
    client.post("/messages", json={"text": "Message 1"})
    client.post("/messages", json={"text": "Message 2"})
    
    response = client.get("/messages")
    assert response.status_code == 200
    messages = response.get_json()
    assert len(messages) == 2
    assert messages[0]["text"] == "Message 1" or messages[1]["text"] == "Message 2"

# --- Test 4 : POST sans texte renvoie quand même 201 ---
def test_post_empty_message(client):
    response = client.post("/messages", json={})
    assert response.status_code == 201
    json_data = response.get_json()
    assert json_data["status"] == "success"
