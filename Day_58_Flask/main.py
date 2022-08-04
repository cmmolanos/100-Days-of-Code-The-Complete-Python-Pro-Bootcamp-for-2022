from flask import Flask, render_template
from post import Post
import requests


url = "https://api.npoint.io/c790b4d5cab58020d391"
posts = requests.get(url).json()
post_objects = [Post(post['id'], post['title'], post['subtitle'], post['body']) for post in posts]

app = Flask(__name__)


@app.route('/')
@app.route('/blog')
def home():
    return render_template("index.html", posts=post_objects)


@app.route('/post/<int:index>')
def show_post(index):
    post = next(p for p in post_objects if p.id == index)
    return render_template("post.html", post=post)


if __name__ == "__main__":
    app.run(debug=True)
