import requests

def test_status_and_data():
    headers = {
    'Accept': '*/*',
    'User-Agent': 'request',
    }

    url = "http://dummy.restapiexample.com/api/v1/employees"

    resposta = requests.get(url, headers = headers)
    resposta_dict = resposta.json()

    status = resposta_dict['status']
    tamanho = len(resposta_dict['data'])

    assert ((status == 'sucess') and (tamanho > 0))