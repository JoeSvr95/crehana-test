import graphene
from models import Post, Comment
from db.db_conf import db_session
from schemas import PostSchema, PostModel, CommentSchema, CommentModel

db = db_session.session_factory()


class RootQuery(graphene.ObjectType):
    all_posts = graphene.List(PostModel)
    all_posts_by_user = graphene.List(PostModel, user_id=graphene.Int(required=True))
    all_comments = graphene.List(CommentModel)
    all_comments_by_post_id = graphene.List(
        CommentModel, post_id=graphene.Int(required=True)
    )
    post_by_id = graphene.Field(PostModel, post_id=graphene.Int(required=True))
    comment_by_id = graphene.Field(CommentModel, comment_id=graphene.Int(required=True))
    comments_by_name = graphene.List(CommentModel, name=graphene.String(required=True))
    comment_by_id_and_post_id = graphene.Field(
        CommentModel,
        comment_id=graphene.Int(required=True),
        post_id=graphene.Int(required=True),
    )

    def resolve_all_posts(self, info):
        query = PostModel.get_query(info)
        return query.all()

    def resolve_all_posts_by_user(self, info, user_id):
        return db.query(Post).filter(Post.userId == user_id)

    def resolve_all_comments(self, info):
        query = CommentModel.get_query(info)
        return query.all()

    def resolve_all_comments_by_post_id(self, info, post_id):
        return db.query(Comment).filter(Comment.postId == post_id)

    def resolve_post_by_id(self, info, post_id):
        return db.query(Post).filter(Post.id == post_id).first()

    def resolve_comment_by_id(self, info, comment_id):
        return db.query(Comment).filter(Comment.id == comment_id).first()

    def resolve_comments_by_name(self, info, name):
        return db.query(Comment).filter(Comment.name == name)

    def resolve_comment_by_id_and_post_id(self, info, comment_id, post_id):
        return (
            db.query(Comment)
            .filter(Comment.id == comment_id, Comment.postId == post_id)
            .first()
        )


class CreateNewPost(graphene.Mutation):
    class Arguments:
        user_id = graphene.Int(required=True)
        title = graphene.String(required=True)
        body = graphene.String(required=True)

    ok = graphene.Boolean()

    @staticmethod
    def mutate(root, info, user_id, title, body):
        post = PostSchema(user_id=user_id, title=title, body=body)
        db_post = Post(userId=post.user_id, title=post.title, body=body)
        db.add(db_post)
        db.commit()
        db.refresh(db_post)
        ok = True
        return CreateNewPost(ok=ok)


class CreateNewComment(graphene.Mutation):
    class Arguments:
        post_id = graphene.Int(required=True)
        name = graphene.String(required=True)
        email = graphene.String(required=True)
        body = graphene.String(required=True)

    ok = graphene.Boolean()

    @staticmethod
    def mutate(root, info, post_id, name, email, body):
        comment = CommentSchema(post_id=post_id, name=name, email=email, body=body)
        db_comment = Comment(
            postId=comment.post_id,
            name=comment.name,
            email=comment.email,
            body=comment.body,
        )
        db.add(db_comment)
        db.commit()
        db.refresh(db_comment)
        ok = True
        return CreateNewComment(ok=ok)


class RootMutation(graphene.ObjectType):
    create_new_post = CreateNewPost.Field()
    create_new_comment = CreateNewComment.Field()
