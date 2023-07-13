from django.urls import path

from .views import homeview,singlepro_view
urlpatterns=[
    path('',homeview,name='home'),
    path('product/<slug:slug>',singlepro_view,name='single_pro')
]