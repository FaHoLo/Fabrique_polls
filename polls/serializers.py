from rest_framework.serializers import ModelSerializer

from .models import Poll, Answer


class PollSerializer(ModelSerializer):
class ActivePollSerializer(ModelSerializer):
    class Meta:
        model = Poll
        fields = ['name', 'description']


class AnswerSerializer(ModelSerializer):
    class Meta:
        model = Answer
        fields = ['question', 'choice', 'text']
