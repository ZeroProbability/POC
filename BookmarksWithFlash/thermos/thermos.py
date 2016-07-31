from flask import Flask, render_template, url_for, request, redirect, flash
from datetime import datetime

from logging import DEBUG

app = Flask(__name__)
app.logger.setLevel(DEBUG)
app.config['SECRET_KEY']='''\x04\xd2\t>[-\x06\x06\x1ar%I\xeb\x18\xd6*\x0f~\xae\xa26\x95@\xee'''

bookmarks = []

def store_bookmark(url):
    bookmarks.append(dict(
        url = url, 
        user = "reindert",
        date = datetime.utcnow()
    ))

def new_bookmarks(num):
    return sorted(bookmarks, key=lambda bm: bm['date'], reverse=True)[:num]


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", new_bookmarks = new_bookmarks(5))

@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == "POST":
        url = request.form['url']
        store_bookmark(url)
        #app.logger.debug('stored url: {}'.format(url))
        flash("Stored bookmark '{}'".format(url))
        return redirect(url_for('index'))

    return render_template("add.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500

if __name__ == "__main__":
    app.run(debug=True)
