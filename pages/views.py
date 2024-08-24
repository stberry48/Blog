from django.views.generic import CreateView
from django.views.generic import TemplateView
from django.views.generic import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

class HomePageView(TemplateView):
    template_name = 'pages/home.html'

class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

class SignUpView(CreateView):
    template_name = "registration/signup.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("login")




