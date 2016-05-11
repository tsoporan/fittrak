from fittrack import db, login_manager

from . import bcrypt

class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    authenticated = db.Column(db.Boolean, default=False)
    active = db.Column(db.Boolean, default=False)
    created = db.Column(db.DateTime)

    def set_password(self, plaintext):
        self.password = bcrypt.generate_password_hash(plaintext)

    def check_password(self, plaintext):
        return bcrypt.check_password_hash(self.password, plaintext)

    def is_active(self):
        return self.active

    def get_id(self):
        """ Flask login requires ID, this is email in our case. """
        return self.email

    def is_authenticated(self):
        return self.authenticated

    def is_anonymous(self):
        """ Not supported """
        return False

    def __repr__(self):
        return '<User: %r>' % self.email
