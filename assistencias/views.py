from django.core import serializers
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect, JsonResponse
from .models import Assistencia, Produto, Pedido, Pessoa
from django.views import generic
from django.db.models import Q
from .forms import NameForm, AssistenciaForm, \
    pesquisaAssistenciaForm, PesquisaClienteForm, PesquisaProdutoForm
from datetime import datetime, date
import logging, json

logger=logging.getLogger(__name__)
# Create your views here.

class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'latest_assistencia_list'

    def get_queryset(self):
        """Return the last five published assistencias."""
        return Assistencia.objects.order_by('-pub_date')[:50]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = pesquisaAssistenciaForm()
        context['formCliente'] = PesquisaClienteForm()
        context['formProduto'] = PesquisaProdutoForm()
        return context

def detail(request, question_id):
    return render(request,'assistencias/index.html')

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def assistencias(request):
    return render(request,'assistencias.html',{
        'entries':Assistencia.objects.all()
    })

def detalhe(request, assistencia_id):
    assistencia = Assistencia.objects.get(pk=assistencia_id)
    form = AssistenciaForm(instance=assistencia)
    if form.is_valid():
        logger.error("VALIDO")
        return render(request,'detalhes.html',{
        'assistencia':assistencia,
        'form':form})
    else:
        return render(request,'detalhes.html',{
        'assistencia':assistencia,
        'form':form})

def atualizar(request, assistencia_id):
    if request.method == 'POST':
        assistencia = Assistencia.objects.get(pk=assistencia_id)
        form = AssistenciaForm(request.POST,instance=assistencia)
        form.save()
        return HttpResponse("THANKS")
    else:
        return HttpResponse("NOT VALID")

def pesquisaPessoa(request):
    body = request.POST
    assistencias = Assistencia.objects.filter(cliente__nome_text__contains=body["nome"])
    arrayAssistencias=[]
    for assistencia in assistencias:
        object = assistencia.sendAssistencia
        arrayAssistencias.append(object)
    return JsonResponse(arrayAssistencias,safe=False)

def pesquisarAssistencia(request):
    requestForm = pesquisaAssistenciaForm(request.POST)
    try:
        dataInit = datetime.strptime(requestForm['pub_date_init'].value(),'%Y-%m-%d')
    except ValueError:
        dataInit = date(1990,1,1)

    try:
        dataFim = datetime.strptime(requestForm['pub_date_fim'].value(),'%Y-%m-%d')
    except ValueError:
        dataFim = date(2100,1,1)

    assistencias = Assistencia.objects.filter(cliente__nome_text__icontains=requestForm['cliente'].value(),
                                              funcionario__nome_text__icontains=requestForm['funcionario'].value(),
                                              topico_text__icontains=requestForm['topico_text'].value(),
                                              descricao_text__icontains=requestForm['descricao_text'].value(),
                                              valor__icontains=requestForm['valor'].value(),
                                              pub_date__gte=dataInit,
                                              pub_date__lte=dataFim
                                              )

    logger.error(assistencias)
    return render(request,'pesquisaAssistencias.html',{'assistencias':assistencias, 'formAssistencia':pesquisaAssistenciaForm(),
                                                       'formCliente':PesquisaClienteForm,'formProduto':PesquisaProdutoForm})

def pesquisarCliente(request):
    if 'novoCliente' in request.POST:
        if request.POST['nome_text']=="":
            return HttpResponse("Nome Invalido")
        else:
            form = PesquisaClienteForm(request.POST)
            form.save()
            return HttpResponse("Cliente Adicionado com sucesso")
    else:
        requestForm = PesquisaClienteForm(request.POST)
        clientes = Pessoa.objects.filter(nome_text__icontains=requestForm['nome_text'].value())
        return render(request,'pesquisaClientes.html',{'clientes':clientes,
                      'formAssistencia':pesquisaAssistenciaForm(),'formCliente':PesquisaClienteForm(),
                        'formProduto':PesquisaProdutoForm()})

def pesquisarProduto(request):
    requestForm = PesquisaProdutoForm(request.POST)
    produtos = Produto.objects.filter(descricao_text__icontains=requestForm['descricao_text'].value())
    return render(request,'pesquisaProdutos.html',{'produtos':produtos,
                  'formAssistencia':pesquisaAssistenciaForm(),'formCliente':PesquisaClienteForm(),
                    'formProduto':PesquisaProdutoForm()})

def atualizarCliente(request,cliente_id):
    if request.method=="GET":
        cliente=Pessoa.objects.get(pk=cliente_id)
        form = PesquisaClienteForm(instance=cliente)
        logger.error(form)
        return render(request,'atualizarCliente.html',{'form':form, 'cliente':cliente, 'formAssistencia':AssistenciaForm()})
    elif request.method=="POST":
        cliente = Pessoa.objects.get(pk=cliente_id)
        form = PesquisaClienteForm(request.POST,instance=cliente)
        form.save()
        return HttpResponse("Cliente Salvo")

def atualizarProduto(request,produto_id):
    if request.method=="GET":
        produto=Produto.objects.get(pk=produto_id)
        form = PesquisaProdutoForm(instance=produto)
        logger.error(form)
        return render(request,'atualizarProduto.html',{'form':form, 'produto':produto})
    elif request.method=="POST":
        produto = Produto.objects.get(pk=produto_id)
        form = PesquisaProdutoForm(request.POST,instance=produto)
        form.save()
        return HttpResponse("Produto Salvo")
