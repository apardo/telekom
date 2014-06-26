# -*- coding: utf-8 -*-

from django.db import models

class Subscriber(models.Model):

  class Meta:
    app_label = 'subscribers'
    db_table = 'subscriber'
    managed = False

  username  = models.CharField(max_length=64)
  password  = models.CharField(max_length=25)
  domain    = models.CharField(max_length=64)
  ha1       = models.CharField(max_length=64)
  ha1b      = models.CharField(max_length=64)

  def __unicode__(self):
    return self.username

  # métodos para crear ha1 y ha1b
