import unittest
from main import app

""""
Tests using unittest

"""


class TestCases(unittest.TestCase):
    def test1(self):
        # test that viewing the post page renders without template errors
        app.testing = True
        client = app.test_client()
        self.assertEqual(client.get('/post/c0wgwg').status_code == 200)

    def test2(self):
        # test that viewing the user page renders without template errors
        app.testing = True
        client = app.test_client()
        self.assertEqual(client.get('/user/putty1574').status_code == 200)

    def test3(self):
        # test that viewing the collections page renders without template error
        app.testing = True
        client = app.test_client()
        self.assertEqual(client.get('/collections').status_code == 200)

    def test4(self):
        # test that viewing the login page renders without template errors
        app.testing = True
        client = app.test_client()
        self.assertEqual(client.get('/login').status_code == 200)

    def test5(self):
        # test that viewing the signup page renders without template error
        app.testing = True
        client = app.test_client()
        self.assertEqual(client.get('/signup').status_code == 200)

    def test6(self):
        # test that viewing the subreddit page renders without template errors
        app.testing = True
        client = app.test_client()
        self.assertEqual(client.get('/elonmusk').status_code == 200)


