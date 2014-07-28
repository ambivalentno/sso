from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext as _

from model_utils import Choices


class User(AbstractUser):
    STATUS = Choices(
        (0, _('user')),
        (1, _('expert')),
        (2, _('moderator')),
        (3, _('admin')),
    )
    status = models.IntegerField(
        choices=STATUS,
        default=STATUS.user,
    )

    created_at = models.DateField(
        auto_now_add=True,
    )
    last_activity = models.DateField(
        auto_now=True,
    )

    def __unicode__(self):
        return "User #%s" % self.id

    def get_absolute_url(self):
        return reverse('user-detail', args=[str(self.id)])
