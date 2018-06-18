# -*- coding: utf-8 -*-
from django.contrib.admin.widgets import AdminDateWidget
from django import forms
from .models import Books



class BookForm(forms.ModelForm):

    published = forms.DateField(widget=forms.SelectDateWidget(years=range(1600, 2020)))
    class Meta:

        model = Books

        fields = ('title','author','isbn','price')
        labels = {'title':u'Название','author':u'Автор','isbn':u'ISBN','price':u'Цена'}
        values = {"save":u'Сохранить'}
