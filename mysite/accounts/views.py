from django.shortcuts import render, redirect ,reverse
from django.http import HttpResponse
from django.views.generic import  DetailView

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required()
def profile(request):
    print("User.id",request.user.id)
    url = reverse("accounts.profile", args=[request.user.id])
    # return  HttpResponse("Hello, world. You're at the profile of mysite.")
    return redirect(url)


class AccountsDetailView(DetailView):
    model = User
    template_name = 'accounts/accounts_detail.html'
