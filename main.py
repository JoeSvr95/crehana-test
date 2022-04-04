import graphene
from src import api
from fastapi import FastAPI
from models import Post, Comment
from db.db_conf import db_session
from gql import RootQuery, RootMutation
from schemas import PostSchema, CommentSchema
from starlette_graphene3 import GraphQLApp, make_graphiql_handler

db = db_session.session_factory()

app = FastAPI()
schema = graphene.Schema(query=RootQuery, mutation=RootMutation)

app.add_route(
    "/graphql",
    GraphQLApp(
        schema=schema,
        on_get=make_graphiql_handler(),
    ),
)

# Posts integration
@app.get("/posts")
def get_posts():
    posts = api.get_all_posts()
    for post in posts:
        p = PostSchema(
            user_id=post.get("userId"), title=post.get("title"), body=post.get("body")
        )
        db_post = Post(userId=p.user_id, title=p.title, body=p.body)
        db.add(db_post)
        db.commit()
        db.refresh(db_post)
    return posts


@app.get("/posts/{post_id}")
def get_post(post_id):
    post = api.get_post(post_id)
    return post


@app.post("/posts")
def save_post(post: PostSchema):
    new_post = api.save_post(post)
    return new_post


@app.put("/posts/{post_id}")
def update_post(post_id, post: PostSchema):
    updated_post = api.update_post(post_id, post)
    return updated_post


@app.patch("/posts/{post_id}")
def patch_post(post_id, post: PostSchema):
    patch_post = api.patch_post(post_id, post)
    return patch_post


@app.delete("/posts/{post_id}")
def delete_post(post_id):
    post = api.delete_post(post_id)
    return post


# Comments integrations
@app.get("/posts/{post_id}/comments")
def get_post_comments(post_id):
    comments = api.get_post_comments(post_id)
    for comment in comments:
        c = CommentSchema(
            post_id=comment.get("postId"),
            name=comment.get("name"),
            email=comment.get("email"),
            body=comment.get("body"),
        )
        db_comment = Comment(postId=c.post_id, name=c.name, email=c.email, body=c.body)
        db.add(db_comment)
        db.commit()
        db.refresh(db_comment)
    return comments


@app.get("/comments")
def search_comment(post_id):
    comments = api.search_comments(post_id)
    return comments
