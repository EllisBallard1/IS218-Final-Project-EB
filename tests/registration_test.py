from flask_login import login_user, login_required, logout_user, current_user
import logging
from app import db
from app.db.models import User, Transactions

def test_registration(application):
    log = logging.getLogger("myApp")
    with application.app_context():
        assert db.session.query(User).count() == 0
        assert db.session.query(Transactions).count() == 0
        user = User("ellis@gmail.com", "abc123")
        db.session.add(user)
        db.session.commit()
        assert db.session.query(User).count() == 1

        user = User.query.filter_by(email="ellis@gmail.com").first()
        log.info(user)
        assert user.email == "ellis@gmail.com"

        db.session.delete(user)
        assert db.session.query(User).count() == 0
