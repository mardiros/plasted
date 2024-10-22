import pytest
from webtest import TestApp

from plasted import load_app


def test_load_app_none():
    with pytest.raises(LookupError) as ctx:
        load_app(None)
    assert str(ctx.value) == "missing environment variable PLASTER_URI"


def test_load_app_yaml(root):
    app = load_app(str(root / "test.yaml"))
    assert app is not None
    client = TestApp(app)
    response = client.get("/")
    assert response.status_code == 200
    assert response.text == "Hello, World!"
