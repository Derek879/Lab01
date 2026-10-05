from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('calculadora.urls')),
    path('', include('tasks.urls')),
]
