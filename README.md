# Posts API

This projects was written using FastAPI and Graphene for a GraphQL API. All the information is stored in a PostgresQL database. The project is dockerized and can be ran with:

```shell
docker-compose up
```

It uses SQLAlchemy as a ORM and Alembic for migrations.

## Integration with JSONPlaceholder

The integration is made up of an API Rest that hits the JSONPlaceholder API endpoints and saves the data returned data in the database. The following endpoints are available:

- `GET /posts` -> Retrieves all posts and saves them in the database
- `GET /posts/<post_id>` -> Posts a new post
- `POST /posts` -> Creates a new post
- `PUT /posts/<post_id>` -> Updates a post
- `PATCH /posts/<post_id>` -> Updates a post
- `GET /posts/<post_id>/comments` -> Retrives all comments from a post and saves them in the database
- `GET /comments?post_id=<post_id>` -> Retrives all comments from a post

In order to save data from JSONPlaceholder, use the `/posts` endpoint to save posts and the `/posts/<post_id>/comments` to save comments of a particular post.

## GraphQL API

Once the data has been saved you can use the GraphQL API to query and save new data to the database. Just use the endpoint:

`GET /graphql`

The following queries are available:

- `allPosts` -> Retrieves all posts
- `allPostByUser` -> Retrieves all posts by an user ID
- `allComments` -> Retrives all comments from all posts
- `allCommentsByPostId` -> Retrives all comments by a post ID
- `postById` -> Gets a post by its ID
- `commentById` -> Gets a comment by its ID
- `commentsByName` -> Gets a comment by the name of the person that posted the comment
- `commentByIdAndPostId` -> Gets a comment by its ID and the post ID it belongs to

## Tests

To run unit test use the following command:

```shell
docker-compose run app python -m unittest
```