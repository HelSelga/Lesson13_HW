from flask import Flask, request, render_template, send_from_directory, redirect
from functions import get_posts_by_tag, get_all_tags
import json

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


@app.route("/post", methods=["GET"])
def page_post_get():
    return render_template("post_form.html")


@app.route("/post", methods=["POST"])
def page_post_create():
    files = request.files.get("picture")
    content = request.form.get("content")
    filename = files.filename
    path = './'+UPLOAD_FOLDER+'/'+filename
    files.save(path)

    if not files:
        return redirect('/post')

    pic_new_url = '/'+UPLOAD_FOLDER+'/'+filename

    return render_template("post_uploaded.html", picture=pic_new_url, content=content)


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


if __name__ == "__main__":
    app.run()
