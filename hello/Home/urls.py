from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),#if we click /admin in the link of starter of django i will be render toadmin page
    path('',include('home.urls'))#to render to home page on random link

    
]