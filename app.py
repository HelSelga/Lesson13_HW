from flask import Flask, request, render_template, send_from_directory
from functions import get_posts_by_tag, get_all_tags

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)


@app.route("/")
def page_index():
    tags = get_all_tags()
    return render_template('index.html', tags=tags)


@app.route("/tag")
def page_tag():
    tag_name = request.args.get('tag')
    posts = get_posts_by_tag(tag_name)
    return render_template('post_by_tag.html', posts=posts, tag=tag_name)


@app.route("/post", methods=["GET", "POST"])
def page_post_create():
    pass


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


if __name__ == "__main__":
    app.run()
