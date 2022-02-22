
from django.contrib import admin
from django.urls import path

admin.site.site_header = "Организация Нур Транс"
admin.site.site_title = "Нур Транс"
admin.site.index_title = "Панель администратора Нур Транс"



urlpatterns = [
    path('', admin.site.urls),
   
]
