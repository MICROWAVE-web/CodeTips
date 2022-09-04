import random
import string

from django.db import models

from authentication.models import User


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    icon = models.ImageField(upload_to='static/tags_icons/', null=True, blank=True)

    def __str__(self):
        return self.name


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


class Tip(models.Model):
    heading = models.CharField(max_length=200, blank=False)
    description = models.TextField(max_length=600, blank=False)
    code = models.TextField(max_length=2000, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)
    tags = models.ManyToManyField(Tag, related_name='tip_tags', blank=True)
    rating = models.IntegerField(blank=False, default=0)
    url_hash = models.CharField(max_length=6, null=True, blank=True, unique=True)

    def save(self):
        if not self.url_hash:
            self.url_hash = id_generator()
            while Tip.objects.filter(url_hash=self.url_hash).exists():
                self.url_hash = id_generator()
        super(Tip, self).save()

    def __str__(self):
        return self.heading

    class Meta:
        ordering = ["date_modified"]



