from django.db import models

# Create your models here.

class Item(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    last_update = models.DateField()

    def __unicode__ (self):
        return self.title


    def lines (self):
        return self.content.count('\n') + 2


    class Meta:
        ordering = ["-last_update"]

