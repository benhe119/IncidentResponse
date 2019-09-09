"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import demo.views as views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('slack/', include('response.slack.urls')),
    path('core/', include('response.core.urls')),
    path('', include('response.ui.urls')),
    path('', views.active_incidents, name='active_incidents'),
    path('active', views.active_incidents, name='active_incidents'),
    path('recent', views.recent_incidents, name='recent_incidents'),
]
