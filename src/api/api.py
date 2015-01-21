from rest_framework import routers, serializers, viewsets
from models import EmailMessage

class EmailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EmailMessage,

class EmailViewSet(viewsets.ModelViewSet):
    model = EmailMessage
    serializer_class = EmailSerializer

    def get_queryset(self):
        return EmailMessage.objects.all()

email_router = routers.DefaultRouter()
email_router.register('emailmessage', EmailViewSet)

