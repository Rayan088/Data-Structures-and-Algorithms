import pytest
from backend.app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True # Enables flask testing mode

    # Client simulates HTTP requests
    with app.test_client() as client:
        yield client

# Function for Flask test setup

def test_orderbook(client):
    response = client.get("/orderbook")

    assert response.status_code == 200
    data = response.get_json()

    assert "bids" in data
    assert "asks" in data

# Test for executed orderbook flask route and JSON reponse

def test_trades(client):
    response = client.get("/trades")

    assert response.status_code == 200

# Test for executed trade flask route

def test_market(client):
    response = client.get("/market")

    assert response.status_code == 200

# Test for executed market flask route

def test_stats(client):
    response = client.get("/stats")

    assert response.status_code == 200

# Test for executed stats flask route

def test_wallet(client):
    response = client.get("/wallet")

    assert response.status_code == 200
    data = response.get_json()

    assert "btc" in data
    assert "usd" in data

# Test for executed wallet flask route and JSON response

def test_user_orders(client):
    response = client.get("/userorders")

    assert response.status_code == 200

# Test for user orders flask route

def test_place_order(client):
    response = client.post("/order", json={"side":"SELL", "price":1000, "quantity": 0.1})

    assert response.status_code == 200

    data = response.get_json()

    assert data["status"] == "order placed"

# Test for user placing order