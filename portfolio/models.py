from django.db import models
from django.db.models.fields import CharField, TextField, URLField
from django.db.models.fields.files import ImageField

# Create your models here.

class Project(models.Model):
    title = CharField(max_length=100)
    description = CharField(max_length=250)

    image = ImageField(upload_to='portfolio/images')
    # the path upload to will start from the media folder
    # so we will upload to personal_portfolio(external)/media/portfolio/images
    url = URLField(blank=True)
    # blank=True means the parameter is optional

    def __str__(self):
        return f"{self.title}"



