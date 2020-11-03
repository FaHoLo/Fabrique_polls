from django.contrib import admin

from .models import Poll, Question, Choice


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 0


@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    search_fields = [
        'name',
    ]
    list_display = [
        'name',
        'start_date',
        'end_date',
    ]

    inlines = [
        QuestionInline
    ]

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['start_date']
        return self.readonly_fields


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 0


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    search_fields = [
        'text',
        'question_type',
        'poll',
    ]
    list_display = [
        'id',
        'text',
        'question_type',
        'poll',
    ]
    inlines = [ChoiceInline]
