from app import db
from app.auth.forms import *
from flask_login import FlaskLoginClient
from app.db.models import User


def test_success_login(application, client):
    form_test = login_form
    form_test.email.data = "ellis@gmail.com"
    form_test.password.data = "abc1234"
    assert form_test.validate


