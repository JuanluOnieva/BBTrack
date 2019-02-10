
from flask import Flask, request
from flask_restplus import Resource, Api, fields


app = Flask(__name__)                  #  Create a Flask WSGI application

"""Version de la api, con titulo y descripcion"""
api = Api(app, version='1.0', title='bbTrack API', description='A simple API for query bbTrack')


if __name__ == '__main__':
    app.r