from django.shortcuts import render, redirect
from .models import Decade, Fad
from .forms import DecadeForm, FadForm

def decade_list(request):
    decades = Decade.objects.all()
    return render(request, 'decade_list.html', {'decades': decades})

def decade_detail(request, id):
    decade = Decade.objects.get(id = id)
    return render(request, 'decade_detail.html', {'decade': decade})

def decade_create(request):
    if request.method == 'POST':
        form = DecadeForm(request.POST)
        if form.is_valid:
            decade = form.save()
            return redirect('decade_detail', id = decade.id)
    else:
        form = DecadeForm()
        return render(request, 'decade_form.html', {'form': form})

def decade_update(request, id):
    decade = Decade.objects.get(id = id)
    if request.method == 'POST':
        form = DecadeForm(request.POST, instance = decade)
        if form.is_valid:
            decade = form.save()
            return redirect('decade_detail', id = decade.id)
    else:
        form = DecadeForm(instance = decade)
        return render(request, 'decade_form.html', {'form': form})

def decade_delete(request, id):
    if request.method == 'POST':
        Decade.objects.get(id = id).delete()
    return redirect('decade_list')

def fad_list(request):
    fads = Fad.objects.all()
    return render(request, 'fad_list.html', {'fads': fads})

def fad_detail(request, id):
    fad = Fad.objects.get(id = id)
    return render(request, 'fad_detail.html', {'fad': fad})

def fad_create(request):
    if request.method == 'POST':
        form = FadForm(request.POST)
        if form.is_valid:
            fad = form.save()
            return redirect('fad_detail', id = fad.id)
    else:
        form = FadForm()
        return render(request, 'fad_form.html', {'form': form})

def fad_update(request, id):
    fad = Fad.objects.get(id = id)
    if request.method == 'POST':
        form = FadForm(request.POST, instance = fad)
        if form.is_valid:
            fad = form.save()
            return redirect('fad_detail', id = fad.id)
    else:
        form = FadForm(instance = fad)
        return render(request, 'fad_form.html', {'form': form})

def fad_delete(request, id):
    if request.method == 'POST':
        Fad.objects.get(id = id).delete()
    return redirect('fad_list')
