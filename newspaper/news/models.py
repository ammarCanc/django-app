"""
Models for news application
"""
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """ The model to store user information """
    name = models.CharField(max_length=50, blank=True)
    joining_date = models.DateField(null=True)
    ROLE_CHOICES = (
        (0, 'Visitor'),
        (1, 'Reporter'),
        (2, 'Moderator'),
    )
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, default=0)


class NewsMedium(models.Model):
    """ This model contain fields required in Blog, Article and News """
    title = models.CharField(max_length=200)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_published = models.DateField()
    approved_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='approver')

    def __str__(self):
        return self.title


class Article(NewsMedium):
    """ This model stores Article fileds other than in NewsMedium """
    image = models.ImageField(upload_to='images', null=True)


class Blog(NewsMedium):
    """ This model stores Blog fileds other than in NewsMedium """
    image = models.ImageField(upload_to='images', null=True)


class NewsBulletin(NewsMedium):
    """ This model stores News fileds other than NewsMedium """
    pass
