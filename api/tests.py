from django.utils import unittest
from django.test.client import RequestFactory, Client
import json

class ApiTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_one_plus_one(self):

        one = 1

        assert one == 1

class SendEmailIntegrationTests(unittest.TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        pass

    def test_send_email(self):
        url = '/email/send/'

        request_data = {
            "FromEmail": "konrad@tangentsolutions.co.za",
            "ToRecipients": ["kehinze@gmail.com"],
            "Subject": "This is test subject from our unit test. ",
            "Body": "This is a test body from our unit test."
        }

        request_data_json = json.dumps(request_data)

        response = self.client.post(url, data=request_data_json, content_type='application/json')

        self.assertEqual(response.status_code, 200)

    def test_send_email_template(self):
        url = '/email/sendtemplate/'

        request_data = {
            "FromEmail": "konrad@tagentsolutions.co.za",
            "ToRecipients": ["kehinze@gmail.com"],
            "Subject" : "This is test email tempalte subject",
            "TemplateName": "tangent-test",
            "TemplateContent": {
                "Name": "TestName",
                "Surname": "Testsurname"
            },
            "UseTemplateFrom": True,
            "UseTemplateSubject":True
        }

        request_data_json = json.dumps(request_data)

        response = self.client.post(url, data=request_data_json, content_type='application/json')

        self.assertEqual(response.status_code, 200)





