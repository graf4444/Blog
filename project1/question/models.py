from django.db import models

from django.conf import settings
from category.models import Category

class Question(models.Model):
    question_text = models.TextField()
    category = models.ForeignKey(Category, related_name='questions', on_delete=models.SET_NULL, null=True)
    autor = models.ForeignKey(settings.AUTH_USER_MODEL)
    pub_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question_text[:255]
    
    class Meta:
       ordering = ('-pub_date',)
 
