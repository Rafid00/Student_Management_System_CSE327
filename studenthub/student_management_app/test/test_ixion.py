from django.http import response
from django.test import TestCase,Client, client
from django.urls import reverse
from student_management_app.models import *

class BaseTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.add_course_url = reverse('student_app:add_course')
        self.send_notice_url = reverse('student_app:send_notice')
        return super().setUp()

class Test_Send_Notice(BaseTest):
    def test_can_view_page_correctly(self):
        response = self.client.get(self.send_notice_url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'send_notice.html')


