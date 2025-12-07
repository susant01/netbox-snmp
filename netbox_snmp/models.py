from django.contrib.postgres.fields import ArrayField
from django.db import models
from netbox.models import NetBoxModel
from django_cryptography.fields import encrypt
from django.urls import reverse



class SnmpCommunity(NetBoxModel):
    name = models.CharField(max_length=100)
    community = encrypt(models.CharField(max_length=255))
    comments = models.TextField(
        blank=True
    )
    
    class Meta:
        permissions = [
                ("view_encrypted_data", "Can view encrypted community fields.")
                ]

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('plugins:netbox-snmp:snmpcommunity', args=[self.pk])

