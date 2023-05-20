from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'content', 'subtitle', 'author', 'isbn', 'price')

    def validate(self, data):
        title = data.get('title', None)
        author = data.get('author', None)

        # check title if it contains only alphabetical chars
        if title.isdigit():
            raise ValidationError(
                {
                    "status": False,
                    "message": "harf yozing"
                }
            )
        # check title and author from database exitice
        if Book.objects.filter(title=title, author=author).exists():
            raise ValidationError(
                {
                    "status": False,
                    "message": "sarlavha va muallif birxil"
                }
            )
        return data

    def validate_price(self, price):
        if price < 0:
            raise ValidationError(
                {
                    "status": False,
                    "message": "xoto narx"
                }
            )
