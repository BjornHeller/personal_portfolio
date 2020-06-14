from django.db import models

# Class equalt table - properties eauels columns
# check django models reference
# https://docs.djangoproject.com/en/3.0/ref/models/fields/
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)

    def  __str__(self):
        return self.title
