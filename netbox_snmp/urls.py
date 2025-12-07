from django.urls import path
from . import models, views
from netbox.views.generic import ObjectChangeLogView

urlpatterns = [
    path('community/',views.SnmpListView.as_view(), name='snmpcommunity_list'),
    path('community/add/',views.SnmpEditView.as_view(), name='snmpcommunity_add'),
    path('community/<int:pk>/',views.SnmpView.as_view(), name='snmpcommunity'),
    path('community/<int:pk>/edit/',views.SnmpEditView.as_view(), name='snmpcommunity_edit'),
    path('community/<int:pk>/delete/',views.SnmpDeleteView.as_view(), name='snmpcommunity_delete'),
    path('community/<int:pk>/changelog/',ObjectChangeLogView.as_view(), name='snmpcommunity_changelog', kwargs={
        'model': models.SnmpCommunity
    }),
]

