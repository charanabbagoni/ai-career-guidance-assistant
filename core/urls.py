from django.contrib import admin
from django.urls import path
from guidance import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.dashboard, name='dashboard'),
    path('generate/', views.generate_guidance, name='generate_guidance'),
]