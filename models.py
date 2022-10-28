from django.db import models


class Cliente(models.Model):
    id = models.BigAutoField(primary_key=True)
    cliente = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'extrato_clients'
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'


class ResumoExtrato(models.Model):
    id = models.BigAutoField(primary_key=True)
    saldoAnterior = models.DecimalField(max_digits=22, decimal_places=2, blank=True, null=True)
    saldoAtual = models.DecimalField(max_digits=22, decimal_places=2, blank=True, null=True)
    saldoBloqueado = models.DecimalField(max_digits=22, decimal_places=2, blank=True, null=True)
    saldoDisponivel = models.DecimalField(max_digits=22, decimal_places=2, blank=True, null=True)
    valorBloqueado = models.DecimalField(max_digits=22, decimal_places=2, blank=True, null=True)
    limite = models.DecimalField(max_digits=22, decimal_places=2, blank=True, null=True)
    dia_consulta = models.CharField(max_length=150, blank=True, null=True)
    intervalo_consulta = models.CharField(max_length=150, blank=True, null=True)
    quantidade_itens = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'extrato_summary'
        verbose_name = 'Resumo do Extrato'
        verbose_name_plural = 'Resumo dos Extratos'


class Item(models.Model):
    id = models.BigAutoField(primary_key=True)
    natureza = models.CharField(max_length=10, blank=True, null=True)
    dataLancto = models.DateTimeField(blank=True, null=True)
    nrDocumento = models.CharField(max_length=150, blank=True, null=True)
    cpfCnpj = models.CharField(max_length=14, blank=True, null=True)
    nomeContraparte = models.CharField(max_length=50, blank=True, null=True)
    agenciaContraparte = models.CharField(max_length=20, blank=True, null=True)
    contaContraparte = models.CharField(max_length=20, blank=True, null=True)
    valor = models.DecimalField(max_digits=22, decimal_places=2, blank=True, null=True)
    saldoAtual = models.DecimalField(max_digits=22, decimal_places=2, blank=True, null=True)
    saldoAnterior = models.DecimalField(max_digits=22, decimal_places=2, blank=True, null=True)
    tipoOperacao = models.CharField(max_length=50, blank=True, null=True)
    # ? VALORES PEGOS DO HISTÓRICO NO JSON
    codigo = models.CharField(max_length=50, blank=True, null=True)
    descricao = models.CharField(max_length=150, blank=True, null=True)
    complemento = models.TextField(blank=True, null=True)
    categoria = models.IntegerField(blank=True, null=True)
    dia_consulta = models.CharField(max_length=150, blank=True, null=True)
    intervalo_consulta = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'extrato_itens'
        verbose_name = 'Item Extrato'
        verbose_name_plural = 'Itens Extratos'


# class Controle(models.Model):
#     dataInicio = models.DateField()
#     dataFinal = models.DateField()
#     controleItens = models.BigIntegerField()
#
#     class Meta:
#         managed = True
#         db_table = 'extrato_controle'
#         verbose_name = 'Controle de Inserções'
