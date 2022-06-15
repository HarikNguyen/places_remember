from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm, UserEditForm, UserEditAvatarForm
from .models import UserWithAvatar

# Login
class LoginView(TemplateView):
    template_name = "account/login.html"

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            user = authenticate(request, username = cleaned_data['username'],
                                         password = cleaned_data['password'])
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return HttpResponse('Authenticated'' Successfully')
                else:
                    return HttpResponse('Disabled Account')
            else:
                return HttpResponse('Invalid login')
        else:
            form=LoginForm()
        return render(request, self.template_name, {'form':form})


    def get(self, request):
        current_user = request.user
        return render(request, self.template_name, {'current_user': current_user})

# Registration
class RegisterView(TemplateView):
    template_successful_name = 'account/register_done.html'
    template_name = 'account/register.html'
    def post(self, request):
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            UserWithAvatar.objects.create(user=new_user)
            return render(request, self.template_successful_name,{'new_user':new_user})
        else:
            user_form = UserRegistrationForm()
        return render(request, self.template_name, {'user_form':user_form})

# Edit info
class UserEditView(TemplateView):
    template_name = 'account/edit.html'
    def post(self, request):
        user_form = UserEditForm(instance=request.user, data=request.POST)
        avatar_form = UserEditAvatarForm(
            instance=request.user.userwithavatar, 
            data=request.POST, files=request.FILES)
        if user_form.is_valid() and avatar_form.is_valid():
            user_form.save()
            avatar_form.save()
            return render(request, self.template_name, {'user_form':user_form, 'avatar_form':avatar_form})
        else:
            user_form = UserEditForm(instance=request.user)
            avatar_form = UserEditAvatarForm(instance=request.user.userwithavatar)
        return render(request, self.template_name, {'user_form':user_form, 'avatar_form':avatar_form})
