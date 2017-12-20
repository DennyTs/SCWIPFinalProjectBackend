
from datetime import datetime
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets

from .serializers import UserSerializer, GroupSerializer, InstitutionUnitSerializer
from rest_framework import generics
from .models import Institution, Institutions_Unit, Capacity, City


from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class InstitutionUnitList(generics.ListAPIView):
    queryset = Institutions_Unit.objects.all()
    serializer_class = InstitutionUnitSerializer


def home(request):
    ins_list = Institution.objects.all()
    return render(request, 'home2.html', {
        'ins_list': ins_list,
    })

def main(request):
    '''
    Render the main page
    '''
    context = {'like':'Django 很棒'}
    return render(request, 'main.html', context)

def about(request):
    '''
    Render the about page
    '''
    return render(request, 'about.html')