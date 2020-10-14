from django.urls import path
from . import views

urlpatterns=[
path('html_form/',views.html_form, name='html_form'),
path('save_data/',views.save_data, name='save_data'),
path('cancel_data/',views.cancel_data, name='cancel_data')


]