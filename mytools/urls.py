"""mytools URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
#from cdp import views
from cdp.views import home_view, product_create_view2, cdp_view, cdp_view2, phone_inter_reset

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('contact/', contact_view, name='contact'),
    #path('my_form/', product_create_view, name='form'),
    path('my_form2/', product_create_view2, name='my_form2'),
    path('phone_reset', phone_inter_reset, name = 'phone_inter_reset'),
    path('cdp/', cdp_view, name='cdp'),
    path('cdp2/', cdp_view2, name='cdphtml'),
    #path('', home_view, name='home'),
    path('', cdp_view2, name='cdphtml')
]
