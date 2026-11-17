# core/admin.py
from django.contrib import admin
from .models import Produto

# Ativação do modelo Produto dentro da retaguarda administrativa
admin.site.register(Produto)