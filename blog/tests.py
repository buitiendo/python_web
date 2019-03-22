from django.test import TestCase
from .models import Post
# Create your tests here.
class BlogTests(TestCase):
    def setUp(self):
        Post.objects.create(title='myTitle', body="just a Test") # khi chạy testcase sẽ tạo ra database ảo không ảnh hưởng đến db đang chạy.

    def test_string_representation(self): # tạo hàm kiểm tra xem Post có trả về title không?
        post = Post(title="My enter title")
        self.assertEqual(str(post), post.title)

    def test_post_listview(self): # kiểm tra list có trả về  status_code 200 không, có trả về link không?
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "myTitle") # kiểm tra xem post có trả về title không?
        self.assertTemplateUsed(response,  'blog/blog.html') # kiểm tra nó có sử  dụng teplate không?

    def test_post_detail_view(self):
        response = self.client.get('/blog/1/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "myTitle")
        self.assertTemplateUsed(response,  'blog/post.html')
