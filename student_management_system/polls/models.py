import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin



# Django Documentation
class Question(models.Model):
    question_text = models.CharField(max_length=120)
    pub_date = models.DateTimeField("Date Published")

    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    # Redo
    def comparator(self):
        if self.pub_date.year==datetime.datetime.year:
            return self.question_text
        else:
            return self.pub_date #

    class Meta:
        ordering = ('-pub_date', )

    def __str__(self):
        return self.question_text

    def recently_published(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choices(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE, related_name='Question')
    choice_text = models.CharField(max_length=120)
    votes = models.IntegerField(default=0)


    class Meta:
        ordering = ('-votes', )
        verbose_name='Choices'
        verbose_name_plural='Choices'

    def __str__(self):
        return self.choice_text

