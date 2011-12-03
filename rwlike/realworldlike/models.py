from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse



class Campaign(models.Model):
    name = models.CharField(max_length=255)
    keyword = models.SlugField(max_length=64)


class PosterDesign(models.Model):
    name = models.CharField(max_length=255)
    campaign = models.ForeignKey(Campaign)


class PrintRun(models.Model):
    user = models.ForeignKey(User)
    design = models.ForeignKey(PosterDesign)
    location = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)


class Poster(models.Model):
    location = models.TextField(null=True, blank=True)


class Spot(models.Model):
    content = models.CharField(max_length=255)
    inNumber = models.CharField(max_length=255)
    sender = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('spot_detail', kwargs={'pk': self.pk})
