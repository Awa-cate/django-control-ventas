from django.urls import path
from . import views


urlpatterns = [
    path('', views.all, name='all'),
    path('product/', views.product, name='product'),
    path('product/<int:product_id>/', views.product_detail, name='products_detail'),
    path('product/<int:product_id>/delete/', views.delete_product, name='delete_product'),
    path('sells/', views.sells, name='sells'),
    path('sells/<int:sell_id>/', views.sells_detail, name='sells_detail'),
    path('sells/<int:sell_id>/delete/', views.delete_sell, name='delete_sell'),
    path('forms/', views.forms, name='forms')
]