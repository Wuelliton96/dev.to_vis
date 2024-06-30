import requests
from datetime import datetime
from django.db import models

## Cadastro de Inspetor
class Inspetor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    telefone = models.CharField(max_length=15)
    
    def __str__(self):
        return "{} - {}".format(self.nome, self.email)
    
    class Meta:
        verbose_name = 'Inspetor'
        verbose_name_plural = 'Inspetores'
        ordering = ['-id']

        
## Opções de Vistorias
class TipoDeVistoria(models.TextChoices):
    LANCHA = 'LANCHA','LANCHA'
    NAVIO = 'NAVIO','NAVIO'
    IATE = 'IATE','IATE'
    JET_SKI = 'JET_SKI','JET_SKI'
    VELEIRO = 'VELEIRO', 'VELEIRO'
    REBOQUE = 'REBOQUE', 'REBOQUE'

## Cadastro de Vistorias
class Vistoria(models.Model):
    codigo = models.CharField(max_length=100)
    tipo_item = models.CharField(max_length=100, choices=TipoDeVistoria.choices)
    cep = models.CharField(max_length=8, null=True,  default='00000000')
    rua = models.CharField(max_length=255, blank=True)
    bairro = models.CharField(max_length=255, blank=True)
    cidade = models.CharField(max_length=255, blank=True)
    estado = models.CharField(max_length=2, blank=True)
    numero = models.CharField(max_length=10, null=True)
    complemento = models.CharField(max_length=255, null=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    esta_vistoriado = models.BooleanField(default=False)
    
    def __str__(self):
        return "{} - {}".format(self.codigo, self.tipo_item)
    
    #def buscar_endereco_por_cep(self):
    #    api_url = f'https://viacep.com.br/ws/{self.cep}/json/'
    #    response = requests.get(api_url)
    #    if response.status_code == 200:
    #        data = response.json()
    #        self.rua = data.get('logradouro', '')
    #        self.bairro = data.get('bairro', '')
    #        self.cidade = data.get('localidade', '')
    #        self.estado = data.get('uf', '')
    #        self.save()
    
    class Meta:
        verbose_name = 'Vistoria'
        verbose_name_plural = 'Vistorias'
        ordering = ['-id']

## Cadastrar as Imagens do Barco
class VistoriaImage(models.Model):
    image = models.ImageField('Images',upload_to='images')
    vistoria = models.ForeignKey(Vistoria, related_name='vistoria_images', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.vistoria.codigo
    
## Registrar Locação
class RegistraVistoria(models.Model):
    vistoria = models.ForeignKey(Vistoria, on_delete=models.CASCADE, related_name='reg_vistoria')
    inspetor = models.ForeignKey(Inspetor, on_delete=models.CASCADE)
    dt_inicio = models.DateTimeField('Inicio')
    dt_fim = models.DateTimeField('Fim')
    criado_em = models.DateField(default=datetime.now, blank=True)
    
    def __str__(self):
        return "{} - {}".format(self.inspetor, self.vistoria)
    
    class Meta:
        verbose_name = 'Registrar Vistoria'
        verbose_name_plural = 'Registrar Vistorias'
        ordering = ['-id']