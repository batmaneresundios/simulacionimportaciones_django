from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Importacion, Resultado

# Esta vista recupera todas las importaciones y sus resultados relacionados.
def importacionesData(request):
    importaciones = Importacion.objects.all()
    data = {'importaciones': importaciones}
    
    for imp in importaciones:
        # Obtén los resultados relacionados con cada importación
        resultados = Resultado.objects.filter(importacion=imp)
        
        if resultados:
            resultado = resultados[0]  # Suponemos que solo hay un resultado por importación
            imp.resultado = resultado
        else:
            pass
    return render(request, 'listar-importaciones.html', data)


# POS.get : está tomando el valor del campo "codigo_articulo" de un formulario enviado por POST, y luego lo convierte en un número entero.
def agregarImportacion(request):
    if request.method == "POST":
        # Obtener los datos del formulario
        nombre_articulo = request.POST.get("nombre_articulo")
        cantidad_unidades = int(request.POST.get("cantidad_unidades"))
        costo_unitario = int(request.POST.get("costo_unitario"))
        codigo_articulo = int(request.POST.get("codigo_articulo"))
        proveedor = request.POST.get("proveedor")
        costo_envio = request.POST.get("costo_envio")

        # Se crea una nueva instancia de Importacion
        importacion = Importacion(
            nombre_articulo=nombre_articulo,
            cantidad_unidades=cantidad_unidades,
            costo_unitario=costo_unitario,
            codigo_articulo=codigo_articulo,
            proveedor=proveedor,
            costo_envio=costo_envio,
        )
         # Se guarda la instancia en la base de datos.
        importacion.save()  # Guardar la instancia de Importacion en la base de datos

        total_pedido = cantidad_unidades * costo_unitario
        resultado = calcular_impuestos_y_resultado(total_pedido, costo_envio)
        resultado.importacion = importacion # Se vincula el resultado con la importación.
        resultado.save()  # Guardar la instancia de Resultado en la base de datos
        # Se Redirige al usuario a la página de resultados
        return redirect('resultado_parcial',resultado_id=resultado.id)
    return render(request, 'agregar-importacion.html')


def resultados_finales(request):
    resultados = Resultado.objects.all()
    # Tu lógica para mostrar los resultados
    context = {
        'resultados': resultados,
    }
    return render(request, 'resultados-finales.html', context)

def calcular_impuestos_y_resultado(total_pedido, costo_envio):
    try:
        total_pedido = int(total_pedido)  
        costo_envio = int(costo_envio) * 890
    except (ValueError, TypeError):
        return None  # O manejar el error de otra forma
    total_pedido = total_pedido * 890
    valor_cif = total_pedido + costo_envio
    tasa_aduana = valor_cif * 0.06
    iva = valor_cif * 0.19
    total_impuestos = tasa_aduana + iva
    total_compra_clp = valor_cif + total_impuestos
    total_compra_usd = total_compra_clp / 890

    resultado = Resultado(
        total_pedido=total_pedido,
        costo_envio=costo_envio,
        tasa_aduana=tasa_aduana,
        iva=iva,
        total_impuestos=total_impuestos,
        total_compra_clp=total_compra_clp,
        total_compra_usd=total_compra_usd,
    )
    return resultado


def guardar_resultado(request):
    if request.method == "POST":
        # Obtener los datos del formulario
        nombre_articulo = request.POST.get("nombre_articulo")
        cantidad_unidades = int(request.POST.get("cantidad_unidades"))
        costo_unitario = int(request.POST.get("costo_unitario"))
        codigo_articulo = int(request.POST.get("codigo_articulo"))
        proveedor = request.POST.get("proveedor")
        costo_envio = request.POST.get("costo_envio")      
        # Calcular impuestos y resultados
        total_pedido = cantidad_unidades * costo_unitario
        resultado = calcular_impuestos_y_resultado(total_pedido, costo_envio)


def ver_resultado(request, resultado_id):
    resultado = Resultado.objects.get(id=resultado_id)
    importacion = resultado.importacion
    context = {'resultado': resultado,
               'importacion':importacion
               }
    return render(request, 'resultado-parcial.html', context)
    
    

def detalle_importacion(request, imp_id):
    importacion = get_object_or_404(Importacion, id=imp_id)
    
    # Como es una relación OneToOne, si la importación no tiene un resultado asociado,se lanzará una excepción. 
    try:
        resultado = importacion.resultado
    except Resultado.DoesNotExist:
        resultado = None

    context = {
        'importacion': importacion,
        'resultado': resultado
    }
    return render(request, 'resultado-parcial.html', context)