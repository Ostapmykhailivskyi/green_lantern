from django.db import models
from common.models import BaseDateAuditModel
from django.utils.translation import gettext_lazy as _


class NewsLetters(BaseDateAuditModel):
    email = models.EmailField()

    class Meta:
        verbose_name = _('Newsletters')
        verbose_name_plural = _('Newsletters')

    def __str__(self):
        return self.email
