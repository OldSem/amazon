# -*- coding: utf-8 -*-

from django.conf.urls import url,include
from . import views


urlpatterns = [
    url(r'^$', views.books_list, name='books_list'),
    url(r'^new_book/$', views.new_book, name='new_book'),
    #url(r'^ads_filter/(?P<teg>[0-9]+)/(?P<activ>[1-2])/(?P<b_date>)/(?P<e_date>)/(?P<text>)/$', views.ads_filter, name='ads_filter'),
    #url(r'^new/dte/$', views.new_dte, name='new_dte'),
    url(r'^log/(?P<nn>[0-9]+)/$', views.log_view, name='log_view'),
    url(r'^book/(?P<nn>[0-9]+)/del/$', views.book_del, name='book_del'),
    url(r'^book/(?P<nn>[0-9]+)/edit/$', views.book_edit, name='book_edit'),

]
urlpatterns += [
    url(r'^accounts/', include('django.contrib.auth.urls')),
]