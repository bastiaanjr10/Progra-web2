from django.shortcuts import render, redirect
from .models import Usuario, tipoUsuario, Producto, tipoProducto
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def index(request):

    request.session["usuario"]="usuario1"
    usuario=request.session["usuario"]
    context = {'usuario':usuario}
    return render(request, 'alumnos/index.html', context)


def index(request):
    usuarios= Usuario.objects.all()
    context={"user":usuarios}
    return render(request, 'alumnos/index.html', context)


def index(request):
    productos= Producto.objects.all()
    context={"prod":productos}
    return render(request, 'alumnos/index.html', context)

def comprar(request):
    context={}
    return render(request, 'alumnos/comprar.html', context)

def nosotros(request):
    context={}
    return render(request, 'alumnos/nosotros.html', context)

def productos(request):
    context={}
    return render(request, 'alumnos/productos.html', context)

def contacto(request):
    context={}
    return render(request, 'alumnos/contacto.html', context)

def crud(request):
    usuario = Usuario.objects.all()
    context = {"usuario": usuario}
    return render(request, "alumnos/user_list.html", context)

def lista_productos(request):
    productos = Producto.objects.all()
    tipos_producto = tipoProducto.objects.all()
    context = {"productos": productos, "tipos_producto": tipos_producto}
    return render(request, "alumnos/lista_productos.html", context)


#Usuarios

def userAdd(request):
    if request.method != "POST":
        tipo = tipoUsuario.objects.all()
        context = {"tipo": tipo}
        return render(request, "alumnos/user_add.html", context)
    else:
        rut = request.POST["rut"]
        nombre = request.POST["nombre"]
        appPaterno = request.POST["appPaterno"]
        appMaterno = request.POST["appMaterno"]
        fecha = request.POST["fecha"]
        tipo = request.POST["tipoUsuario"]
        correo = request.POST["correo"]
        telefono = request.POST["telefono"]

        objTipo = tipoUsuario.objects.get(idTipoUsuario=tipo)
        objUsuario = Usuario.objects.create(
            rut=rut,
            nombre=nombre,
            appPaterno=appPaterno,
            appMaterno=appMaterno,
            fechaNacimiento=fecha,
            tipoUsuario=objTipo,
            correo=correo,
            telefono=telefono,
            activo=1,
        )
        objUsuario.save()
        context = {"mensaje": "OK Registrado Correctamente"}
        return render(request, "alumnos/user_add.html", context)

def userDel(request, pk):
    context = {}
    try:
        user = Usuario.objects.get(rut=pk)

        user.delete()
        usuarios = Usuario.objects.all()
        context = {"mensaje": "OK Registro eliminado", "usuario": usuarios}
        return render(request, "alumnos/user_list.html", context)
    except:
        usuarios = Usuario.objects.all()
        context = {"mensaje": "Error, Rut no encontrado...", "usuario": usuarios}
        return render(request, "alumnos/user_list.html", context)
    
def userEdit(request, pk):
    if pk != "":
        user = Usuario.objects.get(rut=pk)
        tipo = tipoUsuario.objects.all()
        context = {"usuario": user, "tipo": tipo}
        return render(request, "alumnos/user_edit.html", context)
    else:
        context = {"mensaje": "Error, usuario no encontrado"}
        return render(request, "alumnos/user_list", context)

def userUpdate(request):
    if request.method == "POST":
        rut = request.POST["rut"]
        nombre = request.POST["nombre"]
        appPaterno = request.POST["appPaterno"]
        appMaterno = request.POST["appMaterno"]
        fecha = request.POST["fecha"]
        tipo = request.POST["tipoUsuario"]
        correo = request.POST["correo"]
        telefono = request.POST["telefono"]

        objTipo = tipoUsuario.objects.get(idTipoUsuario=tipo)

        user = Usuario()
        user.rut = rut
        user.nombre = nombre
        user.appPaterno = appPaterno
        user.appMaterno = appMaterno
        user.fechaNacimiento = fecha
        user.tipoUsuario = objTipo
        user.correo = correo
        user.telefono = telefono
        user.activo = 1
        user.save()

        tipo = tipoUsuario.objects.all()
        context = {"mensaje": "OK Registro modificado", "tipo": tipo, "usuario": user}

        return render(request, "alumnos/user_edit.html", context)
    else:
        usuarios = Usuario.objects.all()
        context = {"usuario": usuarios}
        return render(request, "alumnos/user_list.html", context)
    


#Productos

def agregar_producto(request):
    if request.method == 'POST':
        codigo = request.POST['codigo']
        nombre = request.POST['nombre']
        tipoProducto_id = request.POST['tipoProducto']
        tipoProducto_obj = tipoProducto.objects.get(idTipoProducto=tipoProducto_id)
        
        Producto.objects.create(codigo=codigo, nombre=nombre, tipoProducto=tipoProducto_obj)
        return render(request, 'alumnos/agregar_producto.html')
    
    tiposProducto = tipoProducto.objects.all()
    context = {'tiposProducto': tiposProducto}
    return render(request, 'alumnos/agregar_producto.html', context)

def editar_producto(request, codigo):
    if codigo != "":
        producto = Producto.objects.get(codigo=codigo)
        tiposProducto = tipoProducto.objects.all()

        if request.method == 'POST':
            producto.nombre = request.POST['nombre']
            tipoProducto_id = request.POST['tipoProducto']
            tipoProducto_obj = tipoProducto.objects.get(idTipoProducto=tipoProducto_id)
            producto.tipoProducto = tipoProducto_obj
            producto.save()

        context = {"producto": producto, "tiposProducto": tiposProducto}
        return render(request, "alumnos/editar_producto.html", context)
    else:
        return render(request, "alumnos/lista_productos.html")

def eliminar_producto(request, codigo):
    producto = Producto.objects.get(codigo=codigo)
    producto.delete()
    
    tiposProducto = tipoProducto.objects.all()
    productos = Producto.objects.all()
    context = {'productos': productos, 'tiposProducto': tiposProducto}
    return render(request, 'alumnos/lista_productos.html', context)


def crud(request):
    usuario = Usuario.objects.all()
    context = {"usuario": usuario}
    return render(request, "alumnos/user_list.html", context)

@login_required
def index(request):
    request.session["usuario"] = "usuario1"
    usuario = request.session["usuario"]
    context = {'usuario': usuario}
    return render(request, 'alumnos/index.html', context)

def userAdd(request):
    if request.method != "POST":
        tipo = tipoUsuario.objects.all()
        context = {"tipo": tipo}
        return render(request, "alumnos/user_add.html", context)
    else:
        rut = request.POST["rut"]
        nombre = request.POST["nombre"]
        appPaterno = request.POST["appPaterno"]
        appMaterno = request.POST["appMaterno"]
        fechaNacimiento = request.POST["fechaNacimiento"]
        tipoUsuario = request.POST["tipoUsuario"]
        correo = request.POST["correo"]
        telefono = request.POST["telefono"]
        activo = request.POST["activo"]
        usuario = Usuario(rut=rut, nombre=nombre, appPaterno=appPaterno, appMaterno=appMaterno,
                          fechaNacimiento=fechaNacimiento, tipoUsuario_id=tipoUsuario, correo=correo,
                          telefono=telefono, activo=activo)
        usuario.save()
        return redirect('crud')


