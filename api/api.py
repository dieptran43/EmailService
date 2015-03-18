from django.http import HttpResponse, HttpResponseServerError
from django.views.decorators.http import require_POST
from django.core.mail import EmailMultiAlternatives, EmailMessage
from rest_framework import viewsets, serializers, routers
from rest_framework.views import APIView
from rest_framework.decorators import detail_route, list_route, api_view
from rest_framework.response import Response
import json


@api_view(["POST"])
def send_email(request):
    """
    Send an email with mandrill template
    ---
    parameters:
        - name: FromEmail
          description: This is from email address field
        - name: ToRecipients
          description: This is from email address field
        - name: Body
          description: This is from email address field
        - name: Subject
          description: This is from email address field

    """

    request_content = request.body

    request_body = json.loads(request_content)

    from_email = request_body.get("FromEmail")
    to_recipients = request_body.get("ToRecipients")
    body = request_body.get("Body")
    subject = request_body.get("Subject")

    msg = EmailMultiAlternatives(subject=subject, body=body, from_email=from_email, to=to_recipients)

    try:
        msg.send()

        response = { "Message": 'Your email has been sent.' }

        return HttpResponse(json.dumps(response), content_type='application/json')

    except Exception as ex:
        return server_error(ex)


@api_view(["POST"])
def send_email_template(request):
    """
    Send an email with mandrill template
    ---
    parameters:
        - name: FromEmail
          description: This is from email address field
        - name: ToRecipients
          description: This is from email address field
        - name: Subject
          description: This is from email address field
        - name: TemplateName
          description: This is from email address field
        - name: TemplateContent
          description: This is from email address field
        - name: UseTemplateSubject
          description: This is from email address field
        - name: UseTemplateFrom
          description: This is from email address field

    """

    request_content = request.body

    request_body = json.loads(request_content)

    from_email = request_body.get("FromEmail", "")
    to_recipients = request_body.get("ToRecipients")
    subject = request_body.get("Subject", "")
    template_name = request_body.get("TemplateName")
    template_content = request_body.get("TemplateContent")
    use_template_subject = request_body.get("UseTemplateSubject", False)
    use_template_from = request_body.get("UseTemplateFrom", False)

    msg = EmailMessage(subject=subject, from_email=from_email, to=to_recipients)

    msg.template_name = template_name
    msg.template_content = template_content
    msg.use_template_subject = use_template_subject
    msg.use_template_from = use_template_from

    try:
        msg.send()

        response = { "Message": 'Your email has been sent.' }

        return HttpResponse(json.dumps(response), content_type='application/json')

    except Exception as ex:
        return server_error(ex)

def server_error(exception):
    error_response = {
        "Message": exception.log_message,
    }
    error_response_json = json.dumps(error_response)

    return HttpResponseServerError(error_response_json)


email_message_router = routers.DefaultRouter()
#email_message_router.register('sendemailw', SendEmailViewSet)




