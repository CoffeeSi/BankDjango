from django.urls import path

from users.views import login, logout

app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),
    path('logout', logout, name='logout'),
]
