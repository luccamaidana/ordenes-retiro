from django.shortcuts import render
from .models import OrdenPedido

def crear_orden_pedido(request):
    contexto = {}
    
    if request.method == 'POST':
        # Capturamos los datos enviados por el formulario HTML
        id_solicitante = request.POST.get('id_solicitante', '').strip()
        tipo_servicio = request.POST.get('tipo_servicio', '').strip()
        cantidad_bulto = request.POST.get('cantidad_bulto', '').strip()
        observacion = request.POST.get('observacion', '').strip()
        
        # Validación explícita de datos obligatorios
        if not id_solicitante or not tipo_servicio or not cantidad_bulto:
            contexto['error'] = "Por favor, complete todos los campos obligatorios (Solicitante, Tipo de Servicio y Cantidad)."
            # Mantenemos los datos ingresados para que el usuario no tenga que escribir todo de nuevo
            contexto['datos'] = request.POST 
            return render(request, 'core/formulario.html', contexto)
        
        try:
            # Intentamos convertir la cantidad a entero
            bultos = int(cantidad_bulto)
            if bultos <= 0:  # <-- La regla de negocio aplicada a la vista
                contexto['error'] = "La cantidad de bultos debe ser un número entero mayor a cero."
                contexto['datos'] = request.POST
                return render(request, 'core/formulario.html', contexto)
        except ValueError:
            contexto['error'] = "La cantidad de bultos debe ser un número entero válido."
            contexto['datos'] = request.POST
            return render(request, 'core/formulario.html', contexto)
            
        # Al pasar las validaciones, creamos el registro de forma persistente
        # El campo 'estado' toma automáticamente el default 'PENDIENTE' que configuramos en el modelo
        orden = OrdenPedido.objects.create(
            id_solicitante=id_solicitante,
            tipo_servicio=tipo_servicio,
            cantidad_bulto=bultos,
            observacion=observacion if observacion else None
        )
        
        contexto['exito'] = f"Orden de retiro registrada con éxito."
        return render(request, 'core/formulario.html', contexto)
        
    # Si el método es GET (o cualquier otro), simplemente preparamos la carga vacía
    return render(request, 'core/formulario.html', contexto)