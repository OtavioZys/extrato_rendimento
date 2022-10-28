import logging

from django.utils.datetime_safe import datetime
from future.backports.datetime import timedelta

from apps.extrato.getters import get_extrato
from apps.extrato.models import Cliente, Controle, Item, ResumoExtrato


def tsk_extrato_rendimento():
    listas = get_extrato()
    client_list = listas['value']
    cliente = client_list['cliente']
    itens_list = listas['value']['itens']
    resumo_list = listas['value']['resumo']

    Cliente.objects.using('adm_int').update_or_create(cliente=cliente)

    hoje = datetime.now()
    ontem = hoje - timedelta(days=1)

    Controle.objects.using('adm_int').update_or_create(
        dataInicio=ontem,
        dataFinal=ontem,
        controleItens=len(itens_list)
    )

    try:
        ResumoExtrato.objects.using('adm_int').update_or_create(
            saldoAnterior=resumo_list['saldoAnterior'],
            saldoAtual=resumo_list["saldoAnterior"],
            saldoBloqueado=resumo_list['saldoBloqueado'],
            saldoDisponivel=resumo_list['saldoDisponivel'],
            valorBloqueado=resumo_list['valorBloqueado'],
            limite=resumo_list['limite'])
    except Exception as errod:
        print('-' * 100)
        logging.log(1, errod)
        print('-' * 100)

    for itens in itens_list:
        try:
            Item.objects.using('adm_int').update_or_create(
                natureza=itens['natureza'],
                dataLancto=itens['dataLancto'],
                nrDocumento=itens['nrDocumento'],
                cpfCnpj=itens['cpfCnpj'],
                nomeContraparte=itens['nomeContraparte'],
                agenciaContraparte=itens['agenciaContraparte'],
                contaContraparte=itens['contaContraparte'],
                valor=itens['valor'],
                saldoAtual=itens['saldoAtual'],
                tipoOperacao=itens['tipoOperacao'],
                codigo=itens['historico']['codigo'],
                descricao=itens['historico']['descricao'],
                complemento=itens['historico']['complemento'],
                categoria=itens['historico']['categoria'])
        except Exception as errod:
            print('-' * 100)
            logging.log(1, errod)
            print('-' * 100)
            continue
