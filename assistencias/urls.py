from django.urls import path

from . import views
app_name = 'assistencias'
urlpatterns = [
    # ex: /polls/
    path('', views.IndexView.as_view(), name='index'),
    path('<int:assistencia_id>/detalhe', views.detalhe, name='detalhe'),
    path('<int:assistencia_id>/atualizar', views.atualizar, name='atualizar'),
    path('pesquisarAssistencia', views.pesquisarAssistencia, name='pesquisa_assistencia'),
    path('pesquisarCliente', views.pesquisarCliente, name='pesquisa_cliente'),
    path('pesquisarProduto', views.pesquisarProduto, name='pesquisa_produto'),

    path('<int:cliente_id>/atualizarCliente', views.atualizarCliente, name='atualiza_cliente'),
    path('<int:produto_id>/atualizarProduto', views.atualizarProduto, name='atualiza_produto'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
