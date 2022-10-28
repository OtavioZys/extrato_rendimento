from datetime import datetime, timedelta
import requests
from integracoes_card.settings import DOMINIO_APIRENDIMENTO, RENDIMENTO_ACCESSKEY, RENDIMENTO_AGENCIA, \
    RENDIMENTO_CONTACORRENTE, \
    RENDIMENTO_USER, RENDIMENTO_ENCODED_AUTH


def get_token():
    urllogin = f"{DOMINIO_APIRENDIMENTO}oauth/access-token?grant_type=client_credentials"
    payload = 'grant-type=client_credentials'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': RENDIMENTO_ENCODED_AUTH
    }

    response = requests.request("POST", urllogin, headers=headers, data=payload)

    token = response.json()
    token = token['access_token']
    return token


def get_extrato():
    hoje = datetime.now()
    ontem = hoje - timedelta(days=1)
    tzsp = ontem.astimezone()
    dtbusca1 = tzsp.strftime('%m-%d-%Y')
    dtbusca2 = hoje.strftime('%m-%d-%Y')
    print(f'data da busca: {dtbusca1}')
    url = f'{DOMINIO_APIRENDIMENTO}pagamentosIB/api/v1/ContasCorrentes/{RENDIMENTO_AGENCIA}/{RENDIMENTO_CONTACORRENTE}'
    urlparm = f'{url}/Extrato/Obter?dataInicio={dtbusca1}&dataFinal={dtbusca2}'
    dtfiltro = tzsp.strftime('%m-%d-%Y')
    token = get_token()
    headers = {
        'ChaveAcesso': RENDIMENTO_ACCESSKEY,
        'access_token': token,
        'Content-Type': 'application/json',
        'dataInicio': dtbusca1,
        'dataFinal': dtbusca2,
        'client_id': RENDIMENTO_USER,
        'Authorization': RENDIMENTO_ENCODED_AUTH
    }

    response = requests.request("GET", urlparm, headers=headers)
    if response.status_code == '403':
        return []
    else:
        return response.json()


def get_data():
    # onti = datetime.today() - timedelta(days=3)
    hoje = datetime.now()
    filtro = hoje - timedelta(days=1)
    tzsp = filtro.astimezone()
    dtbusca1 = tzsp.strftime('%d-%m-%Y')

    # iniciomes = timezone.datetime(int(ano), int(mes), 1, tzinfo=pytz.UTC).date()
    # hoje = datetime.now()
    # ontem = hoje - timedelta(days=1)
    # tzsp = ontem.astimezone(fuso)
    # ontem_str = tzsp.strftime('%m-%d-%Y')
    # print(ontem_str)
    return dtbusca1
