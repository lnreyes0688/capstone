from datetime import datetime as dt
from app import db
from flask_login import UserMixin
from app import login_manager
from werkzeug.security import check_password_hash, generate_password_hash

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    created_on = db.Column(db.DateTime, default=dt.utcnow)

    def save(self):
        self.set_password_hash(self.password)
        db.session.add(self)
        db.session.commit()

    def set_password_hash(self, pword):
        self.password = generate_password_hash(pword)

    def check_password_hash(self, pword):
        return check_password_hash(self.password, pword)

    #def from_dict(self,data):
       # for attr in ['first_name', 'last_name', 'email', 'password']:
         #   if attr in data:
         #       setattr(self, attr, data[attr])

    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'password': self.password,
            'created_on': dt.strftime(self.created_on, '%m/%d/%Y')
        }

    def __repr__(self):
        return f'<User: {self.email}>'


@login_manager.user_loader
def load_user(id):
    return User.query.get(id)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50))
    image = db.Column(db.String)
    title = db.Column(db.String)
    body = db.Column(db.Text)
    created_on = db.Column(db.DateTime, default=dt.utcnow)

    #


    def to_dict(self):
        return {
            'id': self.id,
            'email': self.email,
            'image': self.image,
            'title': self.title,
            'body': self.body,
            'created_on': dt.strftime(self.created_on, '%m/%d/%Y')
        }

    def __repr__(self):
        return f'<Post: [{self.email}]: {self.body[:20]}...>'



