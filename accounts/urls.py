from allauth.account.views import LogoutView
from django.urls import path, include

import accounts
from accounts.views import index

urlpatterns = [
    path('', index, name='index'),

    path('accounts/', include('allauth.urls')),
    path('accounts/logout/', LogoutView.as_view(), name='account_logout'),
]
