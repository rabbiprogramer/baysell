from django.urls import path
from .views import *
app_name = 'admin_panel'

urlpatterns = [
    path('admin-panel/admin-list/',admin_list, name='admin_list')
]
