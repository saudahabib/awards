from django.test import TestCase
from .models import Profile, Project, Rating
# Create your tests here.
'''test behaviors'''

class ProfileTestClass(TestCase):
    '''setup method'''
    def setUp(self):
        self.prof1 = Profile(
        user_id=5,
        username='codignoramus',
        email='saudababs00@gmail.com')
    def test_instance(self):
        self.assertTrue(isinstance(self.prof1, Profile))

    #test saving
    def test_save_profile(self):
        self.prof1.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles)>0)
    #test deleting
    def test_delete_profile(self):
        self.prof1.delete_profile()
        deleted_profile=Profile.objects.all()
        self.assertTrue(len(deleted_profile)==0)

class RatingTestClass(TestCase):
    #set up method
    def setUp(self):
        self.rate1 = Rating(design_rate=8, usability_rate=6, content=5)
    #test isinstance
    def test_instance(self):
        self.assertTrue(isinstance(self.rate1, Rating))

    #test saving method
    def test_save_ratings(self):
        self.rate1.save_rating()
        ratings = Rating.objects.all()
        self.assertTrue(len(ratings)>0)

    #test deleting
    def test_delete_profile(self):
        self.rate1.delete_rating()
        deleted_rates = Rating.objects.all()
        self.assertTrue(len(deleted_rates)==0)

class MoreTestsAreComing(TestCase):
    pass
