from django.db import models
from django.db.models.base import Model
import re

# Acá creamos en modelo con los campos que queremos
# Acá se crean los campos que va a tener la tabla en una base de datos (sqlite en este caso)

class ClienteManager(models.Manager):
    # .Manager para hacer lógica de negocios
    # Aquí vamos a crear todas las funciones, métodos que ayudan a validar los parametros
    # Conviene hacer la validación acá que en el controlador (views)
    def validador_cliente(self, data):
        # Self hace referencia al mismo objeto o a la misma función
        # lo que estamos haciendo es agregar dentro del modelo de cliente, se crea una clase
        # para crear metodos y hacer todo tipo de validaciones
        # Es recomendable crear una varible que se llame errores (un arreglo, objeto -> para pasar un diccionario con todos los errores posibles)
        errores = {} # Diccionario de errores
        # Creamos esta variable que le agregamos la key y la data
        # Tomamos la variable y se la pasamoa a front-end
        # Y si variable es > 0, mostrar cuales son los errores
        if len(data['nombre']) == 0:
            errores['nombre'] = 'Ingrese un nombre'
        if len(data['apellido']) == 0:
            errores['apellido'] = 'Ingrese un apellido'
        if len(data['rut']) == 0:
            errores['rut'] = 'Ingrese un rut'
        if len(data['dv']) == 0:
            errores['dv'] = 'Ingrese un dv'
        # Esto es una expresión regular, para validar datos ingresados
        EMAIL = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL.match(data['email']):
            errores['email'] = "email invalido"
        if len(data['direccion']) == 0:
            errores['direccion'] = 'Ingrese una direccion'
        return errores




# Se crea una clase
class Cliente(models.Model):
    # .Model de tipo modelo porque cuando se generan las migraciones, crean las tablas
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    rut = models.CharField(max_length=12)
    dv = models.CharField(max_length=1)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # Vamos a Crear una clase Manager
    # Nos va a permitir trabajar con las validaciones para el objeto
    objects = ClienteManager()