from django.shortcuts import render , redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth import login , logout , authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from .form import LoginForm
class AccountsView(View):
    class_form = LoginForm
    template_name = 'accounts/login.html'
    def get(self,request):
        form = self.class_form
        return render(request, self.template_name,{'form':form})
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            return redirect("dashboard")

        return render(request, "accounts/login.html", {"form": form})
