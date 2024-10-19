import pytest
from pasted import load_app
from starlette.testclient import TestClient


def test_load_app_none():
    with pytest.raises(LookupError) as ctx:
        load_app(None)
    assert str(ctx.value) == "missing environment variable PLASTER_URI"


def test_load_app_yaml(root):
    app = load_app(str(root / "test.yaml"))
    assert app is not None
    with TestClient(app) as client:
        response = client.get("/")
        assert response.status_code == 200
        assert response.text == "Hello, World!"
