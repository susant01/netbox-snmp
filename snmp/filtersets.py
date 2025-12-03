# your_plugin_name/filtersets.py

import django_filters
from netbox.filtersets import NetBoxModelFilterSet
from .models import SnmpCommunity  # Import your custom model

class SnmpProfileFilterSet(NetBoxModelFilterSet):
    # Example 1: Basic text search on the 'name' field
    # Allows for partial matching (icontains)
    name = django_filters.CharFilter(
        lookup_expr='icontains',
        label='SNMP Profile Name',
    )
    
    # Example 2: Filtering by a related field (e.g., a community string)
    # Assuming your SnmpProfile model has a ForeignKey to a SnmpCommunity model
    # community__name = django_filters.CharFilter(
    #     lookup_expr='icontains',
    #     field_name='community__name',
    #     label='Community String',
    # )

    class Meta:
        model = SnmpCommunity
        # List all fields you want to be able to filter on
        fields = ('id', 'name')

class SnmpCommunityFilterSet(NetBoxModelFilterSet):
    # Add any specific filters you need here, e.g.:
    # name = django_filters.CharFilter(lookup_expr='icontains')
    
    class Meta:
        model = SnmpCommunity
        # List all fields you want to be able to filter on
        fields = ('id', 'name')
