from django.urls import path, register_converter
from . import views


class EnteroConSigno:
    """Acepta enteros positivos y negativos en la URL (ej. -5)."""
    regex = '-?[0-9]+'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return str(value)


register_converter(EnteroConSigno, 'entero')

urlpatterns = [
    path('<str:operacion>/<entero:a>/<entero:b>', views.operar, name='operar'),
]
