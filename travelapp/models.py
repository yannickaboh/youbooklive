from django.db import models
import datetime

# Create your models here.

class Agence(models.Model):
	DEJACREE = 'Déjà crée'
	ENCREATION = 'En création'
	STATUS_AGENCE = [
        (DEJACREE, 'Déjà crée'),
        (ENCREATION, 'En création'),
    ]

	ONLINE = 'En ligne'
	OFFLINE = 'Hors ligne'
	CONNECTED = [
        (ONLINE, 'En ligne'),
        (OFFLINE, 'Hors ligne'),
    ]

	TERRESTRE = 'Voyage Terrestre'
	FERROVIAIRE = 'Voyage Ferroviaire'
	MARITIME = 'Voyage Maritime'
	AERIEN = 'Voyage Aérien'

	SERVICES = [
        (TERRESTRE, 'Voyage Terrestre'),
        (FERROVIAIRE, 'Voyage Ferroviaire'),
        (MARITIME, 'Voyage Maritime'),
        (AERIEN, 'Voyage Aérien'),
    ]

	ESPECES = 'Espèces'
	CARTECREDIT = 'Carte de crédit'
	MOBILEMONEY = 'Mobile Money'
	TOUT = 'Espèces, Carte de crédit...'

	METHOD_PAYMENT = [
        (ESPECES, 'Espèces'),
        (CARTECREDIT, 'Carte de crédit'),
        (MOBILEMONEY, 'Mobile Money'),
        (TOUT, 'Tout'),
    ]


	logo = models.ImageField(upload_to='agences', blank=True, verbose_name='Logo')
	slug = models.SlugField(max_length=250, unique=True, verbose_name='Code de l\'agence')
	name = models.CharField(max_length=250, unique=True, verbose_name='Nom de l\'agence')
	owner_name = models.CharField(max_length=250, blank=True, verbose_name='Nom du Propriétaire')
	district = models.CharField(max_length=250, verbose_name='Quartier')
	town = models.CharField(max_length=250, verbose_name='Ville')
	country = models.CharField(max_length=250, verbose_name='Pays')
	address = models.CharField(max_length=250, verbose_name='Adresse')
	email = models.EmailField(max_length=250, verbose_name='Email de l\'agence')
	phone = models.CharField(max_length=250, verbose_name='Téléphone  de l\'agence')
	description = models.TextField(blank=True, verbose_name='Description  de l\'agence')
	email_owner = models.EmailField(max_length=250, blank=True, verbose_name='Email du Propriétaire')
	phone_owner = models.CharField(max_length=250, blank=True, verbose_name='Téléphone du Propriétaire')
	website = models.CharField(max_length=250, blank=True, verbose_name='Site Web  de l\'agence')
	status = models.CharField(max_length=250, choices=STATUS_AGENCE, default=DEJACREE, verbose_name='Statut Actuel  de l\'agence')
	open_days = models.CharField(max_length=250, verbose_name='Jours Ouverts')
	closed_days = models.CharField(max_length=250, verbose_name='Jours Fermés')
	discount = models.IntegerField(blank=True, verbose_name='Remise', default='0')
	notes = models.IntegerField(blank=True, verbose_name='Notes', default='0')
	code_promo = models.CharField(max_length=250, verbose_name='Code Promo', blank=True)
	longitude = models.CharField(max_length=100, blank=True, default='0.0')
	latitude = models.CharField(max_length=100, blank=True, default='0.0')
	services = models.CharField(max_length=250, choices=SERVICES, default=TOUT, verbose_name='Nos Services')
	payment_method = models.CharField(max_length=250, choices=METHOD_PAYMENT, default=TOUT, verbose_name='Paiement Accepté')
	terms = models.BooleanField(verbose_name='Termes & Conditions')
	connected = models.CharField(max_length=250, choices=CONNECTED, default=OFFLINE, verbose_name='Ouvert ou Fermé ?')
	created = models.DateTimeField(auto_now_add=True, verbose_name='Date de Création')
	updated = models.DateTimeField(auto_now=True, verbose_name='Date de Modification')

	class Meta:
		ordering = ('name',)
		verbose_name = 'agence'
		verbose_name_plural = 'agences'

	def get_absolute_url(self):
		return "/agences/%i/" % self.id

	def __str__(self):
		return '{}'.format(self.name)


