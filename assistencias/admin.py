from django.contrib import admin
from .models import Assistencia, Produto, Pessoa, Pedido

admin.site.register(Assistencia)
admin.site.register(Produto)
admin.site.register(Pessoa)
admin.site.register(Pedido)
# Register your models here.
