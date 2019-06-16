from main import app


def test():
    # test that viewing the page renders without template errors

    app.testing = True
    client = app.test_client()
    assert client.get('/collections').status_code == 200
