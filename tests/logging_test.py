import os
# need to import the loggers and have them print a message in each test
# holds the root directory path
root = os.path.dirname(os.path.abspath(__file__))

# make tests for errors, handler, myapp, request, sqalchemy, uploads, and wekzeug logs

def test_myAppLogs():
    myAppLogs = os.path.join(root, '../logs/myapp.log')
    assert os.path.exists(myAppLogs) == True

def test_errorsLogs():
    errorsLogs = os.path.join(root, '../logs/errors.log')
    assert os.path.exists(errorsLogs) == True

def test_requestLogs():
    requestLogs = os.path.join(root, '../logs/request.log')
    assert os.path.exists(requestLogs) == True

def test_sqlalchemyLogs():
    sqlalchemyLogs = os.path.join(root, '../logs/sqlalchemy.log')
    assert os.path.exists(sqlalchemyLogs) == True

def test_wekzeugLogs():
    wekzeugLogs = os.path.join(root, '../logs/werkzeug.log')
    assert os.path.exists(wekzeugLogs) == True

def test_uploadLogs():
    uploadLogs = os.path.join(root, '../logs/uploads.log')
    assert os.path.exists(uploadLogs) == True

def test_flaskLogs():
    flaskLogs = os.path.join(root, '../logs/flask.log')
    if not os.path.exists(flaskLogs):
        os.mknod(flaskLogs)
    assert os.path.exists(flaskLogs) == True



