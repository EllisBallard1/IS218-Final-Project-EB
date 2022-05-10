import logging
import csv
import os
from flask import Flask, current_app

from app import db

# the actual upload occurs in the songs\__init__
# also need to test that the upload folder has been created


def test_csv_upload(application, client):
    filename = "music.csv"
    #log out to the logger what path is current
    #find the path for teh data path
    #look at the code where he creates folders and makes sure they exist


