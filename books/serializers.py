from rest_framework import serializers
from books.models import Book


class BookSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return Book.objects.create(
            title=validated_data.get('title'),
            description=validated_data.get('description'),
            published=validated_data.get('published')
        )

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.published = validated_data.get('published', instance.published)
        instance.save()
        return instance

    class Meta:
        model = Book
        fields = ('id',
                  'title',
                  'description',
                  'published')
