from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Poll, Answer, Choice
from .serializers import PollSerializer


def index(request):
    return HttpResponse('index page is here')


@api_view(['GET'])
def get_active_polls(request):
    polls = Poll.objects.filter(active=True)
    serializer = PollSerializer(polls, many=True)
    return Response(serializer.data)

