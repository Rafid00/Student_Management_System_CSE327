from django.http import response
from django.test import TestCase,Client, client
from django.urls import reverse
from student_management_app.models import *

class BaseTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.add_course_url = reverse('student_app:manage_semester')   # Testing the  Manage semester feature
        return super().setUp()

class Test_Add_Course(BaseTest):
    def test_can_view_page_correctly(self):
        response = self.client.get(self.add_course_url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'manage_semester.html')