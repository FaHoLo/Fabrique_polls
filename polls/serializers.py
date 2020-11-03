from rest_framework.serializers import ModelSerializer

from .models import Poll


class PollSerializer(ModelSerializer):
    class Meta:
        model = Poll
        fields = ['name', 'description']
