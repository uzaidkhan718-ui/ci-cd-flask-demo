import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app

def test_home():
    client = app.test_client()
    resp = client.get("/")
    assert resp.status_code == 200

def test_status():
    client = app.test_client()
    resp = client.get("/status")
    assert resp.json["ok"] == True

