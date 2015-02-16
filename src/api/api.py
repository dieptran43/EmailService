from django.http import HttpResponse, HttpResponseServerError
from django.views.decorators.http import require_POST
from django.core.mail import EmailMultiAlternatives, EmailMessage
import json

@require_POST
def send_email(request):
    print('send email')

    request_content = request.body

    request_body = json.loads(request_content)

    from_email = request_body.get("FromEmail")
    to_recipients = request_body.get("ToRecipients")
    body = request_body.get("Body")
    subject = request_body.get("Subject")

    msg = EmailMultiAlternatives(subject=subject, body=body, from_email=from_email, to=to_recipients)

    msg.send()

    mandrill_response = json.dumps(msg.mandrill_response[0])

    return HttpResponse(mandrill_response)

@require_POST
def send_email_template(request):
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

        mandrill_response = json.dumps(msg.mandrill_response[0])

        return HttpResponse(mandrill_response)

    except Exception as ex:
        return server_error(ex)

def server_error(exception):
    error_response = {
        "Message": exception.log_message,
    }
    error_response_json = json.dumps(error_response)

    return HttpResponseServerError(error_response_json)




