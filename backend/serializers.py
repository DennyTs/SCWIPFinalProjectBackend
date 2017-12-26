from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Institution, Institutions_Unit, Capacity, City, Aqi, Comment, Favorite, UserProfile
from django.conf import settings


# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ('url', 'username', 'email', 'groups')

# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ('url', 'name')


class UserRegistrationSerializer(serializers.ModelSerializer):
    
    email = serializers.EmailField(
        required=True,
        label="Email Address"
    )

    password = serializers.CharField(
        required=True,
        label="Password",
        style={'input_type': 'password'}
    )

    fullName = serializers.CharField(
        required=True,
        label="Name"
    )

    class Meta(object):
        model = User
        fields = ['fullName', 'email', 'password']


class InstitutionUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institutions_Unit
        fields = '__all__'
        ordering = ['Ins_id']
        depth = 1

class InstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institution
        fields = '__all__'
        ordering = ['ins_id']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        ordering = ['id']

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'
        ordering = ['created']

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'
        ordering = ['city_id']