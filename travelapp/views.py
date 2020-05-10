from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic
from django.contrib.auth.models import Group, User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.forms import ModelForm
import re
from django.db.models import Q
import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist
import urllib
from decimal import Decimal
from django.template import loader
from django import template
from django.template.loader import get_template
from django.core.mail import EmailMessage
from datetime import date

from travelapp import models

# Create your views here.

######################################################################################
#																					 #
#                              MANAGE YOUBOOK SITE                                   #
#																					 #
######################################################################################

# Acceuil
from travelapp.models import ClasseVoyage


def index(request):

    terrestres = ClasseVoyage.objects.filter(voyage__typevoyage__name__contains='Par Voie Terrestre').filter(voyage__date_depart__gte=date.today())[:8]
    trains = ClasseVoyage.objects.filter(voyage__typevoyage__name__contains='Par Voie Ferroviaire').filter(voyage__date_depart__gte=date.today())[:8]
    maritimes = ClasseVoyage.objects.filter(voyage__typevoyage__name__contains='Par Voie Maritime').filter(voyage__date_depart__gte=date.today())[:8]

    return render(request, 'site/index.html', {

        'terrestres':terrestres, 
        'trains':trains, 
        'maritimes':maritimes,


    })


def rechercher(request):

    terrestres = ClasseVoyage.objects.filter(voyage__typevoyage__name__contains='Par Voie Terrestre').filter(voyage__date_depart__gte=date.today())[:8]
    trains = ClasseVoyage.objects.filter(voyage__typevoyage__name__contains='Par Voie Ferroviaire').filter(voyage__date_depart__gte=date.today())[:8]
    maritimes = ClasseVoyage.objects.filter(voyage__typevoyage__name__contains='Par Voie Maritime').filter(voyage__date_depart__gte=date.today())[:8]

    ville_depart = None
    ville_arrivee = None
    if 'ville_depart' and 'ville_arrivee' in request.GET:
        ville_depart = request.GET.get('ville_depart')
        ville_arrivee = request.GET.get('ville_arrivee')

        results_terrestre = ClasseVoyage.objects.all().filter(

           Q(voyage__ville_depart__contains=ville_depart) & Q(voyage__ville_arrivee__contains=ville_arrivee),
           Q(voyage__typevoyage__name__contains='Par Voie Terrestre'), voyage__date_depart__gte=date.today()

        )

        # Paginate
        paginator = Paginator(results_terrestre, 2)
        page = request.GET.get('page')
        results_terrestre = paginator.get_page(page)

        results_ferroviaire = ClasseVoyage.objects.all().filter(

           Q(voyage__ville_depart__contains=ville_depart) & Q(voyage__ville_arrivee__contains=ville_arrivee),
           Q(voyage__typevoyage__name__contains='Par Voie Ferroviaire'

        ))

        # Paginate
        paginator = Paginator(results_ferroviaire, 8)
        page = request.GET.get('page')
        results_ferroviaire = paginator.get_page(page)

        results_maritime = ClasseVoyage.objects.all().filter(

           Q(voyage__ville_depart__contains=ville_depart) & Q(voyage__ville_arrivee__contains=ville_arrivee),
           Q(voyage__typevoyage__name__contains='Par Voie Maritime'

        ))

        # Paginate
        paginator = Paginator(results_maritime, 8)
        page = request.GET.get('page')
        results_maritime = paginator.get_page(page)

    return render(request, 'site/rechercher.html', {

        'terrestres':terrestres, 
        'trains':trains, 
        'maritimes':maritimes,

        'results_terrestre':results_terrestre,
        'results_ferroviaire':results_ferroviaire,
        'results_maritime':results_maritime,

        'ville_depart':ville_depart,
        'ville_arrivee':ville_arrivee


    })
