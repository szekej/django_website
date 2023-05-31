from django.db import models
from django.utils.text import slugify
import misaka
from django.contrib.auth import get_user_model
from django import template

# Create your models here.

User = get_user_model()
register = template.Library()


class Group(models.Model):
    name = models.CharField(max_length=255, unique=True, on_delete=models.CASCADE)
    slug = models.SlugField(allow_unicode=True, unique=True, on_delete=models.CASCADE)
    description = models.TextField(blank=True, default='', on_delete=models.CASCADE)
    description_html = models.TextField(blank=True, default='', editable=False, on_delete=models.CASCADE)
    members = models.ManyToManyField(User, through='GroupMember')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.description_html = misaka.html(self.description)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('groups:single', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['name']


class GroupMember(models.Model):
    group = models.ForeignKey(Group, related_name='membership', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='user_groups', on_delete=models.CASCADE)

    def __str__(self):
        return self.username

    class Meta:
        unique_together = ('group', 'user')