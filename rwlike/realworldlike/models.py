from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse



class Campaign(models.Model):
    name = models.CharField(max_length=255)
    keyword = models.SlugField(max_length=64)
    number = models.IntegerField()

    def __unicode__(self):
        return self.name + ' campaign'


class PosterDesign(models.Model):
    name = models.CharField(max_length=255)
    campaign = models.ForeignKey(Campaign)
    qr_left = models.IntegerField(default=0)
    qr_top = models.IntegerField(default=0)
    qr_size = models.IntegerField(default=30)

    def __unicode__(self):
        return self.name


class PrintRun(models.Model):
    user = models.ForeignKey(User)
    design = models.ForeignKey(PosterDesign)
    location = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return 'http://omnicronsoftware.com/hackspace/leaflet.php?printrunid=' + str(self.pk)


class Poster(models.Model):
    printrun = models.ForeignKey(PrintRun)
    location = models.TextField(null=True, blank=True)


class Spot(models.Model):
    content = models.CharField(max_length=255)
#    poster = models.ForeignKey(Poster)
    inNumber = models.CharField(max_length=255)
    sender = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    credits = models.CharField(max_length=255, blank=True, null=True)

    def __unicode__(self):
        return self.content + ' from ' + self.inNumber

    def get_absolute_url(self):
        return reverse('spot_detail', kwargs={'pk': self.pk})

    # def save
