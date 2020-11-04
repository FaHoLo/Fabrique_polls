from django.db import transaction
from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED

from .models import Poll, Answer, Question
from .serializers import (CroppedPollSerializer, AnswerSerializer,
                          PollSerializer, QuestionSerializer,
                          VotedPollSerializer)


class QuestionsViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAdminUser]


class PollsViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    permission_classes = [permissions.IsAdminUser]


@api_view(['GET'])
def get_active_polls(request):
    polls = Poll.objects.filter(active=True)
    serializer = CroppedPollSerializer(polls, many=True)
    return Response(serializer.data, status=HTTP_200_OK)


@api_view(['GET'])
def get_user_voted_polls(request, user_id):
    # TODO optimize requests to DB
    polls = Poll.objects.prefetch_related('questions')
    answers = Answer.objects.filter(user_id=user_id).select_related('question')

    user_voted_questions = list()
    for answer in answers:
        user_voted_questions.append(answer.question)

    user_voted_polls = set()
    for poll in polls:
        poll_questions = poll.questions.all()
        for question in poll_questions:
            if question in user_voted_questions:
                user_voted_polls.add(poll)
                break

    # TODO Optimize it, its too complicated
    for poll in user_voted_polls:
        for question in poll.questions.all():
            for answer in answers:
                if answer.question != question:
                    continue
                question.answer = answer

    serializer = VotedPollSerializer(user_voted_polls, many=True)
    return Response(serializer.data, status=HTTP_200_OK)


@transaction.atomic
@api_view(['POST'])
def get_user_vote(request):
    serializer = AnswerSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    user_id = request.user.id
    if not user_id:
        # TODO generate random number to anonim user session
        user_id = 12345

    answer = Answer.objects.create(
        user_id=user_id,
        question=serializer.validated_data['question'],
        text=serializer.validated_data['text']
    )
    answer.choice.set(serializer.validated_data['choice'])

    return Response(AnswerSerializer(answer).data, status=HTTP_201_CREATED)
