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

        # Set up a user
        u = User()
        u.email = 'a@a.aa'
        u.set_password('abc')
        db.session.add(u)
        db.session.commit()

        self.assertTrue(User.query.filter_by(email='a@a.aa').first() != None)

        self.user = u

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_index(self):
        rv = self.app.get('/')
        self.assertTrue('Home' in rv.data)

    def test_login(self):
        rv = self.app.get('/login/')
        self.assertTrue('Login' in rv.data)

        rv = self.app.post('/login/', data=dict(
            email = 'a@a.aa',
            password = 'abc',
        ), follow_redirects=True)

        self.assertTrue('Home' in rv.data)

    def test_login_logout(self):
        pass

if __name__ == '__main__':
    unittest.main()
