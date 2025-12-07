from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm
from .models import SnmpCommunity 
from .filtersets import SnmpCommunityFilterSet  # Import your FilterSet

class SnmpForm(NetBoxModelForm):
    class Meta:
        model = SnmpCommunity
        fields= ('name','community')
class SnmpCommunityFilterForm(NetBoxModelFilterSetForm):
    model = SnmpCommunity
    # Point the form to the FilterSet you defined in filtersets.py
    # (Assuming you named the filterset SnmpCommunityFilterSet)
    from .filtersets import SnmpCommunityFilterSet
    filterset_class = SnmpCommunityFilterSet
