from rest_framework import serializers
from book.models import Book


class bookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'name', 'page', 'price']

    def create(self, validated_data):
        """
        Create and return a new `book` instance, given the validated data.
        """
        return Book.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `book` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.page = validated_data.get('page', instance.page)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance