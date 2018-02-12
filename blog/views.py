from django.http import HttpResponse
import datetime
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import View
from django.views import generic
from django.template import loader
from .models import Student
from .forms import studentpanel 

def index(request,):
	
	return render(request, 'blog/index.html',{})

def portal(request):
	all_students = Student.objects.all()
	
	return render(request, 'blog/index2.html', {'all_students': all_students})

def detail(request, student_id):
	all_you = Student.objects.all()
	entry = Student.objects.get(id=str(student_id))
	yd= Student.objects.filter(pk=str(student_id))
	return render(request, 'blog/index3.html', {'yd':yd})

def getDetail(request, pk):
	if request.method == 'POST':
		form = studentpanel(request.POST)
		return render(request, 'blog/index.html', {})

class StudentCreate (CreateView):
	model = Student
	fields = ['title']