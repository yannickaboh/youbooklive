from django.urls import path, include
from django.contrib import admin
from . import views

app_name = 'travelapp'

urlpatterns = [

    # Administration
    path('admin/', admin.site.urls),



]