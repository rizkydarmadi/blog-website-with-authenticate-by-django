from django.conf.urls import url
from .views import (
    artikelistView,
    artikelDetailView,
    artikelkategoriListView,
    artikelCreateView,
    artikelManageView,
    artikelDeleteView,
    artikelUpdateView,
    )
from.import views



urlpatterns = [
    url(r'^manage/update/(?P<pk>\d+)$', artikelUpdateView.as_view(), name='update'),
    url(r'^manage/delete/(?P<pk>\d+)$', artikelDeleteView.as_view(), name='delete'),
    url(r'^manage/$', artikelManageView.as_view(), name='manage'),
    url(r'^tambah/$', artikelCreateView.as_view(), name='create'),
    url(r'^kategori/(?P<kategori>[\w ]+)/(?P<page>\d+)$', artikelkategoriListView.as_view(), name='category'),
    url(r'^detail/(?P<slug>[\w-]+)$', artikelDetailView.as_view(), name='detail'),
    url(r'^(?P<page>\d+)$', artikelistView.as_view(), name='list'),
]