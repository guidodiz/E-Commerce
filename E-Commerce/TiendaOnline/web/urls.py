from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('productos/', views.productos, name='productos'),
    path('novedades/', views.novedades, name='novedades'),
    path('producto/<int:id>', views.vista_producto, name='vista_producto'),
    path('compra/', views.compra, name='compra')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)