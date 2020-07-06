# frontend/views.py

from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView

from meds.models import Med
from .forms import  UserForm
from .forms import  MedForm
from .filters import MedFilter
from django.core.serializers import serialize
import json

def index(request):
    med_list = Med.objects.all()
    
    medForm = MedForm()
    if request.method == "POST":
        medForm = MedForm(request.POST)
        if medForm.is_valid():
            medForm.save()
            return redirect('/#services')
    # med_filter = MedFilter(request.GET, queryset=med_list)
    # context = {'filter': med_filter}
    userForm = UserForm()
    context = {'userForm': userForm}
    if request.method == "POST":
        userForm = UserForm(request.POST)
        if userForm.is_valid():
            userForm.save()
            return redirect('/')

    med_list_json= json.loads(serialize('json', med_list))

    context = {'med_list': med_list, 'medForm': medForm, 'med_list_json': med_list_json, 'userForm':userForm}
    # context = {'meds': meds, 'form': form, 'med_filter': med_filter}
    return render(request, 'frontend/index.html', context)

def deleteMed(request, pk):
    med = Med.objects.get(id=pk)
    if med.delete():
        return redirect('/#services')
        # return render(request, 'frontend/index.html')
    context = {'med': med}
    return render(request, 'frontend/delete.html', context)

def predict(request):
    return render(request, 'frontend/predict.html')

def customPrediction(request):
    form = UserForm()
    context = {'form': form}
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'frontend/custom_prediction.html', context)

class MedDetailView(DetailView):
    model = Med
    template_name = 'frontend/index.html'