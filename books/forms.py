from django import forms

from books.models import Book


class BookForm(forms.Form):
    title = forms.CharField(max_length=200)
    author = forms.CharField(max_length=200)
    year = forms.IntegerField()

    def save(self):
        title = self.cleaned_data['title']
        author = self.cleaned_data['author']
        year = self.cleaned_data['year']
        return Book.objects.create(
            title=title,
            author=author,
            year=year,
        )