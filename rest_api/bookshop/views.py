from rest_framework import generics
from rest_framework import mixins
from .models import Book, Author, Publisher
from .serializers import AuthorSerializer, BookSerializer, PublisherSerializer


class AuthorView(
        generics.GenericAPIView,
        mixins.ListModelMixin,
        mixins.CreateModelMixin,
        mixins.UpdateModelMixin,
        mixins.RetrieveModelMixin,
        mixins.DestroyModelMixin):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()

    lookup_field = 'id'

    def get(self, request, id):
        return self.retrieve(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id):
        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)


class AuthorsView(
        generics.GenericAPIView,
        mixins.ListModelMixin):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()

    def get(self, request):
        return self.list(request)


class PublisherView(
        generics.GenericAPIView,
        mixins.ListModelMixin,
        mixins.CreateModelMixin,
        mixins.UpdateModelMixin,
        mixins.RetrieveModelMixin,
        mixins.DestroyModelMixin):
    serializer_class = PublisherSerializer
    queryset = Publisher.objects.all()

    lookup_field = 'id'

    def get(self, request, id):
        return self.retrieve(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id):
        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)


class PublishersView(
        generics.GenericAPIView,
        mixins.ListModelMixin):
    serializer_class = PublisherSerializer
    queryset = Publisher.objects.all()

    def get(self, request):
        return self.list(request)


class BookView(
        generics.GenericAPIView,
        mixins.ListModelMixin,
        mixins.CreateModelMixin,
        mixins.UpdateModelMixin,
        mixins.RetrieveModelMixin,
        mixins.DestroyModelMixin):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    lookup_field = 'id'

    def get(self, request, id):
        return self.retrieve(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id):
        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)


class BooksView(
        generics.GenericAPIView,
        mixins.ListModelMixin):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    def get(self, request):
        return self.list(request)
