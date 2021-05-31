from django.db import models
from django.db.models.fields import Field
from rest_framework import serializers
from .models import Book, Author, Publisher


class AuthorSerializer(serializers.ModelSerializer):
    books = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'email', 'books']
        # fields = '__all__'  #shows all fields


class PublisherSerializer(serializers.ModelSerializer):
    books = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Publisher
        fields = ['id', 'name', 'business_number', 'books']


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
