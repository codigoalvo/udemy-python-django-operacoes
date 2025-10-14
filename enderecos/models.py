from django.db import models


class Endereco(models.Model):
    logradouro = models.CharField(max_length=255, blank=False, null=False)
    bairro = models.CharField(max_length=255, blank=False, null=False)
    cidade = models.CharField(max_length=255, blank=False, null=False)
    numero = models.IntegerField(null=False, blank=False)
    cep = models.CharField(max_length=10, null=False, blank=False)

    def __str__(self):
        return self.logradouro
