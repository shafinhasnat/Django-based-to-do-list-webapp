from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import List
from .forms import ListForm
from django.contrib import messages
def home(request):
	title = 'Home'
	if request.method == 'POST':
		form = ListForm(request.POST or None)
		if form.is_valid():
			form.save()
			all_items = List.objects.all
			messages.success(request, 'Yor item has been added to the list!!')
			return render(request, 'home.html', {'all_items': all_items, 'title': title})
		pass
	else:
		all_items = List.objects.all 
		return render(request, 'home.html', {'all_items': all_items, 'title': title})

def about(request):
	title = 'About'
	return render(request, 'about.html', {'title':title})

def delete(request, list_id):
	item = List.objects.get(pk=list_id)
	item.delete()
	messages.success(request, 'Yor item has been deleted!!')
	return redirect('home')


def uncross(request, list_id):
	item = List.objects.get(pk=list_id)
	item.completed = False
	item.save()
	return redirect('home')

def cross_off(request, list_id):
	item = List.objects.get(pk=list_id)
	item.completed = True
	item.save()
	return redirect('home')