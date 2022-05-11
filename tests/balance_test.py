from app import db
from app.db.models import User

from flask_login import FlaskLoginClient
from app.auth.forms import *

def test_balance(application):
    application.test_client_class = FlaskLoginClient
    user = User('ellis@gmail.com', 'abc1234')
    db.session.add(user)
    db.session.commit()

    assert user.email == 'ellis@gmail.com'
    assert user.balance == 0.00

    user.balance += 15.5
    assert user.balance == 15.5
    user.balance -= 10.5
    assert user.balance == 5.00
    db.session.delete(user)