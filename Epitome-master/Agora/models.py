from __future__ import unicode_literals
import datetime

from django.db import models
from django.utils import timezone


class VoteMain(models.Model):
    username = models.CharField(max_length=200)
    area = models.IntegerField(default=0)
    vote_proxy = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published')
    def __unicode__(self):              # __unicode__ on Python 2
        return self.question_text
    def was_published_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.pub_date <= now

		
class VoteResult(models.Model):
    vote_main = models.OneToOneField(VoteMain)
    votes = models.IntegerField(default=0)
    def __unicode__(self):              # __unicode__ on Python 2
        return self.votes
        

class VoteTexts(models.Model):
    vote_m = models.OneToOneField(VoteMain)
    vote_name = models.CharField(max_length=200)
    vote_description = models.CharField
    def __unicode__(self):              # __unicode__ on Python 2
        return self.vote_name

	
