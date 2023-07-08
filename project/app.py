#!/usr/bin/env python3
from functools import wraps
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from projects import routes
import jwt
import os

from config import Config

app = Flask(__name__)
app.config.from_object(Config)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


def get_key(val, dic):
    for k, v in dic.items():
        if val == value:
            return key


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if "x-access-token" in request.headers:
            token = request.headers["x-access-token"]
        if not token:
            return jsonify({"message": "Token is missing!"}), 401
        try:
            data = jwt.decode(token, app.config["SECRET_KEY"],
                              algorithms=["HS256"])
            from project.models import Users

            loggedInUser = Users.query.filter_by(public_id=data
                                                 ["public_id"]).first()
        except Exception as ex:
            return jsonify({"message": "Token is invalid!"}), 401
        return f(loggedInUser, *args, **kwargs)

    return decorated


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
