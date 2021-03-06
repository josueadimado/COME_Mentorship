"""COME_Mentorship URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import url, include
from django.urls import re_path
from django.views.static import serve 
from django.conf import settings
api_version = "api/"+settings.API_VERSION

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^', include("accounts.urls")),
    url(r'^{}',include('courses.urls')),
    url(r'^{}/courses/'.format(api_version),include('courses.urls')),
]
# This is not right for a production server but ah well.
urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    }),
]
