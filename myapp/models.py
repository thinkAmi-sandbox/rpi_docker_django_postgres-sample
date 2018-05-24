from django.db import models

class Foo(models.Model):
    name = models.CharField(verbose_name='名前', max_length=255)
