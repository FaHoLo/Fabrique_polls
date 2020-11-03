from django.db import models
from django.utils import timezone


class Poll(models.Model):
    name = models.CharField('название', max_length=250)
    start_date = models.DateTimeField('дата старта', default=timezone.now)
    end_date = models.DateTimeField('дата окончания')
    description = models.TextField('описание')


class Question(models.Model):
    CHOICE = 'CHC'
    CHOICES = 'CHS'
    TEXT = 'TXT'
    QUESTION_TYPE_CHOICES = [
        (CHOICE, 'Выбрать один вариант'),
        (CHOICES, 'Выбрать несколько вариантов'),
        (TEXT, 'Ответ текстом'),
    ]
    text = models.TextField('текст вопроса')
    question_type = models.CharField('тип вопроса', max_length=3,
                                     choices=QUESTION_TYPE_CHOICES, default=CHOICE)


class Choice(models.Model):
    pass
