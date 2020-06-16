from django.db import models
from tinymce import models as tinymce_models
from django.urls import reverse

class İletisim(models.Model):	
	firma_adi=models.CharField(max_length=300 )
	adres=models.TextField()
	telefon=models.CharField(max_length=200)
	gsm=models.CharField(max_length=200)
	e_posta=models.CharField(max_length=200)

	def __str__(self):
		return self.name

class Kategori(models.Model):	
	adi=models.CharField(max_length=400 )
	sira=models.IntegerField()

	def __str__(self):
		return self.name

class Temalar(models.Model):	
	firma_adi=models.CharField(max_length=300 )
	kategori=models.ForeignKey(Kategori, on_delete=models.CASCADE)
	fiyat=models.FloatField()
	iskonto=models.IntegerField()
	sira=models.IntegerField()

	def __str__(self):
		return self.name

class Referanslar(models.Model):	
	firma_adi=models.CharField(max_length=400 )
	logo=models.ImageField(upload_to='media')
	tema=models.ForeignKey(Temalar, on_delete=models.CASCADE)
	sira=models.IntegerField()

	def __str__(self):
		return self.name

class Slider(models.Model):	
	adi=models.CharField(max_length=400 )
	logo=models.ImageField(upload_to='media')
	sira=models.IntegerField()

	def __str__(self):
		return self.name

class Nedir(models.Model):	
	adi=models.CharField(max_length=300 )
	ozet=models.TextField()
	metin=models.TextField()
	sira=models.IntegerField()

	def __str__(self):
		return self.name

class Hesap_Bilgileri(models.Model):	
	iban=models.CharField(max_length=200 )
	hesap_adi=models.CharField(max_length=300)
	banka_adi=models.CharField(max_length=400)
	hesap_türü=models.CharField(max_length=200)
	sira=models.IntegerField()

	def __str__(self):
		return self.name

# Create your models here.
