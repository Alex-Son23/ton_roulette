from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', admin.site.urls),
]

admin.site.site_header = "Администрирование бота"
admin.site.site_title = "Проект"
admin.site.index_title = ""
