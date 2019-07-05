from django.conf.urls import url
from front_panel import views

app_name = 'front_panel'

urlpatterns = [
    url(r'^$', views.login),
    url(r'^registration/$', views.registration, name="register")
]