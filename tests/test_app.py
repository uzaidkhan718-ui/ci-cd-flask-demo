from app import app

def test_home():
    client = app.test_client()
    res = client.get("/")
    assert res.status_code == 200
    assert b"Welcome to My DevOps CI/CD Project" in res.data

def test_status():
    client = app.test_client()
    res = client.get("/status")
    assert res.status_code == 200
    data = res.get_json()
    assert data["ok"] is True
