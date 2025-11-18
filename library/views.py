from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Book
from .forms import BookForm

def base(request):
  return render(request, 'library/base.html')

def home(request):
  books = Book.objects.all()

  return render(request, 'library/home.html', {'books': books})

@login_required
def add_book(request):
  if request.method == "POST":
    form = BookForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('library:home')
  else:
    form = BookForm()
  return render(request, 'library/add_book.html', {'form': form})

@login_required
def delete_book(request, book_id):
  book = get_object_or_404(Book, pk=book_id)
  if request.method == "POST":
    book.delete()
    return redirect('library:home')
  return render(request, 'library/delete.html', {'book': book})

@login_required
def edit_book(request,book_id):
  book = get_object_or_404(Book, pk=book_id)
  if request.method == "POST":
    form = BookForm(request.POST, instance=book)
    if form.is_valid():
      form.save()
      return redirect('library:home')
  else:
    form = BookForm(instance=book)
  return render(request, 'library/edit.html', {'form': form})