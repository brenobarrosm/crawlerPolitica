# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from politica.models import *



class PoliticoPipeline(object):
	
	def process_item(self, item, spider):
		try:
			name = item['name']
			namefantasy = item['namefantasy']
			sigla = item['sigla']
			partido = item['partido']
			state = item['state']
			yearInput = item['yearInput']
			yearOut = item['yearOut']
			email = item['email']
			url = item['url']
	
			if not Politico.objects.filter(name=name, namefantasy=namefantasy, partido=partido).exists():
				Politico.objects.create(name=name, namefantasy=namefantasy,sigla=sigla, partido=partido,state=state,
			yearInput=yearInput, yearOut=yearOut, email=email, url=url)
			
			return item
			
		except ValueError as error:
			print(error)

class PresencaPlenarioPipeline(object):

	def process_item(self, item, spider):
		try:
			# totalSessoes = item['totalSessoes']
			# presencas = item['presencas']
			# ausenciasJustificadas = ['ausenciasJustificadas']
			# ausenciasNaoJustificadas = ['ausenciasNaoJustificadas']

			return item
		except ValueError as error:
			print(error)

class BiographPipeline(object):
	
	def process_item(self, item, spider):
		try:
			#profession = item['profession']
			#schooling = item['schooling']
			#politico = item['politico']
			
			#if not Biograph.objects.filter(profession=profession, politico=politico).exists():
			#	Biograph.objects.create(profession=profession, schooling=schooling, politico=politico)
			return item
		except ValueError as error:
			print(error)

class GastosPipeline(object):

	def process_item(self, item, spider):
		try:

			# nomes_deputados = item['nomes_deputados']
			# gastos_total = item['gastos_total']
			# link_para_camara = item['link_para_camara']

			# if not Gastos.objects.filter(nomes_deputados=nomes_deputados, gastos_total=gastos_total).exists():
			# 	Gastos.objects.create(nomes_deputados=nomes_deputados, gastos_total=gastos_total,link_para_camara=link_para_camara)

			return item
		except ValueError as error:
			print(error)

class VotosNominaisPipeline(object):

	def process_item(self, item, spider):
		try:
			# votacoes_nominais = item['votacoes_nominais']
			# url = item['url']
			# politico = item['politico']

			# if not VotosNominais.objects.filter(politico=politico).exists():
			# VotosNominais.objects.create(votacoes_nominais=votacoes_nominais, url=url, politico=politico)
			return item
		except ValueError as error:
			print(error)

class EmendasAprovadas(object):

	def process_item(self, item, spider):
		try:
			# politico = item['politico']
			# emenda_maior = item['emenda_maior']
			# autorizado_maior = item['autorizado_maior']
			# empenhado_maior = item['empenhado_maior']
			# pago_maior = item['pago_maior']

			# emenda_media = item['emenda_media']
			# autorizado_media = item['autorizado_media']
			# empenhado_media = item['empenhado_media']
			# pago_media = item['pago_media']

			# emenda_menor = item['emenda_menor']
			# autorizado_menor = item['autorizado_menor']
			# empenhado_menor = item['empenhado_menor']
			# pago_menor = item['pago_menor']

			# if not EmendasAprovadas.objects.filter(politico=politico).exists():
			# EmendasAprovadas.objects.create(politico=politico, emenda_maior=emenda_maior, autorizado_maior=autorizado_maior,
			# pago_maior=pago_maior, emenda_media=emenda_media, autorizado_media=autorizado_media,
			# empenhado_media=empenhado_media, pago_media=pago_media, emenda_menor=emenda_menor
			# autorizado_menor=autorizado_menor, empenhado_menor=empenhado_menor, pago_menor=pago_menor)
			return item
		except ValueError as error:
			print(error)