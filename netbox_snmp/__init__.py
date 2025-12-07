try:
    from netbox.plugins import PluginConfig
except ImportError:
    # Fallback for old NetBox versions < 4.0
    from extras.plugins import PluginConfig

# Placeholder for semantic release
__VERSION__ = "0.0.0"


class SNMP(PluginConfig):
    name = "netbox_snmp"
    verbose_name = "Netbox SNMP community"
    description = (
		"Add snmp community in device"
    )
    version = __VERSION__
    author = "Susant Shrestha"
    author_email = "susant.shrestha01@gmail.com"
    base_url = "netbox_snmp"
    required_settings = []
    default_settings = {}
    api_url_config = "netbodx_snmp.api.urls"
# Add this method to ensure models are registered
    def ready(self):
        super().ready()
        from netbox.models.features import register_models
        # This registers all models defined within your plugin
        register_models(*self.get_models())
    #api_url = 'api/snmp'
    #api_config = {
    #        'url_prefix': 'snmp'
    #        }


config = SNMP
