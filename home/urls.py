from django.contrib import admin
from django.urls import path
from home import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('send_mail/', views.mail, name='mail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)