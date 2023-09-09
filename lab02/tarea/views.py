from django.shortcuts import render

def formulario_ope(request):
    context = {
        'titulo': "Formulario de Operaciones",
    }
    return render(request, 'tarea/formulario_ope.html', context)

def calcular(request):
    if request.method == 'POST':
        numero1 = request.POST['numero1']
        numero2 = request.POST['numero2']
        operacion = request.POST['operacion']
        calcular = 0
        if operacion == 'suma':
            calcular = int(numero1) + int(numero2)
        elif operacion == 'resta':
            calcular = int(numero1) - int(numero2)
        elif operacion == 'multiplicacion':
            calcular = int(numero1) * int(numero2)
        elif operacion == 'division':
            calcular = int(numero1) / int(numero2)
    return render(request, 'tarea/resultado_ope.html', {'calcular': calcular})