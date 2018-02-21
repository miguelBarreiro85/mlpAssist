from django import forms
from django.forms import ModelForm
from assistencias.models import Assistencia, Pessoa, Produto

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

class AssistenciaForm(ModelForm):
    class Meta:
        model = Assistencia
        fields = ['produto','funcionario','cliente','topico_text',
                  'descricao_text','pub_date','valor','pago_bol']

class PesquisaClienteForm(ModelForm):
    class Meta:
        model = Pessoa
        fields = ['id','nome_text','telefone_text','email_text','morada_text',
                  'localidade_text','codigo_postal_text']

class PesquisaProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields = ['marca_text','numserie_text','descricao_text']


class pesquisaAssistenciaForm(forms.Form):
    pub_date_init = forms.DateField(required=False)
    pub_date_fim = forms.DateField(required=False)
    produto = forms.IntegerField(label="Id Produto",required=False)
    funcionario = forms.CharField(label='Nome Funcionario', max_length=100,required=False)
    cliente = forms.CharField(label="Nome Cliente", max_length=100,required=False)
    topico_text = forms.CharField(label="Topico", max_length=100,required=False)
    descricao_text = forms.CharField(label="descrição texto", widget=forms.Textarea,required=False)
    valor = forms.DecimalField(required=False)
    pago_bol = forms.BooleanField(required=False)



class pesquisaNome(forms.Form):
    cliente = forms.CharField(label="Nome Cliente", max_length=100,required=False)
