from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name="home"),
    path("clubs", views.clubs, name="clubs"),
    path("about", views.about, name="about"),
    path("services", views.services, name="services"),
    path("contact", views.contact, name="contact"),
    path("delhi/", views.delhi, name="delhi"),
    path("noida/", views.noida, name="noida"),
    path("gurugram/", views.gurugram, name="gurugram"),
]
