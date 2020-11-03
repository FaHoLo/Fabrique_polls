from django.core.validators import MinValueValidator
from django.db import models
from django.utils import timezone


class Poll(models.Model):
    name = models.CharField('название', max_length=250)
    start_date = models.DateTimeField('дата старта', default=timezone.now)
    end_date = models.DateTimeField('дата окончания')
    description = models.TextField('описание')
    active = models.BooleanField('активный', default=True, db_index=True)

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'

    def __str__(self):
        return self.name


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
    poll = models.ForeignKey(Poll, verbose_name='Опрос',
                             on_delete=models.CASCADE, related_name='questions')

    def __str__(self):
        return f'{self.id} {self.question_type}'

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Choice(models.Model):
    question = models.ForeignKey(Question, verbose_name='варианты ответа',
                                 on_delete=models.CASCADE, related_name='choices')
    text = models.CharField('ответ', max_length=200)

    class Meta:
        verbose_name = 'Вариант ответа'
        verbose_name_plural = 'Варианты ответа'

    def __str__(self):
        return f'{self.id} {self.text}'


class Answer(models.Model):
    user_id = models.IntegerField('id пользователя', validators=[MinValueValidator(1)])
    question = models.ForeignKey(Question, verbose_name='вопрос', on_delete=models.CASCADE,
                                 related_name='answers')
    choice = models.ManyToManyField(Choice, related_name='answers', blank=True)
    text = models.TextField('текстовый ответ', blank=True)

    class Meta:
        verbose_name = 'Ответ пользователя на вопрос'
        verbose_name_plural = 'Ответы пользователя на вопрос'

    def __str__(self):
        return f'{self.user_id} {self.question} {self.choice}'
