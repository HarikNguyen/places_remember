from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

from post.forms import PostForm
from .models import Post
class HomeView(TemplateView):
    template_name = 'homepage/home.html'

    def get(self, request):
        return render(request, self.template_name, {'section':'home'})

class CreateView(TemplateView):
    template_name = 'createPR/create.html'
    template_successful_name='homepage/home.html'
    @login_required
    def post(self, request):
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            new_post = post_form.save(commit=False)
            new_post.save()
            return render(request, self.template_successful_name)
        else:
            post_form = PostForm()
        return render(request, self.template_name, {'post_form':post_form})