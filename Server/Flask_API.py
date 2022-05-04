# itspacchu/theenigmacodex
import flask
from flask import Flask, redirect, url_for, request
import os
APP = Flask(__name__)

@APP.route('/')
def home():
    """
    Base API home page
    """
    return "<h1> API Home Page </h1>"

@APP.route('/api',methods = ['GET'])
def data_collector(username, email):
    """
    This function is used to fetch GET request from the user
    This shoudn't be used for production purposes
    eg:
    /login?username=myusername&email=someusername@something.com
    """
    if(request.method == 'GET'):
        username = request.args.get('username')
        email = request.args.get('email')
        # Do what you want to do with username and email here




        # end returns a HTML page, remove it if you dont want anything to be returned
        return f"<h1> Hello {username}! </h1> <h2> Your email is {email} </h2>"
    else:
        return "<h1> Invalid Method , USE GET </h1><br> <code> /login?username=myusername&email=someusername@something.com </code>"

if __name__ == '__main__':
    app = flask.Flask(__name__)
    app.run()