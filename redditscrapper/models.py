from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

# class srape(models.Model):

    # id = Column(Integer, primary_key=True)
    # post_title = Column('post_title', String)
    # submission_url = Column('dest_url', String,
    #                         nullable=True)  # dest_url = destination_url
    # short_link = Column('source_url', String, nullable=True)
    # total_upvotes = Column('upvotes', Integer, nullable=True)
    # tags = Column('tags', String, nullable=True)
    # subreddit = Column('subreddit', String, nullable=True)
    # blogger_posted_on = Column('blogger_posted_on', String, nullable=True)
    # posted = Column('posted', Boolean, nullable=True)

    # id = models.IntegerField(primary_key=True, auto_created=True)
#
# class Post(models.Model):
#     author = models.ForeignKey('auth.User')
#     title = models.CharField(max_length=200)
#     text = models.TextField()
#     created_date = models.DateTimeField(
#             default=timezone.now)
#     published_date = models.DateTimeField(
#             blank=True, null=True)
#
#     def publish(self):
#         self.published_date = timezone.now()
#         self.save()
#
#     def __str__(self):
#         return self.title