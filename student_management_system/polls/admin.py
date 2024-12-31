from django.contrib import admin
from .models import Question, Choices

# Register your models here.


class ChoiceInline(admin.StackedInline):
    model = Choices
    extra = 3


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ["question_text", "pub_date", "recently_published"]
    search_fields = ["question_text"]
    inlines = [ChoiceInline]


#
# @admin.register(Choices)
# class ChoiceAdmin(admin.ModelAdmin):
#     list_display = ['choice_text','votes']
#     list_filter = ['choice_text']
