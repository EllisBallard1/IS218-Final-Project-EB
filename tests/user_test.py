import logging

from app import db
from app.db.models import User, Transactions
from faker import Faker

def test_adding_user(application):
    log = logging.getLogger("myApp")
    with application.app_context():
        assert db.session.query(User).count() == 0
        assert db.session.query(Transactions).count() == 0
        #showing how to add a record
        #create a record
        user = User('ellis@gmail.com', 'passwordTesting')
        #add it to get ready to be committed
        db.session.add(user)
        #call the commit
        db.session.commit()
        #assert that we now have a new user
        assert db.session.query(User).count() == 1
        #finding one user record by email
        user = User.query.filter_by(email='ellis@gmail.com').first()
        log.info(user)
        #asserting that the user retrieved is correct
        assert user.email == 'ellis@gmail.com'
        #this is how you get a related record ready for insert
        user.transaction = [Transactions(500, 'CREDIT'), Transactions(-200, 'DEBIT')]
        #commit is what saves the transactions
        db.session.commit()
        assert db.session.query(Transactions).count() == 2
        transaction1 = Transactions.query.filter_by(AMOUNT=500).first()
        assert transaction1.AMOUNT == 500
        #changing the amount of the transaction
        transaction1.AMOUNT = 600
        #saving the new transaction amount
        db.session.commit()
        transaction2 = Transactions.query.filter_by(AMOUNT=-200).first()
        assert transaction2.AMOUNT == -200
        #checking cascade delete
        db.session.delete(user)
        assert db.session.query(User).count() == 0
        assert db.session.query(Transactions).count() == 0




