import scrapy
import sqlite3
from WebCrawler.items import *
from politica.models import *
import re

class VotosnominaisSpider(scrapy.Spider):
    name = 'VotosNominais'
    allowed_domains = ['www.camara.leg.br']
    start_urls = ['https://www.camara.leg.br/']

    def parse(self, response):
        try:
            politicos = Politico.objects.all()
            for politico in politicos:
                url = politico.url+"/_atuacao?ano=2020"
                yield scrapy.Request(url=url, callback=self.pegando_votos, meta={"id_politico":politico})
        except ValueError as error:
            print(error)

    def pegando_votos(self, response):
        try:
            votos = VotosNominaisItem()

            politico = response.meta['id_politico']
            _id_politico = politico.url
            _id = re.sub('[^0-9]', '', _id_politico)
            url = "https://www.camara.leg.br/deputados/"+_id+"/votacoes-nominais-plenario/2020"
            votos_nominais = response.xpath('/html/body/div[1]/div[2]/div/div[2]/div/div/a/text()').get()

            votos['politico'] = politico
            votos['url'] = url
            votos['votos_nominais'] = votos_nominais

            if not VotosNominais.objects.filter(politico=politico).exists():
                votos.save()
        except ValueError as error:
            print(error)