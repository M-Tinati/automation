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

    def post(self,request):
        form = self.class_form(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,username = cd['username'],password = cd['password'])
            if user is not None:
                login(request,user)
                messages.success(request,"وارد حساب کاربری خود شدید" , 'success')
                return redirect('home:home')
            messages.error(request,"شماره تلفن و رمز عبور اشتباه است" , 'warning')
        return render(request,self.template_name,{'form':form})