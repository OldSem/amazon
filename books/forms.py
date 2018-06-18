# -*- coding: utf-8 -*-
from django.contrib.admin.widgets import AdminDateWidget
from django import forms
from .models import Books


class FilterForm(forms.Form):
    order = forms.ChoiceField(label = 'Дата публикации',widget=forms.RadioSelect, choices=(('Inc', u'По возростанию',), ('Desc', u'По убыванию',)))


class BookForm(forms.ModelForm):

    published = forms.DateField(widget=forms.SelectDateWidget(years=range(1600, 2020)))
    class Meta:

        model = Books

        fields = ('title','author','isbn','price')
        labels = {'title':u'Название','author':u'Автор','isbn':u'ISBN','price':u'Цена'}
        values = {"save":u'Сохранить'}
