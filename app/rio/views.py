from flask import request, render_template

from rio import app

@app.route('/')
def index():
    return 'Hello'
