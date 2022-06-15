from django.urls import path, include
from .views import *
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.conf import settings
from django.conf.urls.static import static

app_name = 'user'

urlpatterns = [
    # login
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # change password
    path('password_change/',
        auth_views.PasswordChangeView.as_view(
            success_url=reverse_lazy('accounts:password_change_done')
        ),
        name='password_change'),
    path('password_change/done/',
        auth_views.PasswordChangeDoneView.as_view(),
        name='password_change_done'),

    # reset password
    path('password_reset', 
        auth_views.PasswordResetView.as_view(
            success_url=reverse_lazy('accounts:password_reset_done')
        ),
        name='password_reset'),
    path('password_reset/done', 
        auth_views.PasswordResetDoneView.as_view(),
        name='password_reset_done'),
    path('reset/<uidb64>/<token>/', 
        auth_views.PasswordResetConfirmView.as_view(
            success_url=reverse_lazy('accounts:password_reset_complete')
        ),
        name='password_reset_confirm'),
    path('reset/done', 
        auth_views.PasswordResetCompleteView.as_view(),
        name='password_reset_complete'),

    # register
    path('register/', RegisterView.as_view(), name='register'),

    # edit
    path('edit/', UserEditView.as_view(), name='edit'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)