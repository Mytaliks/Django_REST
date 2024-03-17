from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Author
from rest_framework import serializers
from python_models import Author


class AuthorSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=128)
    birthday_year = serializers.IntegerField()

    def create(self, validated_data):
        return Author(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.birthday_year = validated_data.get('birthday_year', instance.birthday_year)

        return instance


data = {'name': 'Грин', 'birthday_year': 1880}
serializer = AuthorSerializer(data=data)
serializer.is_valid()
author = serializer.save()

data = {'name': 'Александр', 'birthday_year': 1880}
serializer = AuthorSerializer(author, data=data)
serializer.is_valid()
author = serializer.save()

data = {'birthday_year': 2000}
serializer = AuthorSerializer(author, data=data, partial=True)
serializer.is_valid()
author = serializer.save()
