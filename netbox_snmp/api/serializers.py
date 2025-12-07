from rest_framework import serializers

from netbox.api.serializers import NetBoxModelSerializer
from ..models import SnmpCommunity



class SnmpCommunitySerializer(NetBoxModelSerializer):
   # url = serializers.HyperlinkedIdentityField(
   #     view_name='plugins-api:snmp:snmpcommunity-detail'
   # )
    class Meta:
            model = SnmpCommunity
            fields = ( 'id','name', 'community', 'comments','tags','custom_fields','created','last_updated','url','display')
            # Include all fields needed for form submissio:q
            # L:;
