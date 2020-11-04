from rest_framework.serializers import ModelSerializer

from .models import Poll, Answer, Question, Choice


class ChoiceSerializer(ModelSerializer):
    class Meta:
        model = Choice
        fields = '__all__'


class QuestionSerializer(ModelSerializer):
    choices = ChoiceSerializer(many=True)

    class Meta:
        model = Question
        fields = ['text', 'question_type', 'poll', 'choices']


class PollSerializer(ModelSerializer):
    questions = QuestionSerializer(many=True)

    class Meta:
        model = Poll
        fields = [
            'name', 'start_date', 'end_date',
            'description', 'active', 'questions'
        ]


class ActivePollSerializer(ModelSerializer):
    class Meta:
        model = Poll
        fields = ['name', 'description']


class AnswerSerializer(ModelSerializer):
    class Meta:
        model = Answer
        fields = ['question', 'choice', 'text']
