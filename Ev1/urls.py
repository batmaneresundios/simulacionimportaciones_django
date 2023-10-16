from django.contrib import admin
from django.urls import path
from importacionesChina import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('listar/',views.importacionesData,name="listar_importaciones"),
    path('listar/agregarform/', views.agregarImportacion, name='agregar-importacion'),
    path('resultado_parcial/<int:resultado_id>/', views.ver_resultado, name='resultado_parcial'),
    path('listar/resultados_finales/', views.resultados_finales, name='resultados_finales'),
    path('detalle_importacion/<int:imp_id>/', views.detalle_importacion, name='detalle_importacion'),
]
