from netbox.api.routers import NetBoxRouter


from . import views
router = NetBoxRouter()
router.APIRootView = views.SnmpPluginAPIView

router.register('snmp-communities', views.SnmpCommunityViewSet,basename='snmpcommunity')

urlpatterns = router.urls


