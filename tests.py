from django.test import TestCase
from django.test import TestCase
from .models import Book

class BookTestCase(TestCase):
    def setUp(self):
        Book.objects.create(title="Sample Book", author="Author Name", published_date="2023-01-01", isbn="1234567890123")

    def test_book_creation(self):
        book = Book.objects.get(title="Sample Book")
        self.assertEqual(book.author, "Author Name")

# Create your tests here.
