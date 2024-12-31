from django.shortcuts import render, get_object_or_404, redirect
from .models import Evento, Categoria
from .forms import EventoForm, CategoriaForm

# Create your views here.
#listar eventos
def lista_eventos(request):
    eventos = Evento.objects.all()
    return render (request, 'eventos/lista_eventos.html', {'eventos': eventos})

#crear o editar eventos
def gestionar_evento(request, id=None):
    if id:
        evento = get_object_or_404(Evento, id =id)
    else:
        evento = Evento()

    if request.method == 'POST':
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            return redirect('lista_eventos')  
    else:
        form = EventoForm(instance=evento)

    return render (request,'eventos/gestionar_evento.html', {'form': form} )  

#eliminar un evento

def eliminar_evento(request, id):
    evento = get_object_or_404(Evento, id = id)
    evento.delete()
    return redirect ('lista_eventos')
        


#Para categoria

def lista_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'eventos/lista_categorias.html', {'categorias': categorias})


def nueva_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_categorias')
    else:
        form = CategoriaForm()
    return render(request, 'eventos/form_categoria.html', {'form': form})

def editar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('lista_categorias')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'eventos/form_categoria.html', {'form': form, 'categoria': categoria})

def eliminar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    if request.method == 'POST':
        categoria.delete()
        return redirect('lista_categorias')
    return render(request, 'eventos/eliminar_categoria.html', {'categoria': categoria})