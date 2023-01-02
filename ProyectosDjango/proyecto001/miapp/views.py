from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages



def inicio(request):
    return render (request,'inicio.html')
def integrantes(request):
    return render (request,'integrantes.html')
def crear_cursos(request):
    return render (request,'crear_cursos.html')
def crear_productos(request):
    return render (request,'crear_productos.html')



