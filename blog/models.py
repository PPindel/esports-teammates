from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from teamfinder.util import unique_slug_generator
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.conf import settings
from django.core.validators import RegexValidator

STATUS = ((0, "Draft"), (1, "Published"))
User = settings.AUTH_USER_MODEL


class TeamAd(models.Model):
    """
    Team Ad class
    Has custom fields and options to choose from
    Contains info about the author and date of creation
    """
    ROLES = [
        ('Any', 'Any'),
        ('Damage Dealer', 'Damage Dealer'),
        ('Support / Healer', 'Support / Healer'),
        ('Tank / Defender', 'Tank / Defender'),
    ]
    SKILL = [
        ('Any', 'Any'),
        ('New player', 'New player'),
        ('Advanced player', 'Advanced player'),
        ('Expert player', 'Expert player'),
        ('Proffessional player', 'Proffessional player'),
    ]
    GAMES = [
        ('League of Legends', 'League of Legends'),
        ('World of Warcraft', 'World of Warcraft'),
        ('Defense of the Ancients 2', 'Defense of the Ancients 2'),
        ('Diablo 4', 'Diablo 4'),
        ('Path of Exile', 'Path of Exile'),
        ('Overwatch 2', 'Overwatch 2'),
        ('Smite', 'Smite'),
        ('Dark and Darker', 'Dark and Darker'),
    ]
    title = models.CharField('title (no special chars)', max_length=200, validators=[RegexValidator(r'^[0-9a-zA-Z ]*$', 'Only alphanumeric characters are allowed.')])  # noqa E501
    slug = models.SlugField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="team_ad")  # noqa E501
    game = models.CharField(max_length=25, choices=GAMES, default='League of Legends')  # noqa E501
    role = models.CharField(max_length=25, choices=ROLES, default='Any')
    skill_level = models.CharField(max_length=25, choices=SKILL, default='Any')
    updated_on = models.DateTimeField(auto_now=True)
    description = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=1)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home')


@receiver(pre_save, sender=TeamAd)
def pre_save_receiver(sender, instance, *args, **kwargs):
    """
    Random slug generator
    """
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


class Comment(models.Model):
    """
    Comment class
    Contains info about the author and date of creation
    """
    post = models.ForeignKey(TeamAd, on_delete=models.CASCADE, related_name='comments')  # noqa E501
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=True)
    id = 0

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
