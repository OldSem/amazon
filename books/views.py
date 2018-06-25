# -*- coding: utf-8 -*-
from datetime import datetime, date, time
import logging
import logging.handlers

from django.utils import timezone

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404,redirect,get_list_or_404
from django.http import HttpResponse
import json
from django.core.serializers.json import DjangoJSONEncoder

from .models import Books,Document
from .forms import BookForm,FilterForm

#def books_list(request):
#    books = Books.objects.all
#    return render(request, 'books/books.html', {'books': books})
bytes=1024000
count=10
formatter = logging.Formatter("%(asctime)s-%(message)s")
logmodels = logging.getLogger('users')
logmodels.setLevel(logging.DEBUG)
MODELS_FILE = 'users.log'
handler = logging.handlers.RotatingFileHandler(MODELS_FILE, maxBytes=bytes, backupCount=count)
handler.setFormatter(formatter)
logmodels.addHandler(handler)






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



@login_required
def new_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():

            book = form.save(commit=False)
            book.published = form.cleaned_data['published']
            book.save()
            ip = request.META.get('REMOTE_ADDR', '') or request.META.get('HTTP_X_FORWARDED_FOR', '')
            logmodels.debug('%s %s %s' % (request.user, request.path, ip))
            return redirect('books_list')

    else:
        form = BookForm()
    return render(request, 'books/new_book.html', {'form': form})

@login_required
def book_edit(request, nn):
    book = get_list_or_404(Books, isbn=nn)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book[0])
        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            ip = request.META.get('REMOTE_ADDR', '') or request.META.get('HTTP_X_FORWARDED_FOR', '')
            logmodels.debug('%s %s %s' % (request.user, request.path, ip))
            return redirect('books_list')
    else:
        form = BookForm(instance=book[0])
    return render(request, 'books/book_edit.html', {'form': form})

@login_required
def book_del(request,nn):
    book = get_list_or_404(Books, isbn=nn)
    book[0].delete()
    ip = request.META.get('REMOTE_ADDR', '') or request.META.get('HTTP_X_FORWARDED_FOR', '')
    logmodels.debug('%s %s %s' % (request.user, request.path, ip))
    return redirect('books_list')

def log_view(request):
    return HttpResponse(content, content_type='user.log')

@login_required
def log_view(request):
    logs = open("users.log", "rb").read()
    logs = logs.split('\r\n')
    return render(request, 'books/log.html', {'logs': logs})
