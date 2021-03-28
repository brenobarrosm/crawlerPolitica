import scrapy
from politica.models import *
from scrapy.selector import Selector
from WebCrawler.items import *

class BibliografiaSpider(scrapy.Spider):
	name = 'Bibliografia'
	allowed_domains = ['www.camara.leg.br']
	start_urls = ['https://www.camara.leg.br/deputados/quem-sao']

	def parse(self, response):
		try:
			politicos = Politico.objects.all()
			for politico in politicos:
				url_new = politico.url + '/biografia'
				yield scrapy.Request(url=url_new, callback= self.processing_biografia, meta={'id_politico': politico})
				
		except ValueError as error:
			print(error)
	
	def processing_biografia(self,response):
		try:
			
			biograph = BiographItem()
			politico = response.meta['id_politico']
			
			element = response.selector.css('.informacoes-deputado').get()
			lis = Selector(text=element).css('li').getall()
			for li in lis:
				strli = li.replace('Escolaridade','')
				if strli != li:
					self.scholars = li.replace('<li>','').replace('</li>','').replace('<span>','').replace('</span>','').replace('Escolaridade:', '')
				strli = li.replace('Profissões:','')
				if strli != li:
					self.job = li.replace('<li>','').replace('</li>','').replace('<span>','').replace('</span>','').replace('Profissões:', '')
					
			biograph['politico'] = politico
			biograph['profession'] = self.job
			biograph['schooling'] = self.scholars
			
			if not Biograph.objects.filter(politico=politico, profession=self.job, schooling=self.scholars).exists():
				biograph.save()
			
		except ValueError as error:
			print(error)
	
