from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile
import logging

logger = logging.getLogger(__name__)

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        logger.info('Creating profile instance for user %s', instance.username)
        Profile.objects.create(user=instance)
        logger.info('Profile instance created successfully')
@receiver(post_save, sender=User)
def create_profile(sender, instance, **kwargs):
    instance.profile.save()


# new modified code




