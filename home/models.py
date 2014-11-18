from django.db import models
from django.contrib.auth.models import User, Group

from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

# Create your models here.
class UserSettings(models.Model):
    user = models.OneToOneField(User, related_name="settings")

    track_location = models.BooleanField(default=True)

    def __unicode__(self):
        return self.user.username

    @receiver(post_save, sender=User)
    def create_profile_for_user(sender, instance=None, created=False, **kwargs):
        if created:
            UserSettings.objects.get_or_create(user=instance)

    @receiver(pre_delete, sender=User)
    def delete_profile_for_user(sender, instance=None, **kwargs):
        if instance:
            user_profile = UserSettings.objects.get(user=instance)
            user_profile.delete()

class UserLocation(models.Model):
    user = models.OneToOneField(User)

    lat = models.DecimalField(max_digits=10, decimal_places=7, default=0)
    lng = models.DecimalField(max_digits=10, decimal_places=7, default=0)
    verbose_loc = models.CharField(max_length=300, default="")

    @receiver(post_save, sender=User)
    def create_profile_for_user(sender, instance=None, created=False, **kwargs):
        if created:
            UserLocation.objects.get_or_create(user=instance)

    @receiver(pre_delete, sender=User)
    def delete_profile_for_user(sender, instance=None, **kwargs):
        if instance:
            user_profile = UserLocation.objects.get(user=instance)
            user_profile.delete()


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