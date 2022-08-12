"""Journey_Wishing_Bottle URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include, re_path

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views
from trips.views import attraction, accomodation, restaurant, post_detail, post_new, post_delete, post_edit, register, area, like_post, post_serialized_view, post_new_comment


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('Like',like_post,name='like_post'),
    path('serialized/', post_serialized_view, name='serialized_view'),
    path('area/', area, name="area"),
    path('attraction/', attraction, name='attraction'),
    path('accomodation/', accomodation, name='accomodation'),
    path('restaurant/', restaurant, name='restaurant'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', register, name='register'),
    re_path(r'^post/post_new_comment/(?P<post_id>[0-9]+)/$', post_new_comment, name='post_new_comment'),
    re_path(r'^post/(?P<pk>\d+)/$', post_detail, name="post_detail"),
    re_path(r'^post/new/$', post_new, name='post_new'),
    re_path(r'^post/(?P<pk>[0-9]+)/delete/$', post_delete, name='post_delete'),
    re_path(r'^post/(?P<pk>[0-9]+)/edit/$', post_edit, name='post_edit'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
