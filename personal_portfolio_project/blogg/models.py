from django.db import models

# Class equalt table - properties eauels columns
# check django models reference
# https://docs.djangoproject.com/en/3.0/ref/models/fields/
class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    datetime = models.DateField()

    def  __str__(self):
        return self.title
