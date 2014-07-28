from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class User(models.Model):

    title = models.CharField(
        max_length=150)
    slug = models.SlugField(
        max_length=75)
    created_at = models.DateField(
        auto_now_add=True)

    def __unicode__(self):
        if self.title:
            return self.title[:50]
        return " #%s" % self.id

    def get_absolute_url(self):
        return reverse('user-detail', args=[str(self.id)])
