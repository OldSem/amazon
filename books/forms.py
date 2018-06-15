# -*- coding: utf-8 -*-
from django import forms
from .models import Books



class BookForm(forms.ModelForm):

    class Meta:

        model = Books

        fields = ('title','author','isbn','price')
        labels = {'title':u'Название','author':u'Автор','isbn':u'ISBN','price':u'Цена'}
        values = {"save":u'Сохранить'}
