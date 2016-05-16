from models import *
#from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

# class DetectAnomalySerializer(ModelSerializer):
'''class UserSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, allow_blank=False, max_length=150)
    email = serializers.EmailField(allow_blank=False)
    password = serializers.CharField(allow_blank=False)
    birth_date = serializers.DateField(allow_null=False)
    gender = serializers.CharField(allow_blank=False)

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('code', instance.email)
        instance.password = validated_data.get('password', instance.password)
        instance.birth_date = validated_data.get('birth_date', instance.birth_date)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.save()
        return instance
'''
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name','email', 'password','birth_date','gender')

class TransferSerializer(ModelSerializer):
    #user = Pri

    class Meta:
        model = Transfer
        fields = ()