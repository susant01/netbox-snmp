from django.contrib import admin
# Import the model you are registering
from .models import SnmpCommunity

class SNMPCommunityAdmin(admin.ModelAdmin):
    # Base fieldsets for all users
    fieldsets_standard = (
        (None, {'fields': ('name')}),
    )
    
    # Fieldsets including the sensitive field
    fieldsets_sensitive = (
        (None, {'fields': ('name', 'community')}),
    )

    def get_fieldsets(self, request, obj=None):
        # Check if the user has the required permission
        if request.user.has_perm('snmp.view_encrypted_data'):
            return self.fieldsets_sensitive
        return self.fieldsets_standard

admin.site.register(SnmpCommunity, SNMPCommunityAdmin)
