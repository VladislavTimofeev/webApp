import enum

from django.db import models


class Role(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=60)


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=30)
    role_id = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.email}"


class Genre(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=60)


class Book(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=60)
    genre_id = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}


class WaitList(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)


class NotificationType(enum.Enum):
    id = models.IntegerField(primary_key=True)
    Reserved = 1
    Reservation_finished = 2
    Reservation_cancelled = 3
    Reservation_expired = 4


class Notification(models.Model):
    sent = models.DateTimeField()
    type = NotificationType  # check is needed
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)


class Publisher(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=60)


class BookCopy(models.Model):
    id = models.IntegerField(primary_key=True)
    year_of_publishing = models.IntegerField()

    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    publisher_id = models.ForeignKey(Publisher, on_delete=models.CASCADE)


class BorrowedBook(models.Model):
    id = models.IntegerField(primary_key=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    is_returned = False

    book_copy_id = models.ForeignKey(BookCopy, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)


class Hold(models.Model):
    id = models.IntegerField(primary_key=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    book_copy_id = models.ForeignKey(BookCopy, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)


class Author(models.Model):
    id = models.IntegerField(primary_key=True)
    author_firstname = models.CharField(max_length=60)
    author_lastname = models.CharField(max_length=60)


class BookAuthor(models.Model):
    id = models.IntegerField(primary_key=True)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE)
