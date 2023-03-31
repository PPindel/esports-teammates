from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from teamfinder.util import unique_slug_generator
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.conf import settings

STATUS = ((0, "Draft"), (1, "Published"))
User = settings.AUTH_USER_MODEL


class TeamAd(models.Model):
    ROLES = [
        ('ANY', 'Any'),
        ('DMG', 'Damage Dealer'),
        ('SUP', 'Support / Healer'),
        ('DEF', 'Tank / Defender'),
    ]
    SKILL = [
        ('ANY', 'Any'),
        ('NEW', 'New player'),
        ('MID', 'Advanced player'),
        ('EXP', 'Expert player'),
        ('PRO', 'Proffesional player'),
    ]
    GAMES = [
        ('LOL', 'League of Legends'),
        ('WOW', 'World of Warcraft'),
        ('DOTA2', 'Defense of the Ancients 2'),
        ('DIA4', 'Diablo 4'),
        ('POE', 'Path of Exile'),
        ('OW2', 'Overwatch 2'),
        ('SMITE', 'Smite'),
        ('DAD', 'Dark and Darker'),
    ]
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="team_ad")  # noqa E501
    game = models.CharField(max_length=5, choices=GAMES, default='LOL')
    role = models.CharField(max_length=3, choices=ROLES, default='ANY')
    skill_level = models.CharField(max_length=3, choices=SKILL, default='ANY')
    updated_on = models.DateTimeField(auto_now=True)
    description = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('home')


@receiver(pre_save, sender=TeamAd)
def pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


class Comment(models.Model):
    post = models.ForeignKey(TeamAd, on_delete=models.CASCADE, related_name='comments')  # noqa E501
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"

    # def get_absolute_url(self):
    #     return reverse('home')
