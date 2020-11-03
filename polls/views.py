from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from .models import Poll, Answer
from .serializers import PollSerializer


def index(request):
    return HttpResponse('index page is here')


@api_view(['GET'])
def get_active_polls(request):
    polls = Poll.objects.filter(active=True)
    serializer = PollSerializer(polls, many=True)
    return Response(serializer.data, status=HTTP_200_OK)


@api_view(['GET'])
def get_user_voted_polls(request, user_id):
    # TODO optimize requests to DB
    polls = Poll.objects.prefetch_related('questions')
    answers = Answer.objects.filter(user_id=user_id).select_related('question')

    user_questions = set()
    for answer in answers:
        user_questions.add(answer.question)

    user_polls = set()
    for poll in polls:
        poll_questions = poll.questions.all()
        for question in poll_questions:
            if question in user_questions:
                user_polls.add(poll)
                break

    serializer = PollSerializer(user_polls, many=True)
    return Response(serializer.data, status=HTTP_200_OK)

