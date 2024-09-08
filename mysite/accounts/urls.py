
from django.urls import include, path
from accounts.views import  AccountsDetailView, profile

from django.contrib.auth.decorators import login_required
urlpatterns = [

    path('', include('django.contrib.auth.urls')),
    path('profile/', profile, name='profile'),
    path('profile/<int:pk>', login_required(AccountsDetailView.as_view()), name='accounts.profile'),
]