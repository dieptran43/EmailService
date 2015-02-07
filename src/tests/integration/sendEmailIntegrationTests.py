from unittest import TestCase
import json
import requests

class SendEmailIntegrationTests(TestCase):

    def setUp(self):
        pass


    def test_send_email(self):

        request = {
            "FromEmail": "konrad@tangentsolutions.co.za",
            "ToRecipients": ["konrad@tangentsolutions.co.za"],
            "Body": "This is an integration test email",
            "Subject": "This is a integration test subject",
        }

        json_request = json.dumps(request)
        url = "http://localhost:8000/email/send"

        server_response = requests.post(url, json_request)

        json_server_response = json.loads(server_response.content)

        assert json_server_response["status"] == 'sent'
        assert server_response.status_code == 200, "Response return successful status 200"

    def test_send_email_template(self):

        request = {
            "FromEmail": "konrad@tangentsolutions.co.za",
            "ToRecipients": ["kehinze@gmail.com"],
            "Subject": "This is a test subject for email template",
            "TemplateName": "tangent_test",
            "TemplateContent": { "Test1": "test content 1" }
        }

        url = "http://localhost:8000/email/sendtemplate"

        json_request = json.dumps(request)

        server_response = requests.post(url, json_request)

        json_server_response = json.loads(server_response.content)

        assert json_server_response["status"] == 'sent'
        assert server_response.status_code == 200, "Response return successful status 200"