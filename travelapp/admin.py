from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.conf import settings
from travelapp.forms import *
from travelapp.models import TypeVoyage, Agence, Engin, Voyage, ClasseVoyage, Escale


# Register your models here.


class TypeVoyageAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug']
	prepopulated_fields = {'slug':('name',)}

admin.site.register(TypeVoyage, TypeVoyageAdmin)

class AgenceAdmin(admin.ModelAdmin):
	list_display = ['name', 'owner_name', 'email', 'phone', 'created', 'updated']
	list_per_page = 10
	search_fields  = ('name',)

	fieldsets = (
        (None, {
            'fields': ('logo' ,'name', 'owner_name', 'district', 'town', 'country',
                'address', 'email', 'phone', 'description',
                'email_owner', 'phone_owner', 'website', 'status', 'open_days',
                'closed_days', 'discount', 'latitude', 'longitude', 'services',
                'payment_method', 'terms', 'slug')
        }),
    )

	class Media:
		if hasattr(settings, 'GOOGLE_MAPS_API_KEY') and settings.GOOGLE_MAPS_API_KEY:
			css = {
                'all': ('travelapp/css/admin/location_picker.css',),
            }
			js = (
                'https://maps.googleapis.com/maps/api/js?key={}'.format(settings.GOOGLE_MAPS_API_KEY),
                'travelapp/js/admin/location_picker.js',
            )

admin.site.register(Agence, AgenceAdmin)

class EnginAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug']
	prepopulated_fields = {'slug':('name',)}

admin.site.register(Engin, EnginAdmin)

class VoyageAdmin(admin.ModelAdmin):
	list_display = ['name', 'typevoyage','ville_depart','ville_arrivee','heure_depart','heure_arrivee', 'nbre_places', 'stock', 'available', 'created', 'updated']
	list_editable = ['nbre_places', 'stock', 'available']
	list_per_page = 10

admin.site.register(Voyage, VoyageAdmin)


class ClasseVoyageAdmin(admin.ModelAdmin):
	list_display = ['name', 'voyage', 'slug','nbre_places_classe','price_adult', 'price_child', 'stock_classe']
	prepopulated_fields = {'slug':('name',)}

admin.site.register(ClasseVoyage, ClasseVoyageAdmin)


class EscaleAdmin(admin.ModelAdmin):
	list_display = ['voyage', 'ville_arrivee','heure_arrivee','heure_depart']

admin.site.register(Escale, EscaleAdmin)
