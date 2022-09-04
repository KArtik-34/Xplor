from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('creator/', admin.site.urls),
    
    path(" ",include('ProjectX.urls')),
    path("xplor/",include('ProjectX.urls'))


]
