"""
URL configuration for brahma project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from entities.views import EntityCreateView, IndexView, RegisterView, CommunityListView, \
    UserListView, EntityListView, CommunityCreateView, UserDetailView, \
    CommunityDetailView, ProfileView
from entities.api_views import communities, users


urlpatterns = [
    # path('register/', RegisterView.as_view(), name="register"),
    # path('profile/', ProfileView.as_view(), name="profile"),
    # path('api/communities/', communities, name="api-communities"),
    # path('api/users/', users, name="api-users"),
    # path('communities/', CommunityListView.as_view(), name="communities"),
    # path('communities/<str:slug>', CommunityDetailView.as_view(), name="community"),
    # path('create-community', CommunityCreateView.as_view(), name="create-community"),
    # path('create-other-entity', EntityCreateView.as_view(), name="create-community"),
    # path('users/<int:pk>/', UserDetailView.as_view(), name="user"),
    # path('users/', UserListView.as_view(), name="users"),
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
    path('', IndexView.as_view())
]

urlpatterns += [
    path('user/', include('django.contrib.auth.urls')),
]
