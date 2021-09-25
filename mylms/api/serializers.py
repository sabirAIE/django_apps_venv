
from django.db import models
from django.db.models import fields
from django.utils import tree
from rest_framework import serializers
from .models import studentModel, songModel, singerModel

#model Serializers

# class studentModelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = studentModel
#         fields = ['name', 'roll', 'city']



#validation using Validators, We create a function to validate the Field and then we use it in the validators 
#while Creating a field in the serializers. It does not return anything but raises a validation error

# lets create a validator function
# def validate_isString(value):
#     if not isinstance(value, str):
#         raise serializers.ValidationError("Field input Should be In Letter")

#class Serializers
class studentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = studentModel
        fields = '__all__'


    # We do not awrite Create and update methods in Model Serializer So we are commenting it
    # def create(self,student_data):
    #     return studentModel.objects.create(**student_data)
    
    # #update Method for API Put Request
    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name',instance.name)
    #     instance.roll = validated_data.get('roll',instance.roll)
    #     instance.city = validated_data.get('city',instance.city)
    #     instance.save()
    #     return instance

    # #Field Level Validation 
    # def validate_roll(self, value):
    #     if value >200:
    #         raise serializers.ValidationError('Roll No mmust be below 200')
    #     elif not isinstance(value,int):
    #         raise serializers.ValidationError('Roll No Must be Interger')
    #     return value
    
    # # def validate_name(self, value):
    # #     if not isinstance(value, str):
    # #         raise serializers.ValidationError('Name must be in Letters')
    # #     return value

    # #object level validation Data is A dictionary data type
    # def validate(self, data):
    #     if data['name'].lower() =='imran' and data['city'].lower() !='ranchi':
    #         raise serializers.ValidationError(
    #             'Data Miss match'
    #         )
    #     return data


"""
@ Here we are going to have serializer Relation type
"""
class songModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = songModel
        fields = "__all__"

# class singerModelSerializer(serializers.ModelSerializer):
#     song = serializers.StringRelatedField(many=True, read_only=True)
#     # song = serializers.PrimaryKeyRelatedField(read_only=True)
#     # song = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='singerModel-detail')
#     class Meta:
#         model = singerModel
#         fields  = ['id','firstName','lastName','gender','song']

"""
@ One More Serializer Relation is Nested Serializer, to do that we do something like this
"""

class singerModelSerializer(serializers.ModelSerializer):
    # song = serializers.StringRelatedField(many=True, read_only=True)
    # song = serializers.PrimaryKeyRelatedField(read_only=True)
    # song = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='singerModel-detail')
    sungby = songModelSerializer(many=True,read_only=True)
    class Meta:
        model = singerModel
        fields  = ['id','firstName','lastName','gender','sungby']
