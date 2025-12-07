from netbox.plugins import PluginMenuItem, PluginMenu

menu_items = (
	PluginMenuItem(
        link='plugins:netbox_snmp:snmpcommunity_list',
        link_text='Community'
    ),

)

menu = PluginMenu(
        label= "SNMP",
        groups = (('SnmpCommunity', menu_items),)
        )
