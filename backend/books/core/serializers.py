from rest_framework.serializers import ModelSerializer,SerializerMethodField
from .models import Book,Author

class BookUtilSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ('title','author','published_date','id','slug')


class BookSerializer(ModelSerializer):
    author = SerializerMethodField()
    author_obj = SerializerMethodField()
    class Meta:
        model = Book
        fields = ('title','author','published_date','id','author_obj','slug','image', 'price')

    def get_author(self,obj):
        return obj.author.first_name + ' ' + obj.author.last_name

    def get_author_obj(self,obj):
        return AuthorUtilSerializer(obj.author).data

class AuthorSerializer(ModelSerializer):
    books = SerializerMethodField()
    class Meta:
        model = Author
        fields = ('first_name','last_name','books','slug','state','id')

    def get_books(self,obj):
        return BookSerializer(obj.book_set.all(),many=True).data


class AuthorUtilSerializer(ModelSerializer):
    book_count = SerializerMethodField()
    class Meta:
        model = Author
        fields = ('slug','state','book_count')

    def get_book_count(self,obj):
        return obj.book_set.count()

    