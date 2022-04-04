import requests

API_ENDPOINT = "https://jsonplaceholder.typicode.com"


def get_all_posts():
    posts = requests.get(f"{API_ENDPOINT}/posts")
    return posts.json()


def get_post(id):
    post = requests.get(f"{API_ENDPOINT}/posts/{id}")
    return post.json()


def save_post(post):
    post = requests.post(
        f"{API_ENDPOINT}/posts",
        data={"userId": post.user_id, "title": post.title, "body": post.body},
    )
    return post.json()


def update_post(post_id, post):
    updated_post = requests.put(
        f"{API_ENDPOINT}/posts/{post_id}",
        data={"userId": post.user_id, "title": post.title, "body": post.body},
    )
    return updated_post.json()


def patch_post(post_id, post):
    updated_post = requests.patch(
        f"{API_ENDPOINT}/posts/{post_id}",
        data={"userId": post.user_id, "title": post.title, "body": post.body},
    )
    return updated_post.json()


def delete_post(id):
    post = requests.delete(f"{API_ENDPOINT}/posts/{id}")
    return post.json()


def get_post_comments(post_id):
    comments = requests.get(f"{API_ENDPOINT}/posts/{post_id}/comments")
    return comments.json()


def search_comments(post_id):
    payload = {"postId": post_id}
    comments = requests.get(f"{API_ENDPOINT}/comments", params=payload)
    return comments.json()
