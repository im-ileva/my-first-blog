from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<pk>/remove/', views.post_remove, name='post_remove'),
    path('catalog/', views.catalog, name='catalog'),
    path('catalog/new/', views.product_new, name='product_new'),
    path('catalog/product/<int:pk>/remove/', views.product_remove, name='product_remove'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)