from django.http import Http404
from django.shortcuts import render

# Cada operación: (símbolo, nombre que se muestra, función)
OPERACIONES = {
    'sumar': ('+', 'suma', lambda a, b: a + b),
    'restar': ('-', 'resta', lambda a, b: a - b),
    'multiplicar': ('x', 'multiplicación', lambda a, b: a * b),
}


def operar(request, operacion, a, b):
    if operacion not in OPERACIONES:
        raise Http404('Operación no válida')
    simbolo, nombre, funcion = OPERACIONES[operacion]
    contexto = {
        'nombre': nombre,
        'a': a,
        'b': b,
        'simbolo': simbolo,
        'resultado': funcion(a, b),
    }
    return render(request, 'calculadora/resultado.html', contexto)
