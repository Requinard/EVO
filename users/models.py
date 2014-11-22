from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_delete, post_save
from django.dispatch import receiver

# Create your models here.
class Friendship(models.Model):
    user_sent = models.ForeignKey(User, related_name="inviter")
    user_received = models.ForeignKey(User, related_name="invitee")
    accepted = models.BooleanField(default=False)
    seen = models.BooleanField(default=False)

    def __unicode__(self):
        return "%s requested to %s" % (self.user_sent, self.user_received)


    """
    Determines if 2 users have a friendship
    """
    def DetermineRelation(self, user1, user2):
        relation = Friendship.objects.filter(user_sent=user1).filter(user_received=user2).filter(accepted=True)
        relation += Friendship.objects.filter(user_sent=user2).filter(user_received=user1).filter(accepted=True)

        if len(relation) > 0:
            return True

        return False

    """
    Returns pending request that were sent by the user
    """
    def get_sent_pending_requests(self, user):
        return Friendship.objects.filter(seen=False).filter(user_sent=user)

    """
    Returns pending requests that are waiting for a user
    """
    def get_received_pending_requests(self, user):
        return Friendship.objects.filter(seen=False).filter(user_received=user)

    """
    Get all accepted friend request that this user sent
    """
    def get_accepted_sent_request(self,user):
        return Friendship.objects.filter(seen=True).filter(accepted=True).filter(user_sent=user)

    """
    Get all accepted friend request that the user received
    """
    def get_accepted_received_requests(self, user):
        return Friendship.objects.filter(seen=True).filter(accepted=True).filter(user_received=user)

    """
    Gets all of a users friends
    """
    def get_user_friends(self, user):
        sent = Friendship.get_accepted_sent_request()
        received = Friendship.get_accepted_received_requests()

        return sent + received

    """
    Declines a request
    """
    def set_request_declined(self):
        self.seen = True
        self.accepted = False
        self.save()

    """
    Accepts a request
    """
    def set_request_accepted(self):
        self.seen = True
        self.accepted = True
        self.save()

class UserSettings(models.Model):
    user = models.OneToOneField(User, related_name="settings")

    track_location = models.BooleanField(default=True)

    def __unicode__(self):
        return self.user.username

    @receiver(post_save, sender=User)
    def create_settings_for_user(sender, instance=None, created=False, **kwargs):
        if created:
            UserSettings.objects.get_or_create(user=instance)

    @receiver(pre_delete, sender=User)
    def delete_settings_for_user(sender, instance=None, **kwargs):
        if instance:
            user_settings = UserSettings.objects.get(user=instance)
            user_settings.delete()

class UserLocation(models.Model):
    user = models.OneToOneField(User, related_name="location")

    lat = models.DecimalField(max_digits=10, decimal_places=7, default=0)
    lng = models.DecimalField(max_digits=10, decimal_places=7, default=0)
    verbose_loc = models.CharField(max_length=300, default="")

    @receiver(post_save, sender=User)
    def create_location_for_user(sender, instance=None, created=False, **kwargs):
        if created:
            UserLocation.objects.get_or_create(user=instance)

    @receiver(pre_delete, sender=User)
    def delete_location_for_user(sender, instance=None, **kwargs):
        if instance:
            user_location = UserLocation.objects.get(user=instance)
            user_location.delete()

    def __unicode__(self):
        return self.verbose_loc

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name="profile")


    @receiver(post_save, sender=User)
    def create_profile_for_user(sender, instance=None, created=False, **kwargs):
        if created:
            UserProfile.objects.get_or_create(user=instance)

    @receiver(pre_delete, sender=User)
    def delete_profile_for_user(sender, instance=None, **kwargs):
        if instance:
            user_profile = UserProfile.objects.get(user=instance)
            user_profile.delete()