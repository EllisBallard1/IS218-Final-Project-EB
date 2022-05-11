import logging
import os


def upload_tansaction_test(client, application):
    application.app_context()
    application.secret_key = "Secret Key"
    application.config['WTF_CSRF_ENABLED'] = False
    response = client.post('/login', data=dict(email="ellisb@gmail.com", password="abc123"),
                           follow_redirects=True)
    assert response.status_code == 200





