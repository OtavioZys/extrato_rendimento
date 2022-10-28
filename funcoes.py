from apps.extrato.models import ResumoExtrato, Item
from apps.extrato.getters import get_extrato, get_data, get_token
from datetime import datetime


def get_resumo():
    lista_response = get_extrato()
    lista_value = dict(lista_response['value'])
    resumo = dict(lista_value['resumo'])
    hoje = datetime.now()
    hoje_str = hoje.strftime('%d-%m-%Y')
    consulta = get_data()
    intervalo_consulta = str(f"{consulta} à {hoje_str}")
    quantidade_itens = len(lista_value['itens'])
    dicionario_resumo = {
        'saldoAnterior': resumo['saldoAnterior'],
        'saldoAtual': resumo['saldoAtual'],
        'saldoBloqueado': resumo['saldoBloqueado'],
        'saldoDisponivel': resumo['saldoDisponivel'],
        'valorBloqueado': resumo['valorBloqueado'],
        'limite': resumo['limite'],
        'dia_consulta': hoje_str,
        'intervalo_consulta': intervalo_consulta,
        'quantidade_itens': quantidade_itens
    }
    return dicionario_resumo


def get_itens():
    lista_response = get_extrato()
    lista_value = dict(lista_response['value'])
    hoje = datetime.now()
    hoje_str = hoje.strftime('%d-%m-%Y')
    consulta = get_data()
    intervalo_consulta = str(f"{consulta} à {hoje_str}")
    # controller_while = 0
    # itens_list = []
    # while controller_while < quantidade_itens:
    #     item = dict(lista_value['itens'][controller_while])
    #     itens_list.append(item)
    #     controller_while = controller_while + 1
    # controller_for = 0
    lista_dicionarios = []
    for items in lista_value['itens']:
        dicionario = {
            'natureza': items['natureza'],
            'dataLancto': items['dataLancto'],
            'nrDocumento': items['nrDocumento'],
            'cpfCnpj': items['cpfCnpj'],
            'nomeContraparte': items['nomeContraparte'],
            'agenciaContraparte': items['agenciaContraparte'],
            'contaContraparte': items['contaContraparte'],
            'valor': items['valor'],
            'saldoAtual': items['saldoAtual'],
            'saldoAnterior': items['saldoAnterior'],
            'tipoOperacao': items['tipoOperacao'],
            'codigo': items['historico']['codigo'],
            'descricao': items['historico']['descricao'],
            'complemento': items['historico']['complemento'],
            'categoria': items['historico']['categoria'],
            'dia_consulta': hoje_str,
            'intervalo_consulta': intervalo_consulta
        }
        lista_dicionarios.append(dicionario)
    print(len(lista_dicionarios))
    return lista_dicionarios
