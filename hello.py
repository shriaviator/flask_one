
from flask import Flask, render_template, url_for

app = Flask(__name__)
# assuming data is a avilable as a list of objects
posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2022'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2022'
    }
]

# postinal args , keyword arguments ,arbitrary keyword arguments ,arbitary positional argumrns


@app.route("/")
@app.route("/home")
def hello_world():
    return render_template("home.html", posts=posts, title="ekdoteen")


@app.route("/about")
def about_world():
    return render_template("about.html")


if __name__ == '__main__':
    app.run(debug=True)
