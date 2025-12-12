from django.shortcuts import render

from blog.models import Autor, Categoria, Post
from blog.forms import AutorFormulario, CategoriaFormulario, PostFormulario, BusquedaFormulario

def inicio(request):
    return render(request, 'blog/inicio.html')

def crear_autor(request):
    if request.method == 'POST':
        mi_formulario = AutorFormulario(request.POST)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            nuevo_autor = Autor(nombre=data['nombre'], apellido=data['apellido'], email=data['email'], profesion=data['profesion'])
            nuevo_autor.save()
            return render(request, 'blog/inicio.html', {'mensaje': 'Autor creado con éxito'})
    else:
        mi_formulario = AutorFormulario()
    return render(request, 'blog/crear_autor.html', {'mi_formulario': mi_formulario})

def crear_categoria(request):
    if request.method == 'POST':
        mi_formulario = CategoriaFormulario(request.POST)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            nueva_cat = Categoria(nombre=data['nombre'])
            nueva_cat.save()
            return render(request, 'blog/inicio.html', {'mensaje': 'Categoría creada con éxito'})
    else:
        mi_formulario = CategoriaFormulario()
    return render(request, 'blog/crear_categoria.html', {'mi_formulario': mi_formulario})

def crear_post(request):
    if request.method == 'POST':
        mi_formulario = PostFormulario(request.POST)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            nuevo_post = Post(titulo=data['titulo'], contenido=data['contenido'], fecha_publicacion=data['fecha_publicacion'])
            nuevo_post.save()
            return render(request, 'blog/inicio.html', {'mensaje': 'Post creado con éxito'})
    else:
        mi_formulario = PostFormulario()
    return render(request, 'blog/crear_post.html', {'mi_formulario': mi_formulario})

def buscar_autor(request):
    if request.method == "POST":
        mi_formulario = BusquedaFormulario(request.POST) 
        if mi_formulario.is_valid():
            info = mi_formulario.cleaned_data
            autores = Autor.objects.filter(nombre__icontains=info["termino"])
            return render(request, "blog/resultado_busqueda.html", {"autores": autores})
    else:
        mi_formulario = BusquedaFormulario()
    return render(request, "blog/buscar_autor.html", {"mi_formulario": mi_formulario})
