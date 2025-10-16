from rest_framework import serializers
from .models import Author, Book, Borrow, Genre


# 1️⃣ Author Serializer
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


# 2️⃣ Genre Serializer
class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


# 3️⃣ Book Serializer
class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(
        queryset=Author.objects.all(), source='author', write_only=True
    )
    genre = GenreSerializer(read_only=True)
    genre_id = serializers.PrimaryKeyRelatedField(
        queryset=Genre.objects.all(), source='genre', write_only=True
    )

    class Meta:
        model = Book
        fields = [
            'id',
            'title',
            'author', 'author_id',
            'genre', 'genre_id',
            'published_date',
            'available_copies'
        ]


# 4️⃣ Borrow Serializer
class BorrowSerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)
    book_id = serializers.PrimaryKeyRelatedField(
        queryset=Book.objects.all(), source='book', write_only=True
    )

    class Meta:
        model = Borrow
        fields = [
            'id',
            'book', 'book_id',
            'borrower_name',
            'borrowed_on',
            'rented_days',
            'charges'
        ]
