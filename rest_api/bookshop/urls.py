from django.urls import path
from .views import BookView, BooksView, AuthorView, AuthorsView, PublisherView, PublishersView

urlpatterns = [
    path('authors/', AuthorsView.as_view(), name='authors'),
    path('author/<int:id>/', AuthorView.as_view(), name='author-thing'),
    path('books/', BooksView.as_view()),
    path('book/<int:id>/', BookView.as_view()),
    path('publishers/', PublishersView.as_view()),
    path('publisher/<int:id>/', PublisherView.as_view()),
]
