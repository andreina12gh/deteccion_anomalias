from rest_framework.decorators import permission_classes
from rest_framework import generics
from rest_framework.permissions import AllowAny
from data.models import User
from data.serializers import UserSerializer
from django.shortcuts import render
from django import forms
from django.http import HttpResponse
from django.views import generic
from django.utils.translation import gettext_lazy as _
from django.views.generic.edit import FormMixin, ProcessFormView
from django import forms
from .forms import UserForm

class IndexView(generic.TemplateView):

    def get_context_data(self, **kwargs):
        self.context = {'urls' : [('sign_in','Registrarse')]}
        return self.context
'''def index(request):
    context = {'urls': [('sign_in','Registrarse')]}
    return render(request, template, context)
'''

def redirect(request):
    form = UserForm()
    #template = "data/login.html"
    #return render(request, template, {'request':request.path})
    return render(request, 'data/login.html', {'form':form})

def sign_in(request):
    #template = "data/sign_in.html"
    #return render(request, template)
    form = UserForm()
    return render(request, 'data/login.html', {'form':form})

def create(request):
    return HttpResponse(request)

'''
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('name', 'email', 'password', 'birth_date', 'gender')
'''
'''class UserForm(forms.ModelForm):

    name = forms.CharField(label=_("Nombre"),
                           max_length=150,
                           widget = forms.TextInput,
    )

    class Meta:
        model = User
        fields = ('name',)
        exclude = ('id', 'email','password','birth_date', 'gender')
        widgets = {
            'name' : forms.Textarea(attrs={'cols':80, 'rows':20}),
        }
class UserView(generic.FormView):
    template_name = "data/login.html"
    form_class = UserForm
    #form_class =
    #success_url = "/data/login"

    def form_valid(self, form):
        return HttpResponse("valid")

    def form_invalid(self, form):
        return HttpResponse("invalid")
'''
@permission_classes((AllowAny,))
class UserList(generics.ListCreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer

@permission_classes((AllowAny,))
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer