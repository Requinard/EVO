from django.db import models
from django.contrib.auth.models import Group, User
from django.db.models.signals import pre_delete, post_save
from django.dispatch import receiver

# Create your models here.
class UserGroup(models.Model):
    user = models.ForeignKey(User, related_name="owner")
    included_users = models.ManyToManyField(User, related_name="included_users")
    name = models.CharField(max_length=120, default="friends")

    def __unicode__(self):
        return self.name

    @receiver(post_save, sender=User)
    def create_group_for_user(sender, instance=None, created=False, **kwargs):
        if created:
            group = Group.objects.get_or_create(group=instance)

    @receiver(pre_delete, sender=User)
    def delete_group_for_user(sender, instance=None, **kwargs):
        if instance:
            event = Group.objects.get(group=instance)
            event.delete()


class Event(models.Model):
    group = models.OneToOneField(UserGroup, related_name='event')

    @receiver(post_save, sender=Group)
    def create_event_for_group(sender, instance=None, created=False, **kwargs):
        if created:
            group = Event.objects.get_or_create(group=instance)

    @receiver(pre_delete, sender=Group)
    def delete_event_for_group(sender, instance=None, **kwargs):
        if instance:
            event = Event.objects.get(group=instance)
            event.delete()

