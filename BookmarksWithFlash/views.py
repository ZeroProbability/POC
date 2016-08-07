from datetime import datetime

from flask import render_template, url_for, request, redirect, flash

from thermos.forms import BookmarksForm
from thermos.models import User, Bookmark

from thermos import app, db

#Fake login
def logged_in_user():
    return User.query.filter_by(username='anbu').first()

print '====> called once'

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", new_bookmarks = Bookmark.newest(5))

@app.route("/add", methods=['GET', 'POST'])
def add():
    form = BookmarksForm()
    if form.validate_on_submit():
        url = form.url.data
        description = form.description.data
        bm = Bookmark(user=logged_in_user(), url=url, description=description)
        #db.session.add(bm)
        db.session.commit()
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
