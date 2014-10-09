from django.db import models
from django.contrib.auth.models import User, Group

# Create your models here.
class Post(models.Model):
    ## Metadata
    owner = models.ForeignKey(User, verbose_name="Owner of this object")
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    group = models.ForeignKey(Group, blank=True, null=True)

    ## Post data
    post_body = models.TextField()
    loc_lat = models.FloatField(default=0)
    loc_long = models.FloatField(default=0)
    loc_verbose = models.TextField(default="0")

    class Meta:
        ordering = ("-date_created", "date_modified")

    def __str__(self):
        return self.post_body

    def get_location_num(self):
        return "%s, %s" % (self.loc_lat, self.loc_long)

    def get_post_comments(self):
        return PostComment.objects.filter(post_related=self)

class PostComment(models.Model):
    ## Metadata
    owner = models.ForeignKey(User, verbose_name="Owner of this object")
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    post_related = models.ForeignKey(Post)

    ## Post data
    post_body = models.TextField()
    loc_lat = models.FloatField()
    loc_long = models.FloatField()
    loc_verbose = models.TextField()