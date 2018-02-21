import datetime
from django.db import models
from django.utils import timezone
import logging
logger=logging.getLogger(__name__)

class Assistencia(models.Model):
    produto = models.ForeignKey('Produto', on_delete=models.CASCADE)
    funcionario = models.ForeignKey('Pessoa',related_name="funcionario", on_delete=models.CASCADE)
    cliente = models.ForeignKey('Pessoa',related_name="cliente", on_delete=models.CASCADE)
    topico_text = models.CharField(max_length=50)
    descricao_text = models.TextField(max_length=200)
    pub_date = models.DateField()
    valor = models.DecimalField(decimal_places=2,max_digits=5, blank=True)
    foto = models.FileField(blank=True)
    pago_bol = models.BooleanField(default=False)

    @property
    def get(self):
        data = {'produto':self.produto.id,'funcionario':self.funcionario.nome_text,
                'cliente':self.cliente.nome_text,'topico_text':self.topico_text,
                'descricao_text':self.descricao_text,'valor':self.valor,
                'pago_bol':self.pago_bol}
        return data

    def __str__(self):
        return self.topico_text

    @property
    def sendAssistencia(self):
        id=self.id
        produto = self.produto.descricao_text
        funcionario = self.funcionario.nome_text
        cliente = self.cliente.nome_text
        topico = self.topico_text
        descricao = self.descricao_text
        valor = float(self.valor)
        pago = self.pago_bol
        jsonObj = {'id':id,'produto':produto,'cliente':cliente,'topico':topico,'descricao':descricao,
                   'valor':valor,'pago':pago}
        logger.error("borala",jsonObj)
        return jsonObj


class Produto(models.Model):
    marca_text = models.CharField(max_length=200,blank=True)
    numserie_text= models.CharField(max_length=200,blank=True)
    descricao_text = models.CharField(max_length=200)
    assistencias = models.ManyToManyField(Assistencia,related_name="assistencias",blank=True)

    def __str__(self):
        return self.descricao_text

class Pessoa(models.Model):
    nome_text = models.CharField(max_length=50,blank=True,null=True)
    telefone_text = models.IntegerField(blank=True,null=True)
    email_text = models.EmailField(blank=True,null=True)
    morada_text = models.CharField(max_length=50,blank=True,null=True)
    localidade_text = models.CharField(max_length=50,blank=True,null=True)
    codigo_postal_text = models.CharField(max_length=10,blank=True,null=True)
    assistencias = models.ManyToManyField(Assistencia,blank=True,null=True)

    def __str__(self):
        return self.nome_text

class Pedido(models.Model):
    cliente = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    pedido_text = models.CharField(max_length=200)
    valor = models.DecimalField(decimal_places=2,max_digits=5,blank=True)
    foto = models.FileField(blank=True)

    def __str__(self):
        return self.pedido_text
