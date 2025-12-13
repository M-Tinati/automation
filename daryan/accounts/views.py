from django.shortcuts import render , redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth import login , logout , authenticate
from django.contrib.auth.mixins import LoginRequiredMixin

class AccountsView(View):
    template_name = 'accounts/login.html'
    def get(self,request):
        return render(request, self.template_name)
    def post(self,request):
        pass
