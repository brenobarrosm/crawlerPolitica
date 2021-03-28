import scrapy
from scrapy.selector import Selector
from scrapy.http import HtmlResponse
from WebCrawler.items import *
#from WebCrawler.items import DeputadoCamera

import sqlite3
# cria e conecta com banco de dados
conn = sqlite3.connect('deputados.db')
cursor = conn.cursor()
# cria tabela (schema)
cursor.execute("""
CREATE TABLE IF NOT EXISTS deputados (
     id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
     nome TEXT NOT NULL,
     nome_ficticio TEXT NOT NULL,
     partido TEXT NOT NULL,
     estado VARCHAR(2) NOT NULL,
     link TEXT NOT NULL,
     ano_entrada VARCHAR(4) NOT NULL,
     ano_saida VARCHAR(4) NOT NULL
 );
 """)
conn.close()

# classe para inserir os dados dos deputados no banco de dados local
class insertData():
	increment = 0
	# constructor
	def __init__(self, nome, nome_ficticio, partido, estado, link, ano_entrada, ano_saida):
		self.conn = sqlite3.connect('deputados.db')
		self.cursor = self.conn.cursor()
		self.nome = nome
		self.nome_ficticio = nome_ficticio
		self.partido = partido
		self.estado = estado
		self.link = link
		self.ano_entrada = ano_entrada
		self.ano_saida = ano_saida
	# salva no banco e 'printa' comentario
	def save(self):
		self.__class__.increment += 1
		self.id = self.__class__.increment
		try:
			self.cursor.execute("""
			INSERT INTO deputados (nome, nome_ficticio, partido, estado, link, ano_entrada, ano_saida)
			VALUES(?,?,?,?,?,?,?)
			""", (self.nome, self.nome_ficticio, self.partido, self.estado,self.link, self.ano_entrada, self.ano_saida))
			self.conn.commit()
			print('Inserido com sucesso: (id do banco) -> '+str(self.id))
			self.conn.close()
		except ValueError as identifier:
			print(identifier)

class DeputadosSpider(scrapy.Spider):
	name = 'Deputados'
	allowed_domains = ['www.camara.leg.br']
	start_urls = ['https://www.camara.leg.br/deputados/quem-sao']

	def parse(self, response):
		#Getting all Id(s)  'Deputados' 
		options = response.selector.xpath('//form/select/option').getall()

		#List all options selecteds
		for option in options:
			Id   = Selector(text=option).xpath('//option/@value').get() 
			link = 'https://www.camara.leg.br/deputados/'+ Id
			
			#This line below redirect to page and crawling informations
			yield scrapy.Request(url=link, callback= self.pagePersonal)

	#Getting informations in site 'https://www.camara.leg.br/deputados/'
	def pagePersonal(self, response):
		try:
			deputado = PoliticoItem()
			
			namefantasy  = response.selector.css('.nome-deputado ::text').get()
			if namefantasy[-1] == ' ':
				namefantasy = namefantasy[:-1]
			if namefantasy[0] == ' ':
				namefantasy = namefantasy[1:]
			name         = response.selector.xpath('//ul[@class="informacoes-deputado"]/li/text()').get()
			if name[-1] == ' ':
				name = name[:-1]
			if name[0] == ' ':
				name = name[1:]
			sigla = response.selector.css('.foto-deputado__partido-estado ::text').get()
			partido = sigla.replace(' ','').split('-')[0]
			state   = sigla.replace(' ','').split('-')[1]
			yearMandatory  = response.selector.css('.cargo-periodo__anos ::text').get() 
			yearInput = yearMandatory.replace(' ','').split('-')[0]
			yearOut   = yearMandatory.replace(' ','').split('-')[1]
			email = response.selector.css('.email ::text').get() 
			_id = response.selector.xpath('/html/head/meta[11]/@content').get()
			urlid = 'https://www.camara.leg.br'+_id

			deputado['name'] = name.upper()
			deputado['namefantasy'] = namefantasy.upper()
			deputado['sigla'] = sigla
			deputado['partido'] = partido
			deputado['state']= state
			deputado['yearInput']= yearInput
			deputado['yearOut'] = yearOut
			deputado['url']	= urlid
			deputado['email'] = email
			
			return deputado

		except ValueError as error:
			print(error)
