import unittest

from fittrack import db, app
from fittrack.models import User

class FittrackTestCase(unittest.TestCase):

    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False

        db.create_all()

        self.app = app.test_client()

    def register(self, email, password):
        return self.app.post('/register/', data=dict(
            email = email,
            password = password,
        ), follow_redirects=True)

    def login(self, email, password):
        return self.app.post('/login/', data=dict(
            email = email,
            password = password,
        ), follow_redirects=True)

    def logout(self):
        return self.app.get('/logout/', follow_redirects=True)

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_index(self):
        rv = self.app.get('/')
        self.assertTrue('Home' in rv.data)

    def test_register(self):
        rv = self.app.get('/register/')
        self.assertTrue('Register' in rv.data)

        rv = self.register('b@b.bb', 'abc')
        self.assertTrue('Thanks for registering' in rv.data)

        self.assertTrue(User.query.filter_by(email='b@b.bb').first())

    def test_login(self):
        rv = self.app.get('/login/')
        self.assertTrue('Login' in rv.data)

        self.register('a@a.aa', 'abc')
        rv = self.login('a@a.aa', 'abc')

        self.assertTrue('Home' in rv.data)

    def test_login_logout(self):

        self.register('a@a.aa', 'abc')
        self.login('a@a.aa', 'abc')
        rv = self.logout()

        self.assertTrue('Home' in rv.data)

if __name__ == '__main__':
    unittest.main()
