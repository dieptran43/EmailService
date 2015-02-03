from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.core.mail import EmailMultiAlternatives
import json

@require_POST
def send_email(request):

    requestContent = request.body

    requestBody = json.loads(requestContent)

    from_email = requestBody.get("FromEmail")
    to_recipients = requestBody.get("ToReceipients")
    body = requestBody.get("Body")
    subject = requestBody.get("Subject")

    msg = EmailMultiAlternatives(subject=subject, body=body, from_email=from_email, to=to_recipients)

    msg.send()

    mandrill_response = json.dumps(msg.mandrill_response[0])

    return HttpResponse(mandrill_response)



