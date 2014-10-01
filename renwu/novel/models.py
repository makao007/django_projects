from django.db import models



class category (models.Model):
    name = models.CharField(max_length=200)
    order = models.IntegerField()

    def __unicode__ (self):
        return '%s' % self.name

    class Meta :
        ordering = ['order']


class tag (models.Model):
    name = models.CharField(max_length=200)

    def __unicode__ (self):
        return '%s' % self.name

class novel (models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey (category)
    tag = models.ForeignKey (tag)

    content = models.TextField ()

    def __unicode__(self):
        return self.title

