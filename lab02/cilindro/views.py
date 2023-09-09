from django.shortcuts import render

def formulario_cili(request):
    context = {
        'titulo': "CÁLCULO DEL VOLUMEN DE UN CILINDRO",
    }
    return render(request, 'cilindro/formulario_cili.html', context)
def calcular(request):
    if request.method == 'POST':
        diametro = float(request.POST['diametro'])
        altura = float(request.POST['altura'])
        radio = diametro / 2
        volumen = 3.1416 * radio ** 2 * altura
        return render(request, 'cilindro/resultado_cili.html', {'volumen': volumen})
    else:
        return render(request, 'cilindro/formulario_cili.html')