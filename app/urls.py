from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import render
from django.urls import path
from dsuplementos.views import ListaProdutoView, DetalheProdutoView, checkout


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ListaProdutoView.as_view(), name='lista_produto'),
    path('produto/<int:pk>/', DetalheProdutoView.as_view(), name='detalhe_produto'),
    path('checkout/<int:produto_id>/', checkout, name='checkout'),
    path('success/', lambda request: render(request, 'success.html'), name='success'),
    path('cancel/', lambda request: render(request, 'cancel.html'), name='cancel'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)