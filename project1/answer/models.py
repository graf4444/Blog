from django.db import models

from django.conf import settings
from question.models import Question

class Answer(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    text = models.TextField()
    date_create = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text[:255]

    class Meta:
        ordering = ('-date_create',)
