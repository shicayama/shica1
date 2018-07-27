from django.conf.urls import url
from django.urls import path
from . import views

app_name = "timemaker"
urlpatterns = [
    url(r'^index/', views.index_template, name='index_template'),
    url(r'^import/', views.PostImport.as_view(), name='import'),
]
