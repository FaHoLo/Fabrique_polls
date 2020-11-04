from rest_framework.serializers import ModelSerializer, ValidationError

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
    questions = QuestionSerializer(many=True, required=False)

    def update(self, instance, validated_data):
        if validated_data.get('start_date'):
            raise ValidationError("start_date is immutable once set.")
        return super(PollSerializer, self).update(instance, validated_data)

    class Meta:
        model = Poll
        fields = [
            'name', 'start_date', 'end_date',
            'description', 'active', 'questions'
        ]


class CroppedPollSerializer(ModelSerializer):
    class Meta:
        model = Poll
        fields = ['name', 'description']


class AnswerSerializer(ModelSerializer):
    class Meta:
        model = Answer
        fields = ['question', 'choice', 'text']


class QuestionWithUserAnswerSerializer(ModelSerializer):
    answers = AnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = ['text', 'answers']


class VotedPollSerializer(ModelSerializer):
    questions = QuestionWithUserAnswerSerializer(many=True)

    class Meta:
        model = Poll
        fields = ['name', 'description', 'active', 'questions']
