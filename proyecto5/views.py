from django.shortcuts import render, redirect, get_object_or_404
from .models import Persona
from .forms import PersonaForm
from django.urls import reverse


def lista_personas(request):
    personas=Persona.objects.all()
    return render(request, 'lista_personas.html', {'personas': personas})

def crear_persona(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_personas')
    else:
        form = PersonaForm()
    return render(request, 'crear_persona.html', {'form': form})

def editar(request, dni):
    persona = get_object_or_404(Persona, DNI=dni)
    if request.method == 'POST':
        form = PersonaForm(request.POST, instance=persona)
        if form.is_valid():
            form.save()
            return redirect('lista_personas')
    else:
        form = PersonaForm(instance=persona)
    return render(request, 'editar.html', {'form': form, 'persona': persona})

def eliminar(request, dni):
    persona = get_object_or_404(Persona, DNI=dni)
    if request.method == 'POST':
        persona.delete()
        return redirect('lista_personas')
    return render(request, 'eliminar.html', {'persona':persona})

def inicio (request):
    return render (request, 'inicio.html')
