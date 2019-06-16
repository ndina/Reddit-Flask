from main import app


class TestCases:
    def test1(self):
        # test that viewing the page renders without template errors
        app.testing = True
        client = app.test_client()
        assert client.get('/user/dina2505').status_code == 200

    def test2(self):
        # test that viewing the page renders without template errors
        app.testing = True
        client = app.test_client()
        assert client.get('/user/Euvoria').status_code == 200


    def test(self):
        # test that viewing the page renders without template errors
        app.testing = True
        client = app.test_client()
        assert client.get('/user/putty1574').status_code == 200




