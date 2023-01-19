from django.shortcuts import render, redirect
from .models import Registros

# Create your views here.
def home(request):
    registros = Registros.objects.all()
    return render(request,'index.html', {'Registros': registros})

def add_reg(request):
    user_name = request.POST['user_name']
    pet_type = request.POST['pet_type']
    pet_name = request.POST['pet_name']
    vaccine = request.POST['vaccine']
    
    registro = Registros.objects.create(
        user_name = user_name,
        pet_type = pet_type,
        pet_name = pet_name,
        vaccine = vaccine
    )
    return redirect('/')

def delete_reg(request, id):
    registro = Registros.objects.get(id = id)
    registro.delete()
    
    return redirect('/')

def edit_reg(request, id):
    registro = Registros.objects.get(id = id)
    return render(request, 'edit.html', {"registro": registro})

def update_reg(request, id):
  user_name = request.POST['user_name']
  pet_type = request.POST['pet_type']
  pet_name = request.POST['pet_name']
  vaccine = request.POST['vaccine']

  registro = Registros.objects.get(id = id)
  registro.user_name = user_name
  registro.pet_type = pet_type
  registro.pet_name = pet_name
  registro.vaccine = vaccine

  registro.save()
  return redirect('/')