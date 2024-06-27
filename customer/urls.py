from django.urls import path
from .views import *


app_name = 'customer'
urlpatterns = [
    path('',index , name = 'index'),
    path('about/',about ,name='about'),
    path('persons/',persons, name = 'persons'),
    path('persons/update/<int:id>/', update_person, name='update_person'),
    path('shop/',shop , name = 'shop'),
]
