import time
from django.db import models


class Entry(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    data = models.TextField()

    class Meta:
        verbose_name_plural = 'Entries'

    def __unicode__(self):
        return self.created_on.strftime('%d/%m/%Y %H:%M:%S')

    def get_utc_created_on(self):
        return int(time.mktime(self.created_on.timetuple()) * 1000)
