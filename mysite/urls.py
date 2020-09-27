from django.contrib import admin
from django.urls import path
from . import HomePage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , HomePage.homepage , name = 'homepage'),
    path('analyze' , HomePage.analyze , name = 'analyze')
]
