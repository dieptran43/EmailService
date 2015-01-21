from django.test import TestCase
import json
import requests

class EmailServiceTest(TestCase):

    def setUp(self):
        pass

    def test_json_send_email(self):
       requests.post("http://127.0.0.1:8000/sendemail")

    def test_send_email(self):

        emailRequest = {
            "from_email": "noreply@tangentsolutions.co.za",
            "from_name": "email service",
            "template_name": "tangent-test",
            "template_content": [
                {
                    "name": "CompanyName",
                    "content": "Example text"
                }
            ],

        }

        requests.post("", json={})
        self.__email_service.Send()

    def test_send_email_template(self):

        self.__email_service.SendEmailTemplate()
