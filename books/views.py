# -*- coding: utf-8 -*-
from datetime import datetime, date, time
from django.utils import timezone


from django.shortcuts import render, get_object_or_404,redirect,get_list_or_404
from django.http import HttpResponse
import json
from django.core.serializers.json import DjangoJSONEncoder

from .models import Books
from .forms import BookForm,FilterForm

#def books_list(request):
#    books = Books.objects.all
#    return render(request, 'books/books.html', {'books': books})


def books_list(request):

    book = Books.objects.order_by('published')



    if request.method == "POST":
        form = FilterForm(request.POST)
        if form.is_valid():


            order=form.cleaned_data['order']
            if order == 'Inc':
                book = Books.objects.order_by('published')
            else:
                book = Books.objects.order_by('-published')

            return render(request, 'books/books.html', {'form': form, 'books': book})


    else:
        form = FilterForm()


    return render(request, 'books/books.html', {'form': form,'books':book})




def new_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():

            book = form.save(commit=False)
            book.published = form.cleaned_data['published']
            book.save()
            return redirect('books_list')

    else:
        form = BookForm()
    return render(request, 'books/new_book.html', {'form': form})


def book_edit(request, nn):
    book = get_list_or_404(Books, isbn=nn)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book[0])
        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            return redirect('books_list')
    else:
        form = BookForm(instance=book[0])
    return render(request, 'books/book_edit.html', {'form': form})

def book_del(request,nn):
    book = get_list_or_404(Books, isbn=nn)
    book[0].delete()
    return redirect('books_list')