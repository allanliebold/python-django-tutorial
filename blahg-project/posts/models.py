# -*- coding: utf-8 -*-
"""Posts models."""
from __future__ import unicode_literals

from django.db import models


class Post(models.Model):
    """Post class model."""

    title = models.CharField(max_length=250)
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to='media/', null=True, blank=True)
    body = models.TextField()

    def pub_date_format(self):
        """Format publication date."""
        return self.pub_date.strftime('%b %e, %Y')

    def summary(self):
        """Shortened version of post body."""
        return self.body[:100]

    def __str__(self):
        """Label Post object with title."""
        return self.title
