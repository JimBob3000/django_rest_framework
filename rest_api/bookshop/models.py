from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=100)
    business_number = models.IntegerField()

    def __str__(self):
        return self.name


class Book(models.Model):
    author = models.ForeignKey(
        Author, related_name='books', on_delete=models.CASCADE)
    publisher = models.ForeignKey(
        Publisher, related_name='books', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    pages = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return self.title
