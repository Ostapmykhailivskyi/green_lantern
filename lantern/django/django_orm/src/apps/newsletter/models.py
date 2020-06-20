from django.db import models


class NewsLetter(models.Model):
    NewsLetterID = models.AutoField(primary_key=True)
    Email = models.EmailField(max_length=70, blank=True)

    class Meta:
        verbose_name = ('Newsletter')
        verbose_name_plural = ('Newsletters')
