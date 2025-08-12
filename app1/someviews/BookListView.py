from django.http import HttpResponse
from django.views.generic import ListView
from app1.models import Book

class BookListView(ListView):
    model = Book
    template_name = 'bookList.html'

    def head(self, *args, **kwargs):
        last_book = self.get_queryset().latest('publication_date')
        response = HttpResponse(
            headers={'Last-Modified': last_book.publication_date.strftime('%a, %d %b %Y %H:%M:%S GMT')},
        )
        return response