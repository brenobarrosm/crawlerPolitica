import scrapy
import sqlite3
from WebCrawler.items import *
from politica.models import *
import re

class EmendasaprovadasSpider(scrapy.Spider):
    name = 'EmendasAprovadas'
    allowed_domains = ['www.camara.leg.br']
    start_urls = ['https://www.camara.leg.br/']

    def parse(self, response):
        try:
            politicos = Politico.objects.all()
            for politico in politicos:
                url = politico.url+"/_emendas?ano=2020"
                yield scrapy.Request(url=url, callback=self.pegando_emendas, meta={"id_politico":politico})
        except ValueError as error:
            print(error)

    def pegando_emendas(self, response):
        try:
            emendas = EmendasAprovadasItem()

            politico = response.meta['id_politico']
            _id_politico = politico.url
            _id = re.sub('[^0-9]', '', _id_politico)
            url = "https://www.camara.leg.br/deputados/"+_id+"/todas-emendas?ano=2020"

            emenda_maior = response.xpath('/html/body/div[1]/ul/li[1]/p/text()').get()
            autorizado_maior = response.xpath('/html/body/div[1]/ul/li[1]/ul/li[1]/span[2]/text()').get()
            empenhado_maior = response.xpath('/html/body/div[1]/ul/li[1]/ul/li[2]/span[2]/text()').get()
            pago_maior = response.xpath('/html/body/div[1]/ul/li[1]/ul/li[3]/span[2]/text()').get()

            emenda_media = response.xpath('/html/body/div[1]/ul/li[2]/p/text()').get()
            autorizado_media = response.xpath('/html/body/div[1]/ul/li[2]/ul/li[1]/span[2]/text()').get()
            empenhado_media = response.xpath('/html/body/div[1]/ul/li[2]/ul/li[2]/span[2]/text()').get()
            pago_media = response.xpath('/html/body/div[1]/ul/li[2]/ul/li[3]/span[2]/text()').get()

            emenda_menor = response.xpath('/html/body/div[1]/ul/li[3]/p/text()').get()
            autorizado_menor = response.xpath('/html/body/div[1]/ul/li[3]/ul/li[1]/span[2]/text()').get()
            empenhado_menor = response.xpath('/html/body/div[1]/ul/li[3]/ul/li[2]/span[2]/text()').get()
            pago_menor = response.xpath('/html/body/div[1]/ul/li[3]/ul/li[3]/span[2]/text()').get()

            emendas['politico'] = politico
            emendas['emenda_maior'] = emenda_maior
            emendas['autorizado_maior'] = autorizado_maior
            emendas['empenhado_maior'] = empenhado_maior
            emendas['pago_maior'] = pago_maior

            emendas['emenda_media'] = emenda_media
            emendas['autorizado_media'] = autorizado_media
            emendas['empenhado_media'] = empenhado_media
            emendas['pago_media'] = pago_media

            emendas['emenda_menor'] = emenda_menor
            emendas['autorizado_menor'] = autorizado_menor
            emendas['empenhado_menor'] = empenhado_menor
            emendas['pago_menor'] = pago_menor

            emendas['url'] = url

            if not EmendasAprovadas.objects.filter(politico=politico).exists():
                emendas.save()
        except ValueError as error:
            print(error)
