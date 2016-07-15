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

@app.route("/add", methods=('GET', 'POST'))
def add():
    if request.method == 'POST':
        pass
    return render_template("add.html")

@app.route("/quote")
def quote():
    return render_template("quote.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(debug=True)
