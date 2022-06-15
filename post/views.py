from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'homepage/home.html'

    def get(self, request):
        return render(request, self.template_name, {'section':'home'})
