from netbox.api.viewsets import NetBoxModelViewSet
from rest_framework.routers import APIRootView


from .. import  models
from .serializers import SnmpCommunitySerializer

# A separate view for the plugin's API root
class SnmpPluginAPIView(APIRootView):
    """
    Plugin API root view
    """
    # This dictionary maps the view name (from urls.py) to a description.
    # It tells the API root what links to display.
    # The key 'snmp-list' should match the name of the URL pattern for your main ModelViewSet router.
    def get_view_name(self):
        return 'Snmp Community'

class SnmpCommunityViewSet(NetBoxModelViewSet):
    queryset = models.SnmpCommunity.objects.prefetch_related('tags').order_by('pk')
    serializer_class = SnmpCommunitySerializer
