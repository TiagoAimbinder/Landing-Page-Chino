from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout

class HomeVista(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)

        return context

class LoginVista(TemplateView):
    template_name = 'login.html'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        username = request.POST["username"]
        password = request.POST["password"]
        print(username, password)
        user = authenticate(request, username=username, password=password)

        if user is not None:
            print("Usuario Correcto")
            login(request,user)
        else:
            print("Usuario Incorrecto")
                
        return redirect('home')

def logoutUser(request):
    logout(request)
    return redirect('home')