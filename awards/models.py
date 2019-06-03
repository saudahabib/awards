from django.db import models

# Create your models here.
class Profile(models.Model):
    user_id=models.IntegerField(default=0)
    username=models.CharField(max_length=30)
    email=models.CharField(max_length=30, blank=True)
    profile_pix = models.ImageField(upload_to = 'images/', blank=True)
    def __str__(self):
        return self.username
    '''save profile method'''
    def save_profile(self):
        self.save()

    '''delete ratings method'''
    def delete_profile(self):
        deleted_profile = Profile.objects.all().delete()
        return deleted_profile


class Project(models.Model):
    title = models.CharField(max_length=30)
    landing_page=models.ImageField(upload_to = 'images/', blank = True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    description = models.TextField()
    link = models.CharField(max_length=50)
    def __str__(self):
        return self.title




class Rating(models.Model):
    design_rate=models.IntegerField(default=0)
    usability_rate=models.IntegerField(default=0)
    content=models.IntegerField(default=0)
    def __str__(self):
        return self.design_rate

    def save_rating(self):
        self.save()

    '''delete ratings method'''
    def delete_rating(self):
        delete_rates = Rating.objects.all().delete()
        return delete_rates
