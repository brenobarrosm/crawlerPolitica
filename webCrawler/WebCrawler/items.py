# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem
from politica.models import *

class PoliticoItem(DjangoItem):
	django_model = Politico
	
class PresencaPlenarioItem(DjangoItem):
	django_model = PresencaPlenario

class BiographItem(DjangoItem):
	django_model = Biograph

class GastosItem(DjangoItem):
	django_model = Gastos

class VotosNominaisItem(DjangoItem):
	django_model = VotosNominais

class EmendasAprovadasItem(DjangoItem):
	django_model = EmendasAprovadas