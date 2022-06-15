from django.urls import path
from .views import *

app_name = 'post'

urlpatterns = [
    # path('login/', LoginView.as_view(), name='login'),
    path('', HomeView.as_view(), name='home'),
]