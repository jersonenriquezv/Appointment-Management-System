from django.shortcuts import render
from .models import Patient
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import PatientForm

def index(request):
    return render(request, 'patients/index.html', {
        'patients': Patient.objects.all()

    })

def view_patient(request, id):
    patient = Patient.objects.get(pk=id)
    return HttpResponseRedirect(reverse['index'])

def add(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            new_patient = form.save()  # This saves the form and creates a new patient
            return render(request, 'patients/add.html', {
                'form': PatientForm(),
                'success': True
            })
    else:
        form = PatientForm()  # Initialize an empty form for a GET request

    # If the request is not POST or the form is not valid, show the empty or invalid form
    return render(request, 'patients/add.html', {
        'form': form
    })

def edit(request, id):
    if request.method == 'POST':
        patient = Patient.objects.get(pk=id)
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return render(request, 'patients/edit.html', {
                'form': form,
                'success': True
            })
    else:
        patient = Patient.objects.get(pk=id)
        form = PatientForm(instance=patient)
    return render(request, 'patients/edit.html', {
        'form': form
    })


def delete(request, id):
    if request.method == 'POST':
        patient = Patient.objects.get(pk=id)
        patient.delete()
    return HttpResponseRedirect(reverse('index'))

    