class TypeVoyage(models.Model):
	name = models.CharField(max_length=250, unique=True, verbose_name='Libellé')
	slug = models.SlugField(max_length=250, unique=True, verbose_name='Code')
	description = models.TextField(blank=True, verbose_name='Description')
	image = models.FileField(upload_to='type_voyages', blank=True, verbose_name='Image')

	class Meta:
		ordering = ('name',)
		verbose_name = 'type de voyage'
		verbose_name_plural = 'types de voyage'

	def __str__(self):
		return '{}'.format(self.name)

class Engin(models.Model):
	name = models.CharField(max_length=250, unique=True, verbose_name='Libellé')
	slug = models.SlugField(max_length=250, unique=True, verbose_name='Code')
	description = models.TextField(blank=True, verbose_name='Description')
	image = models.FileField(upload_to='engins', blank=True, verbose_name='Image')
	created = models.DateTimeField(auto_now_add=True, verbose_name='Date de Création')
	updated = models.DateTimeField(auto_now=True, verbose_name='Date de Modification')

	class Meta:
		ordering = ('name',)
		verbose_name = 'engin'
		verbose_name_plural = 'engins'

	def __str__(self):
		return '{}'.format(self.name)


class Voyage(models.Model):
	agence = models.ForeignKey(Agence, on_delete=models.CASCADE, verbose_name='Agence')
	typevoyage = models.ForeignKey(TypeVoyage, on_delete=models.CASCADE, verbose_name='Type de Voyage')
	engin = models.ForeignKey(Engin, on_delete=models.CASCADE, verbose_name='Engin')
	name = models.CharField(max_length=250, unique=True, verbose_name='Réference')
	date_depart = models.DateField(verbose_name='Date Départ')
	date_arrivee = models.DateField(verbose_name='Date Arrivée')
	heure_depart = models.TimeField(verbose_name='Heure Départ')
	heure_arrivee = models.TimeField(verbose_name='Heure Arrivée')
	ville_depart = models.CharField(max_length=250, verbose_name='Ville Départ')
	ville_arrivee = models.CharField(max_length=250, verbose_name='Ville Arrivée')
	description = models.TextField(blank=True, verbose_name='Description')
	nbre_places = models.IntegerField(verbose_name='Nombre de Places')
	stock = models.IntegerField(verbose_name='Stock')
	image = models.ImageField(upload_to='voyages', blank=True, verbose_name='Photo')
	available = models.BooleanField(default=True, verbose_name='Disponibilité')
	created = models.DateTimeField(auto_now_add=True, verbose_name='Date de Création')
	updated = models.DateTimeField(auto_now=True, verbose_name='Date de Modification')

	class Meta:
		ordering = ('name',)
		verbose_name = 'voyage'
		verbose_name_plural = 'voyages'

	def get_absolute_url(self):
		return "/agence/voyage/%i/" % self.id

	def __str__(self):
		return '{}'.format(self.name)


class ClasseVoyage(models.Model):
	voyage = models.ForeignKey(Voyage, on_delete=models.CASCADE, verbose_name='Voyage')
	name = models.CharField(max_length=250, verbose_name='Libellé')
	slug = models.SlugField(max_length=250, verbose_name='Code')
	description = models.TextField(blank=True, verbose_name='Description')
	price_adult = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Prix Adulte')
	price_child = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Prix Enfant')
	nbre_places_classe = models.IntegerField(verbose_name='Nombre de Places')
	stock_classe = models.IntegerField(verbose_name='Stock')
	created = models.DateTimeField(auto_now_add=True, verbose_name='Date de Création')
	updated = models.DateTimeField(auto_now=True, verbose_name='Date de Modification')

	class Meta:
		ordering = ('name',)
		verbose_name = 'classe voyage'
		verbose_name_plural = 'classes voyage'

	def __str__(self):
		return '{}'.format(self.name)


class Escale(models.Model):
	voyage = models.ForeignKey(Voyage, on_delete=models.CASCADE, verbose_name='Voyage')
	heure_arrivee = models.TimeField(verbose_name='Heure Arrivée')
	heure_depart = models.TimeField(verbose_name='Heure Départ')
	ville_arrivee = models.CharField(max_length=250, verbose_name='Ville Arrivée')
	created = models.DateTimeField(auto_now_add=True, verbose_name='Date de Création')
	updated = models.DateTimeField(auto_now=True, verbose_name='Date de Modification')

	class Meta:
		ordering = ('voyage',)
		verbose_name = 'escale'
		verbose_name_plural = 'escales'

	def __str__(self):
		return '{}'.format(self.ville_arrivee)
