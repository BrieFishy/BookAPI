from rest_framework import serializers
from .models import BookData


class BookSerializer(serializers.ModelSerializer):
    book_image = serializers.ImageField(max_length=None, use_url=True)
    class Meta:
        model = BookData
        fields = ['book_name', 'book_category', 'book_description', 'book_rating', 'book_image']