import logging
import os


def test_upload_tansaction(client, application):
    application.app_context()
    application.secret_key = "Secret Key"
    application.config['WTF_CSRF_ENABLED'] = False
    response = client.post('/login', data=dict(email="ellis@gmail.com", password="abc123"),
                           follow_redirects=True)
    assert response.status_code == 200

    transactions = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "transactions.csv"))
    file_data = open(transactions, "rb")
    data = {"file": (file_data, "transactions.csv")}
    response = client.post('/transactions/upload', data=data, follow_redirects=True, buffered=True, content_type='multipart/form-data')
    assert response.status_code == 200
    response = client.get("/transactions")
    assert response.status_code == 200

    assert os.path.exists(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'app/uploads', 'transactions.csv'))) == True
    response = client.get('/logout', follow_redirects=True)
    assert response.status_code == 200




