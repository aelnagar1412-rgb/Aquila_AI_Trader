import json
import os
from flask import session, redirect, url_for, request

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
USERS_FILE = os.path.join(BASE_DIR, "users.json")

def check_login(username, password):
    with open(USERS_FILE, "r") as f:
        users = json.load(f)
    return users.get(username) == password

def login_required(func):
    def wrapper(*args, **kwargs):
        if not session.get("user"):
            return redirect(url_for("login"))
        return func(*args, **kwargs)
    wrapper.__name__ = func.__name__
    return wrapper
