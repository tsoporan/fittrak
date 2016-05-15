from fittrack import db, login_manager

from . import bcrypt

class Base(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    created_on = db.Column(db.DateTime, default=db.func.now())
    updated_on = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())

class User(Base):
    username = db.Column(db.String, unique=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    authenticated = db.Column(db.Boolean, default=False)
    active = db.Column(db.Boolean, default=False)

    def set_password(self, plaintext):
        self.password = bcrypt.generate_password_hash(plaintext)

    def check_password(self, plaintext):
        return bcrypt.check_password_hash(self.password, plaintext)

    def is_active(self):
        """ A user is active once they have confirmed their account.  """
        return self.active

    def get_id(self):
        """ Flask login requires ID, this is email in our case. """
        return unicode(self.email)

    def is_authenticated(self):
        return self.authenticated

    def is_anonymous(self):
        """ Not supported """
        return False

    def __repr__(self):
        return '<User: %r>' % self.email

@login_manager.user_loader
def load_user(email):
    return User.query.filter_by(email=email).first()

class Workout(Base):
    """ A workout is composed of exercises """
    ended_on = db.Column(db.DateTime)
    exercise = db.relationship('Exercise', backref='workout', lazy='dynamic')
    routine = db.Column(db.Boolean, default=False)

class Exercise(Base):
    """ An exercise is composed of sets """
    username = db.Column(db.String, unique=True)
    set = db.relationship('Set', backref='exercise', lazy='dynamic')
    workout_id = db.Column(db.Integer, db.ForeignKey('workout.id'))

class Set(Base):
    """ A set relates to an exercise, an exercise has many sets.  """
    weight = db.Column(db.Integer)
    reps = db.Column(db.Integer)
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercise.id'))

