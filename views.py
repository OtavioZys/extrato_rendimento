import errno
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from datetime import datetime
from apps.extrato.getters import get_data
from apps.extrato.models import ResumoExtrato, Item
from apps.extrato.funcoes import get_resumo, get_itens


@login_required
def index_extrato(request):
    # Cliente.objects.using('adm_int').update_or_create(cliente=lista_value['cliente'])
    resumo = get_resumo()
    ResumoExtrato.objects.using('adm_int').create(
        saldoAnterior=resumo['saldoAnterior'],
        saldoAtual=resumo["saldoAnterior"],
        saldoBloqueado=resumo['saldoBloqueado'],
        saldoDisponivel=resumo['saldoDisponivel'],
        valorBloqueado=resumo['valorBloqueado'],
        limite=resumo['limite'],
        dia_consulta=resumo['dia_consulta'],
        intervalo_consulta=resumo['intervalo_consulta'],
        quantidade_itens=resumo['quantidade_itens'])
    itens = get_itens()
    for dado in itens:
        try:
            Item.objects.using('adm_int').create(
                natureza=dado['natureza'],
                dataLancto=dado['dataLancto'],
                nrDocumento=dado['nrDocumento'],
                cpfCnpj=dado['cpfCnpj'],
                nomeContraparte=dado['nomeContraparte'],
                agenciaContraparte=dado['agenciaContraparte'],
                contaContraparte=dado['contaContraparte'],
                valor=dado['valor'],
                saldoAtual=dado['saldoAtual'],
                saldoAnterior=dado['saldoAnterior'],
                tipoOperacao=dado['tipoOperacao'],
                codigo=dado['codigo'],
                descricao=dado['descricao'],
                complemento=dado['complemento'],
                categoria=dado['categoria'],
                dia_consulta=dado['dia_consulta'],
                intervalo_consulta=dado['intervalo_consulta'],)
        except Exception:
            print('erro')

    context = {
        'usuario': request.user.first_name,
        'segment': 'apps_extrato_dashboard',
        'itens_lista': '',
    }

    return render(request, 'extrato/index.html', context)
