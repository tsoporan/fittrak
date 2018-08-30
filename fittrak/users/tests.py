from django.test import TestCase, Client
from django.contrib.auth import get_user_model

from fittrak.schema import schema


class UserTestCases(TestCase):
    def setUp(self):
        User = get_user_model()
        User.objects.create_user('Foo', 'foo@bar.com', 'FooBar')

    def test_viewer_access(self):
        client = Client()

        resp = client.get('/graphql')

        self.assertRedirects(resp, '/accounts/login/?next=/graphql')

        loggedIn = client.login(username='Foo', password='FooBar')

        self.assertTrue(loggedIn)

        resp = client.get('/graphql')

        self.assertEquals(resp.status_code, 400)
        self.assertEquals(resp.json()["errors"],
                          [{
                              "message": "Must provide query string."
                          }])
