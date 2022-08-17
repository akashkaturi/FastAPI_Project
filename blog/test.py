from fastapi import FastAPI
from fastapi.testclient import TestClient
from main import app
import logging

client = TestClient(app)


def test_app():
    response = client.get('/blog/1')
    assert response.status_code == 200
    assert 100 == 10 * 10


def test_add():
    logging.info("hello")
    print("hello")
