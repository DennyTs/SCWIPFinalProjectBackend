
from datetime import datetime
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets

from .serializers import UserSerializer, GroupSerializer, InstitutionUnitSerializer
from rest_framework import generics
from .models import Institution, Institutions_Unit, Capacity, City, Comment

from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.http import HttpResponse

from django.contrib import messages
from .form import UserForm, UserProfileForm

from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login

from django.contrib.auth import logout as auth_logout


# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer

# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer

# class InstitutionUnitList(generics.ListAPIView):
#     queryset = Institutions_Unit.objects.all()
#     serializer_class = InstitutionUnitSerializer


def home(request):
    ins_list = Institution.objects.all()
    return render(request, 'home2.html', {
        'ins_list': ins_list,
    })

def main(request):
    '''
    Render the main page
    '''
    context = {'like':'這行是由view.main所print'}
    return render(request, 'main.html', context)

def about(request):
    '''
    Render the about page
    '''
    return render(request, 'about.html')


#輸出機構及其對應的留言
def institution(request):
    '''
    Render the article page
    '''
    institution = Institution.objects.all()
    itemList = []
    for institution in institution :
        items = [institution]
        items.extend(list(Comment.objects.filter(ins_id=institution.ins_id)))
        itemList.append(items)
    return render(request, 'about.html', context)

#註冊
def register(request):
    '''
    Register a new user
    '''
    template = 'register.html'
    if request.method == 'GET':
        return render(request, template, {'userForm':UserForm(),
                                          'userProfileForm':UserProfileForm()})
    # POST
    userForm = UserForm(request.POST)
    userProfileForm = UserProfileForm(request.POST)
    if not userForm.is_valid() or not userProfileForm.is_valid():
        return render(request, template, {'userForm':userForm,
                                          'userProfileForm':userProfileForm})
    user = userForm.save()
    userProfile = userProfileForm.save(commit=False)
    userProfile.user = user
    userProfile.save()
    messages.success(request, '歡迎註冊')
    return redirect('main:main')

#登入
def login(request):
    '''
    Login an existing user
    '''
    template = 'login.html'
    if request.method == 'GET':
        return render(request, template)
    # POST
    username = request.POST.get('username')
    password = request.POST.get('password')
    if not username or not password:    # Server-side validation
        messages.error(request, '請填資料')
        return render(request, template)
    user = authenticate(username=username, password=password)
    if not user:    # authentication fails
        messages.error(request, '登入失敗')
        return render(request, template)
    if not user.is_active:
        messages.error(request, '帳號已停用')
        return render(request, template)
    # login success
    auth_login(request, user)
    messages.success(request, '登入成功')
    return redirect('main:main')

#logout
def logout(request):
    '''
    Logout the user
    '''
    auth_logout(request)
    messages.success(request, '歡迎再度光臨')
    return redirect('main:main')    