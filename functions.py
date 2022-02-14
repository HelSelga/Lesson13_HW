import json
POST_PATH = "posts.json"


def load_info_from_json():
    with open(POST_PATH, "r", encoding="utf-8") as f:
        posts = json.load(f)

    if posts:
        return posts
    else:
        return []


def get_posts_by_tag(tag_name):
    posts = load_info_from_json()
    post_match = []
    search_object = f'#{tag_name}'
    for post in posts:
        if search_object in post['content']:
            post_match.append(post)

    return post_match


def get_tags_by_string(string):
    tags = set()
    for word in string.split(" "):
        if word.startswith("#"):
            tags.add(word[1:])
    return tags


def get_all_tags():
    posts = load_info_from_json()
    tags = set()
    for post in posts:
        post_content = post.get('content')
        tags_in_posts = get_tags_by_string(post_content)
        tags = tags.union(tags_in_posts)

    return list(tags)