from django.db import models


# Create your models here.
class Politico(models.Model):

    name = models.CharField(max_length=200, default='nulo')
    namefantasy = models.CharField(max_length=200, default='nulo')
    sigla = models.CharField(max_length=8, default='nulo')
    partido = models.CharField(max_length=8, default='nulo')
    state = models.CharField(max_length=4, default='nulo')
    yearInput = models.CharField(max_length=4, default='nulo')
    yearOut = models.CharField(max_length=4, default='nulo')
    email = models.CharField(max_length=200, default='nulo')
    url = models.URLField(verbose_name='Link', default='nulo')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Biograph(models.Model):

    profession = models.CharField(max_length=200, default='nulo')
    schooling = models.CharField(max_length=300, default='nulo')
    politico = models.ForeignKey(
        Politico, related_name='biograph', on_delete=False, null=True)

    def __str__(self):
        return self.profession


class PresencaPlenario(models.Model):
    totalSessoes = models.CharField(max_length=4, default='nulo')
    presencas = models.CharField(max_length=4, default='nulo')
    ausenciasJustificadas = models.CharField(max_length=4, default='nulo')
    ausenciasNaoJustificadas = models.CharField(max_length=4, default='nulo')
    politico = models.ForeignKey(
        Politico, related_name='presencaplenario', on_delete=False, null=True)

    def __str__(self):
        return self.totalSessoes + " sessões"
        

class Gastos(models.Model):

    politico = models.ForeignKey(
        Politico, related_name='gasto', on_delete=False, null=True)
    gastos_total = models.CharField(max_length=20, default='nulo')
    link_para_camara = models.CharField(max_length=200, default='nulo')

    def __str__(self):
        return self.politico.name
    # class Meta:
    # 	ordering = ["politico"]

class VotosNominais(models.Model):
    politico = models.ForeignKey(
        Politico, related_name='votosnominais', on_delete=False, null=True)
    url = models.URLField(verbose_name='Link', default='nulo')
    votos_nominais = models.CharField(max_length=3, default='nulo')

    def __str__(self):
        return self.politico.name

class EmendasAprovadas(models.Model):
    politico = models.ForeignKey(
        Politico, related_name='emendasaprovadas', on_delete=False, null=True)
    emenda_maior = models.CharField(max_length=255, default='nulo')
    autorizado_maior = models.CharField(max_length=20, default='nulo')
    empenhado_maior = models.CharField(max_length=20, default='nulo')
    pago_maior = models.CharField(max_length=20, default='nulo')

    emenda_media = models.CharField(max_length=255, default='nulo')
    autorizado_media = models.CharField(max_length=20, default='nulo')
    empenhado_media = models.CharField(max_length=20, default='nulo')
    pago_media = models.CharField(max_length=20, default='nulo')

    emenda_menor = models.CharField(max_length=255, default='nulo')
    autorizado_menor = models.CharField(max_length=20, default='nulo')
    empenhado_menor = models.CharField(max_length=20, default='nulo')
    pago_menor = models.CharField(max_length=20, default='nulo')

    url = models.URLField(verbose_name='Link', default='nulo')

    def __str__(self):
        return self.politico.name