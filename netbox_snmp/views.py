from netbox.views import generic
from .filtersets import SnmpProfileFilterSet # <-- Import the new FilterSet
from . import forms, models, tables
from .api.serializers import SnmpCommunitySerializer 

class SnmpView(generic.ObjectView):
    queryset= models.SnmpCommunity.objects.all()


class SnmpListView(generic.ObjectListView):
    queryset= models.SnmpCommunity.objects.all()
    filterset = SnmpProfileFilterSet
    table = tables.SnmpTable

class SnmpEditView(generic.ObjectEditView):
    queryset= models.SnmpCommunity.objects.all()
    form = forms.SnmpForm
    serializers_class =  SnmpCommunitySerializer

class SnmpDeleteView(generic.ObjectDeleteView):
    queryset= models.SnmpCommunity.objects.all()
