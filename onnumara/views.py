from django.shortcuts import render
from onnumara.models import İletisim, Kategori, Temalar, Referanslar, Nedir, Hesap_Bilgileri
from django.views import generic

class TemalarListView(generic.ListView):
    model = Temalar

class TemalarDetailView(generic.DetailView):
	model = Temalar

class ReferanslarListView(generic.ListView):
    model = Referanslar

class İletisimListView(generic.ListView):
    model = İletisim

class İletisimDetailView(generic.DetailView):
	model = İletisim

class Hesap_BilgileriListView(generic.ListView):
    model = Hesap_Bilgileri

class Hesap_BilgileriDetailView(generic.DetailView):
	model = Hesap_Bilgileri


class NedirListView(generic.ListView):
    model = Nedir

class NedirDetailView(generic.DetailView):
	model = Nedir
# Create your views here.
