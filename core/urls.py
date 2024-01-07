from django.urls import path
from .views import *


urlpatterns = [
    path("execute-command/", execute_command, name="execute_command"),
    path("", home, name="home"),
]
