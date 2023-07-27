from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# class login_user(TemplateView):
#     template_name = 'templates/authentication/login.html'

#     def get_context_data(self, **kwargs):
#         context =  super().get_context_data(**kwargs)
#         return context

def login_user(request):
    return render( request, 'authenticate/login.html', {})

class LoginVista(TemplateView):
    template_name = 'authenticate/login.html'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        return context