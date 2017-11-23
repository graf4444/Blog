from django.db import models

class Category(models.Model):
    name_category = models.CharField(max_length=512)
    
    def __str__(self):
        return self.name_category

    class Meta:
        ordering = ('name_category',)
