from django.http import HttpResponse, HttpResponseServerError
from django.views.decorators.http import require_POST
from django.core.mail import EmailMultiAlternatives, EmailMessage
from rest_framework import viewsets, serializers, routers
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import detail_route, list_route, api_view
from rest_framework.response import Response
import json
from models import Email

class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = ('pk', 'from_email')

class EmailViewSet(viewsets.ModelViewSet):

    queryset = Email.objects.all()

    serializer_class = EmailSerializer
    search_fields = ('email_status')
    ordering_fields = ('created')

    def list(self, request, *args, **kwargs):
        """
        List available emails.
        ---
          parameters_strategy: merge
          parameters:
            - name: from_email
              description: from email address must be a valid email address
              required: false
              type: string
              paramType: query
        """
        return super(EmailViewSet, self).list(request, *args, **kwargs)

    @detail_route(methods=['post'])
    def send_test_email(self, pk=None, request, *args, **kwargs):

        return Response(status=status.HTTP_200_OK())


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
        import pdb;pdb.set_trace()
        return server_error(ex)

def server_error(exception):
    error_response = {
        "Message": exception.log_message,
    }
    error_response_json = json.dumps(error_response)

    return HttpResponseServerError(error_response_json)


email_message_router = routers.DefaultRouter()
email_message_router = routers.DefaultRouter()
email_message_router.register('email', EmailViewSet)




