import main
from unittest import TestCase
from unittest.mock import Mock, patch
from pprint import pprint
from schemas.post import PostSchema

from src.api import *


class TestIntegration(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.posts = [
            {
                "userId": 1,
                "id": 1,
                "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
                "body": "quia et suscipitsuscipit recusandae consequuntur expedita et cumreprehenderit molestiae ut ut quas totamnostrum rerum est autem sunt rem eveniet architecto",
            },
            {
                "userId": 2,
                "id": 11,
                "title": "et ea vero quia laudantium autem",
                "body": "delectus reiciendis molestiae occaecati non minima eveniet qui voluptatibusaccusamus in eum beatae sitvel qui neque voluptates ut commodi qui inciduntut animi commodi",
            },
            {
                "userId": 3,
                "id": 21,
                "title": "asperiores ea ipsam voluptatibus modi minima quia sint",
                "body": "repellat aliquid praesentium dolorem quosed totam minus non itaquenihil labore molestiae sunt dolor eveniet hic recusandae veniamtempora et tenetur expedita sunt",
            },
            {
                "userId": 4,
                "id": 31,
                "title": "ullam ut quidem id aut vel consequuntur",
                "body": "debitis eius sed quibusdam non quis consectetur vitaeimpedit ut qui consequatur sed aut inquidem sit nostrum et maiores adipisci atquequaerat voluptatem adipisci repudiandae",
            },
            {
                "userId": 5,
                "id": 42,
                "title": "commodi ullam sint et excepturi error explicabo praesentium voluptas",
                "body": "odio fugit voluptatum ducimus earum autem est incidunt voluptatemodit reiciendis aliquam sunt sequi nulla doloremnon facere repellendus voluptates quiaratione harum vitae ut",
            },
        ]

        cls.comments = [
            {
                "postId": 1,
                "id": 1,
                "name": "id labore ex et quam laborum",
                "email": "Eliseo@gardner.biz",
                "body": "laudantium enim quasi est quidem magnam voluptate ipsam eostempora quo necessitatibusdolor quam autem quasireiciendis et nam sapiente accusantium",
            },
            {
                "postId": 1,
                "id": 2,
                "name": "quo vero reiciendis velit similique earum",
                "email": "Jayne_Kuhic@sydney.com",
                "body": "est natus enim nihil est dolore omnis voluptatem numquamet omnis occaecati quod ullam atvoluptatem error expedita pariaturnihil sint nostrum voluptatem reiciendis et",
            },
            {
                "postId": 11,
                "id": 51,
                "name": "molestias et odio ut commodi omnis ex",
                "email": "Laurie@lincoln.us",
                "body": "perferendis omnis essevoluptate sit mollitia sed perferendisnemo nostrum quivel quis nisi doloribus animi odio id quas",
            },
            {
                "postId": 11,
                "id": 52,
                "name": "esse autem dolorum",
                "email": "Abigail.OConnell@june.org",
                "body": "et enim voluptatem totam laudantiumimpedit nam labore repellendus enim earum autconsectetur mollitia fugit qui repellat expedita suntaut fugiat vel illo quos aspernatur ducimus",
            },
            {
                "postId": 21,
                "id": 101,
                "name": "perspiciatis magnam ut eum autem similique explicabo expedita",
                "email": "Lura@rod.tv",
                "body": "ut aut maxime officia sed aliquam et magni autemveniam repudiandae nostrum odio enim eum optio automnis illo quasi quibusdam inventore explicaboreprehenderit dolor saepe possimus molestiae",
            },
            {
                "postId": 21,
                "id": 102,
                "name": "officia ullam ut neque earum ipsa et fuga",
                "email": "Lottie.Zieme@ruben.us",
                "body": "aut dolorem quos ut nonaliquam unde iure minima quod ullam quifugiat molestiae tempora voluptate vel laboresaepe animi et vitae numquam ipsa",
            },
            {
                "postId": 31,
                "id": 151,
                "name": "ut quas facilis laborum voluptatum consequatur odio voluptate et",
                "email": "Cary@taurean.biz",
                "body": "quos eos sint voluptatibus similique iusto perferendis omnis voluptasearum nulla cumquedolorem consequatur officiis quis consequatur aspernatur nihil ullam etenim enim unde nihil labore non ducimus",
            },
            {
                "postId": 31,
                "id": 152,
                "name": "quod doloremque omnis",
                "email": "Tillman_Koelpin@luisa.com",
                "body": "itaque veritatis explicaboquis voluptatem mollitia soluta id nondoloribus nobis fuga providentnesciunt saepe molestiae praesentium laboriosam",
            },
            {
                "postId": 42,
                "id": 206,
                "name": "deserunt eveniet quam vitae velit",
                "email": "Sophie@antoinette.ca",
                "body": "nam iusto minus expedita numquamet id quisvoluptatibus minima porro facilis dolores beatae aut sitaut quia suscipit",
            },
            {
                "postId": 42,
                "id": 207,
                "name": "asperiores sed voluptate est",
                "email": "Jessika@crystel.ca",
                "body": "nulla quos harum commodiaperiam qui et dignissimosreiciendis ut quia est corrupti itaquelaboriosam debitis suscipit",
            },
        ]

        cls.new_post = {
            "userId": 6,
            "id": 51,
            "title": "soluta aliquam aperiam consequatur illo quis voluptas",
            "body": "sunt dolores aut doloribusdolore doloribus voluptates tempora etdoloremque et quocum asperiores sit consectetur dolorem"
        }

        cls.deleted_post = {
            "userId": 2,
            "id": 11,
            "title": "et ea vero quia laudantium autem",
            "body": "delectus reiciendis molestiae occaecati non minima eveniet qui voluptatibusaccusamus in eum beatae sitvel qui neque voluptates ut commodi qui inciduntut animi commodi",
        }

    @patch("src.api.requests.get")
    def test_get_posts(self, mock_get_all_posts):
        mock_get_all_posts.return_value = Mock()
        mock_get_all_posts.return_value.json.return_value = self.posts

        response = get_all_posts()
        self.assertEqual(len(response), len(self.posts))

    @patch("src.api.requests.get")
    def test_get_post(self, mock_get_post):
        expected_post = {
            "userId": 3,
            "id": 21,
            "title": "asperiores ea ipsam voluptatibus modi minima quia sint",
            "body": "repellat aliquid praesentium dolorem quosed totam minus non itaquenihil labore molestiae sunt dolor eveniet hic recusandae veniamtempora et tenetur expedita sunt",
        }

        mock_get_post.return_value = Mock()
        mock_get_post.return_value.json.return_value = self.posts[2]

        response = get_post(21)
        self.assertEqual(response, expected_post)

    @patch("src.api.requests.post")
    def test_save_post(self, mock_save_post):
        new_post = PostSchema(
            user_id=6, 
            id=51, 
            title="soluta aliquam aperiam consequatur illo quis voluptas", 
            body="sunt dolores aut doloribusdolore doloribus voluptates tempora etdoloremque et quocum asperiores sit consectetur dolorem"
        )

        expceted_response = {
            "userId": 6,
            "id": 51,
            "title": "soluta aliquam aperiam consequatur illo quis voluptas",
            "body": "sunt dolores aut doloribusdolore doloribus voluptates tempora etdoloremque et quocum asperiores sit consectetur dolorem"
        }

        mock_save_post.return_value = Mock()
        mock_save_post.return_value.json.return_value = self.new_post

        response = main.save_post(new_post)

        self.assertEqual(response, expceted_response)

    @patch("src.api.requests.delete")
    def test_delete_post(self, mock_delete_post):
        mock_delete_post.return_value = Mock()
        mock_delete_post.return_value.json.return_value = self.posts[1]

        resposne = delete_post(2)
        self.assertEqual(resposne, self.deleted_post)

    @patch("src.api.requests.get")
    def test_get_comments(self, mock_get_posts_comments):
        post_id = 1
        comments_from_post = [
            {
                "postId": 1,
                "id": 1,
                "name": "id labore ex et quam laborum",
                "email": "Eliseo@gardner.biz",
                "body": "laudantium enim quasi est quidem magnam voluptate ipsam eostempora quo necessitatibusdolor quam autem quasireiciendis et nam sapiente accusantium",
            },
            {
                "postId": 1,
                "id": 2,
                "name": "quo vero reiciendis velit similique earum",
                "email": "Jayne_Kuhic@sydney.com",
                "body": "est natus enim nihil est dolore omnis voluptatem numquamet omnis occaecati quod ullam atvoluptatem error expedita pariaturnihil sint nostrum voluptatem reiciendis et",
            }
        ]
        mock_get_posts_comments.return_value = Mock()
        mock_get_posts_comments.return_value.json.return_value = list(filter(lambda c: c.get("postId") == post_id, self.comments))

        response = get_post_comments(post_id)
        self.assertEqual(response, comments_from_post)

    
