"""project URL Configuration
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
from django.conf import settings
from django.urls import include, path
from core import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name="home"),
    path('accounts/', include('registration.backends.default.urls')),
    path('profile/', views.profile_page, name='profile_page'),
    path('habitlist/', views.list_habit, name='list_habit'),
    path('habitlist/add/', views.add_habit, name='add_habit'),
    path('<int:pk>/edit_habit/', views.edit_habit, name='edit_habit'),
    path('<int:pk>/delete_habit/', views.delete_habit, name='delete_habit'),
    path('habitlist/<int:pk>', views.display_habit, name='display_habit'),
    path('habitlist/<int:pk>/add_record/', views.add_record, name='add_record',)
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
