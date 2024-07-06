"""
URL configuration for trydjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path

# from pages import views # using this would affect how we import views fro mother apps so do like this:
from pages.views import home_view, contact_view
from products.views import product_detail_view, product_create_view, product_create_view_raw

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.home_view, name='home'),
    path('', home_view, name='home'),
    path('contact/', contact_view),
    path('product/', product_detail_view),
    path('create/', product_create_view),
    path('create_raw/', product_create_view_raw)

]
