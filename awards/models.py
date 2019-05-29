from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=30)
    landing_page=models.ImageField(upload_to = 'images/', blank = True)
    description = models.TextField()
    link = models.CharField(max_length=30)
    def __str__(self):
        return self.title


class Profile(models.Model):
    user_id=models.IntegerField(default=0)
    username=models.CharField(max_length=30)
    contact=models.IntegerField(default=0)
    def __str__(self):
        return self.username


class Rating(models.Model):
    design_rate=models.IntegerField(default=0)
    usability_rate=models.IntegerField(default=0)
    content=models.IntegerField(default=0)
    def __str__(self):
        return self.design_rate
