"""ERP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from Product.views import funshowproduct
from Purchase.views import funshowpurchase
from Sales.views import funshowsales
from Stock.views import funshowstock
from Warehouse.views import funshowwarehouse

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^goto_product/',funshowproduct),
    url(r'^goto_purchase/',funshowpurchase),
    url(r'^goto_sales/',funshowsales),
    url(r'^goto_stock/',funshowstock),
    url(r'^goto_warehouse/',funshowwarehouse),
]
