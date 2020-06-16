from django.urls import path
from . import views

urlpatterns = [
	
	path('iletisim/', views.İletisimListView.as_view(), name='iletisim'),
	path('iletisim-detail/<int:pk>', views.İletisimDetailView.as_view(), name='iletisim-detail'),

	path('temalar/', views.TemalarListView.as_view(), name='temalar'),
	path('temalar-detail/<int:pk>', views.TemalarDetailView.as_view(), name='temalar-detail'),	

	path('referanslar/', views.ReferanslarListView.as_view(), name='referanslar'),

	path('hesap-bilgileri/', views.Hesap_BilgileriListView.as_view(), name='hesap-bilgileri'),	
	path('hesap-bilgileri-detail/<int:pk>', views.Hesap_BilgileriDetailView.as_view(), name='hesap-bilgileri-detail'),
	
	path('nedir/', views.NedirListView.as_view(), name='nedir'),	
	path('nedir-detail/<int:pk>', views.NedirDetailView.as_view(), name='nedir-detail'),


]