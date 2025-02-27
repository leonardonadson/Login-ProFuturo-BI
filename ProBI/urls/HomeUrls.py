from django.urls import path
from ProBI.views.HomeView import home_view
urlpatterns = [
path("", home_view),
]