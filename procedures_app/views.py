from django.shortcuts import redirect, render
from django.views.generic.base import View
from django.db import connection

from .forms import *
from .models import *

class IndexView(View):
    def get(self, request):
        users = MyUser.objects.all()
        return render(request, "procedures_app/index.html", {'users': users})


class CreatePageView(View):
    def get(self, request):
        return render(request, "procedures_app/create_page.html")


class CreateView(View):
    def post(self, request):
        form = CreateMyUser(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            c = connection.cursor()
            c.execute("CALL create_myuser( %s); ", (name, ))
        
        return redirect('/')


class UpdatePageView(View):
    def get(self, request, pk):
        user = MyUser.objects.get(id=pk)
        return render(request, "procedures_app/update_page.html", {'user': user})


class UpdateView(View):
    def post(self, request):
        form = UpdateMyUser(request.POST)
        if form.is_valid():
            id = form.cleaned_data['id']
            name = form.cleaned_data['name']
            c = connection.cursor()
            c.execute("CALL update_myuser( %s, %s); ", (id, name))
        
        return redirect('/')


class DeletePageView(View):
    def get(self, request, pk):
        user = MyUser.objects.get(id=pk)
        return render(request, "procedures_app/delete_page.html", {'user': user})


class DeleteView(View):
    def post(self, request):
        form = DeleteMyUser(request.POST)
        if form.is_valid():
            id = form.cleaned_data['id']
            c = connection.cursor()
            c.execute("CALL delete_myuser( %s); ", (id,))
        
        return redirect('/')