from django.http import response
from django.test import TestCase,Client, client
from django.urls import reverse
from student_management_app.models import *

class BaseTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_home_url = reverse('student_app:login_home')
        return super().setUp()

class Test_Add_Course(BaseTest):
    def test_can_view_page_correctly(self):
        response = self.client.get(self.login_home_url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'login.html')
