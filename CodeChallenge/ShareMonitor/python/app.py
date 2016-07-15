#!/usr/bin/env python
# encoding: utf-8

from logging import DEBUG
from datetime import datetime

from flask import Flask, render_template, request, redirect, url_for, flash
app = Flask(__name__)
app.logger.setLevel(DEBUG)

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/add", method=('GET', 'POST'))
def add():
    if request.method == 'POST':
        pass
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
