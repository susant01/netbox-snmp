import django_tables2 as tables

from netbox.tables import NetBoxTable, ChoiceFieldColumn
from .models import SnmpCommunity 

class SnmpTable(NetBoxTable):

    class Meta(NetBoxTable.Meta):
        model = SnmpCommunity
        fields = ('pk', 'id', 'name', 'community', )
        default_columns = ('name', 'community')
