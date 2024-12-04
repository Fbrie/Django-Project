"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

# Import views from the Weatherapp
from Weatherapp import views

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin URL
    path('', include("Weatherapp.urls")),  # Include the Weatherapp URLs (handle routes from Weatherapp/urls.py)
    path('', views.index, name='index'),  # Root path for the Weatherapp
    path('register/', views.register, name='register'),  # Registration URL
    path('members/', views.members_list, name='members_list'),  # Members list URL
    path('test/', views.test_view, name='test'),  # Test template URL
    path('user/<int:user_id>/', views.user_detail, name='user_detail'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Serve media files in development
