from django.db import models
from django.utils import timezone


class Poll(models.Model):
    name = models.CharField('название', max_length=250)
    start_date = models.DateTimeField('дата старта', default=timezone.now)
    end_date = models.DateTimeField('дата окончания')
    description = models.TextField('описание')


class Question(models.Model):
    pass


class Choice(models.Model):
    pass
