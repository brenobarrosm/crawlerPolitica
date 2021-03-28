import scrapy
from datetime import datetime
import sqlite3
from WebCrawler.items import *
from bs4 import BeautifulSoup
from politica.models import *

# classe para realiar o crawler da página


class PresencaPlenarioSpider(scrapy.Spider):

    name = 'PresencaPlenario'
    allowed_domains = ['camara.leg.br']
    start_urls = ['https://www.camara.leg.br/deputados/quem-sao']

    # método para realizar o crawler
    def parse(self, response):

        try:

            politicos = Politico.objects.all()

            for politico in politicos:
                url_new = politico.url + "/presenca-plenario/2020"
                yield scrapy.Request(url=url_new, callback=self.processing_presenca, meta={'id_politico': politico})

        except ValueError as error:
            print(error)

    def processing_presenca(self, response):

        try:
            presencaPlenario = PresencaPlenarioItem()
            politico = response.meta['id_politico']

            verificacao = response.selector.xpath(
                '//*[@id="main-content"]/section/div/table[2]/tbody/tr[5]/td[2]//text()').get()

            if verificacao:

                totalSessoes = response.selector.xpath(
                    '//*[@id="main-content"]/section/div/table[2]/tbody/tr[5]/td[2]//text()').get().strip()
                presencas = response.selector.xpath(
                    '//*[@id="main-content"]/section/div/table[2]/tbody/tr[6]/td[2]//text()').get().strip()
                ausenciasJustificadas = response.selector.xpath(
                    '//*[@id="main-content"]/section/div/table[2]/tbody/tr[7]/td[2]//text()').get().strip()
                ausenciasNaoJustificadas = response.selector.xpath(
                    '//*[@id="main-content"]/section/div/table[2]/tbody/tr[8]/td[2]//text()').get().strip()

                presencaPlenario['politico'] = politico
                presencaPlenario['totalSessoes'] = totalSessoes
                presencaPlenario['presencas'] = presencas
                presencaPlenario['ausenciasJustificadas'] = ausenciasJustificadas
                presencaPlenario['ausenciasNaoJustificadas'] = ausenciasNaoJustificadas

            else:

                presencaPlenario['politico'] = politico
                presencaPlenario['totalSessoes'] = "0"
                presencaPlenario['presencas'] = "0"
                presencaPlenario['ausenciasJustificadas'] = "0"
                presencaPlenario['ausenciasNaoJustificadas'] = "0"

            if not PresencaPlenario.objects.filter(politico=politico).exists():
                presencaPlenario.save()

        except ValueError as error:
            print(error)
