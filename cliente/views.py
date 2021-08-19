from django.shortcuts import render, HttpResponse
from . models import Cliente # importando el objeto (modelo) Cliente para que trabaje en agregar


def inicio(request):
    # return HttpResponse("this is the equivalent of @app.route('/')!")
    return render(request, "index.html")

def agregar(request):
    # Estamos capturando lo que está en el formulario, acá en el back-end a través del request, por medio del método POST
    # request.POST['nombre_parametro']
    # Vamos a tomar un objeto o  modelo .objects porque es un objeto
    Cliente.objects.create(
    # asignarlo a una variable
    nombre = request.POST['nombre'],
    apellido = request.POST['apellido'],
    rut = request.POST['rut'],
    dv = request.POST['dv'],
    email = request.POST['email'],
    password = request.POST['password'],
    direccion = request.POST['direccion']
    )
    return render(request, "index.html")


# (request) podria ser utilizado en tod CRUD
def leer(request):
    # primero creamos una variable -> clientes (variable tipo objeto, en este caso una clase)
    # en este caso es de tipo .objects Cliente
    # En Python la variable es definida por su contenido
    # El tipo de variable es definida por el contenido
    clientes = Cliente.objects.all() 
    # lo que hacemos acá es una consulta
    # consulta similar a "select * from cliente"
    # Cuando ejecutamos migrations y migrate ORM hace esto solo
    return render(request, "index.html")



def actualizar(request):
    # metodo actualizar, vamos a recibir por request
    # el campo del cual estamos haciendo referencia es el id
    # porque id es un identificador único, no se repite
    id = request.POST['id']
    # que se hace con ese id, se debe preguntar si existe el registro con ese id
    # Esa consulta se hace con el GET
    cliente = Cliente.objects.get(id=id)
    # se está trayendo solo 1 registro con el id
    # Se debe preguntar si el registro existe o no, la BD va a responder

    # Para continuar, se debe ir a validar los parametros
    # Crear una variable -> puede ser errors
    errors = Cliente.objects.validador_cliente(request.POST)

    if len(cliente) > 0:
        # Si el usuario existe, podemos tomar toda la data y modificarla
        # Porque si no existe se debe enviar mensaje de error
        cliente.nombre = request.POST['nombre']
        cliente.apellido = request.POST['apellido']
        cliente.rut = request.POST['rut']
        cliente.dv = request.POST['dv']
        cliente.email = request.POST['email']
        cliente.password = request.POST['password']
        cliente.direccion = request.POST['direccion']