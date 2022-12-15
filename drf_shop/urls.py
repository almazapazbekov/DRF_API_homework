"""drf_shop URL Configuration

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
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from shop import views

router = DefaultRouter()
router.register('product', views.ProductViewSet, basename='product')
# router.register('category', views.CategoryApiView, basename='category')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('category/', views.CategoryApiView.as_view(), name='category'),
    path('category/<int:id>', views.CategoryDetailAPIView.as_view(), name='category_detail'),
    path('firm/', views.firm_view, name='firm'),
    path('firm/<int:id>', views.firm_detail, name='firm_detail'),

]
