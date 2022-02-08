"""tmart URL Configuration

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
from django.urls import path , include
from django.conf.urls.static import static
from django.conf import settings

from .views import home
from tmart_Product.views import AllProducts
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('all', AllProducts.as_view()),
    path('', include('tmart_Product.urls')),
    path('', include('tmart_account.urls')),
]

if settings.DEBUG:
    urlpatterns=urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns=urlpatterns +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)