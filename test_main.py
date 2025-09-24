from main import app
import pytest

@pytest.fixture
def client():
    app.config['TESTING'] = True
    return app.test_client()

def test_get_subscriptions(client):
    res = client.get('/subscriptions')
    assert res.status_code == 200

def test_create_subscription(client):
    subscription = {
        "email": "carmen@gmail.com",
        "name": "Carmen",
        "plan": "standard"
    }
    
    res = client.post('/subscriptions', json = subscription)
    assert res.status_code == 201
    
    datos = res.get_json()
    assert datos["email"] == "carmen@gmail.com"
    assert datos["name"] == "Carmen"

def test_get_subscription_with_id(client):
    subscription = {
        "email": "carmen@gmail.com",
        "name": "Carmen", 
        "plan": "standard"
    }
    r1 = client.post('/subscriptions', json = subscription)
    nuevo = r1.get_json()
    
    r2 = client.get(f'/subscriptions/{nuevo["id"]}')
    assert r2.status_code == 200