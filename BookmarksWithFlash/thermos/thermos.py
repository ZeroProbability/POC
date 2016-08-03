from datetime import datetime
import os

from flask import Flask, render_template, url_for, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy

from logging import DEBUG

from forms import BookmarksForm
import models

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.logger.setLevel(DEBUG)
app.config['SECRET_KEY']='''\x04\xd2\t>[-\x06\x06\x1ar%I\xeb\x18\xd6*\x0f~\xae\xa26\x95@\xee'''
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'thermos.db')
db = SQLAlchemy(app)

bookmarks = []

def store_bookmark(url, description):
    bookmarks.append(dict(
        url = url, 
        description = description,
        user = "reindert",
        date = datetime.utcnow()
    ))

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", new_bookmarks = models.Bookmark.newest(5))

@app.route("/add", methods=['GET', 'POST'])
def add():
    form = BookmarksForm()
    if form.validate_on_submit():
        url = form.url.data
        description = form.description.data
        bm = models.Bookmark(url=url, description=description)
        db.session.add(bm)
        db.session.commit()
        store_bookmark(url, description)
        #app.logger.debug('stored url: {}'.format(url))
        flash("Stored bookmark '{}'".format(description))
        return redirect(url_for('index'))

    return render_template("add.html", form=form)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500

if __name__ == "__main__":
    app.run(debug=True)
