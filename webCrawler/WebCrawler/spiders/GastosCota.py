import scrapy
import sqlite3
from WebCrawler.items import *
from bs4 import BeautifulSoup
from politica.models import *
import re

class GastoscotaSpider(scrapy.Spider):
    name = 'GastosCota'
    allowed_domains = ['camara.leg.br']
    start_urls = ['https://www.camara.leg.br/deputados/quem-sao/']

    def parse(self, response):
        try:
            url = "https://www.camara.leg.br/cota-parlamentar/"
            yield scrapy.Request(url=url, callback=self.gerando_link)
        except ValueError as error:
            print(error)
    
    def gerando_link(self, response):
        try:
            id_list = response.xpath('//ul[@id = "listaDeputados"]//input[@id]/@value').getall()
            for id_politico in id_list:
                try:
                    new_url = "https://www.camara.leg.br/cota-parlamentar/index.jsp?deputadosSelecionados="+id_politico+"&dataInicio=01/2020&dataFim=12/2020&despesa=todas&pesquisar=sim&cnpjFornecedor="
                    yield scrapy.Request(url=new_url, callback=self.pegando_gastos)
                except ValueError as error:
                    print("Erro de requisição")
        except ValueError as error:
            print(error)
    
    def pegando_gastos(self, response):
        try:
            gasto = GastosItem()

            gastos_deputados = response.xpath('//*[@id="nivel1Total0"]/text()').get()
            namefantasy = response.xpath('//*[@id="refinamentoAplicado"]/ul/li[1]/ul/li/ul/li/text()').get()
            gastos_total = re.sub(r"\s+", "", str(gastos_deputados))

            if namefantasy[-1] == ' ':
                namefantasy = namefantasy[:-1]
            if Politico.objects.filter(namefantasy=namefantasy.upper()):
                try:
                    politico = Politico.objects.filter(namefantasy=namefantasy.upper())[0]
                    gasto['politico'] = politico
                    gasto['gastos_total'] = gastos_total
                    gasto['link_para_camara'] = response.url
                except ValueError as error:
                    print(error)
                if not Gastos.objects.filter(politico=politico).exists():
                    try:
                        gasto.save()
                    except ValueError as error:
                        print(error)
        except ValueError as error:
            print(error)
