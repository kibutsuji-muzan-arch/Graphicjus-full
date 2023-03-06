from django.db import models
from django.utils.translation import gettext_lazy as _
from uuid import uuid4

class Services(models.Model):
    name = models.CharField(_('Name'), max_length=20, unique=True)
    def __str__(self):
        return self.name

class Contact(models.Model):
    uuid = models.UUIDField(default=uuid4, primary_key=True, unique=True)
    name = models.CharField(_('Name'), max_length=20)
    email = models.EmailField(_('Email'), max_length=200, unique=False)
    service = models.ManyToManyField(Services, related_name='Services', verbose_name=_('Services'))
    contacted = models.BooleanField(_('Contacted'), default=False)
    
    def __str__(self):
        return str(self.uuid)