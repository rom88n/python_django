from django.db import models

# Create your models here.

class Articles(models.Model):
    title = models.CharField('Title Article', max_length=50, default='')
    anons = models.CharField('Description', max_length=250)
    full_text = models.TextField('Description')
    date = models.DateTimeField('Date publication')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'