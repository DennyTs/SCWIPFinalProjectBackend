from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Institution, Institutions_Unit, Capacity, City

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class InstitutionUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institutions_Unit
        fields = '__all__'
        ordering = ['Ins_id']
        depth = 1
