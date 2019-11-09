from django.db import models


class Link(models.Model):
    full_url = models.URLField(max_length=200)
    short_url = models.CharField(max_length=80, blank=True)

    def _get_unique_url(self):
        num = 1
        new_url = 'shorter/'+str(num)+str('/')
        while Link.objects.filter(short_url=new_url).exists():
            num += 1
            new_url = '{}{}'.format('shorter/', str(num) + str('/'))
        return new_url

    def __str__(self):
        return self.full_url

    def save(self, *args, **kwargs):
        if not self.short_url:
            self.short_url = self._get_unique_url()
        super().save(*args, **kwargs)