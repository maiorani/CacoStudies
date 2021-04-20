import requests
def pega_rua(cep):
    "https://viacep.com.br/ws/01001000/json/"
    #colocar o cep dentro da url
    url = f"https://viacep.com.br/ws/{cep}/json/"
    req = requests.get(url)
    dic = req.json()
    return dic['logradouro']

cep = input('Digite seu CEP: ')
print (pega_rua(cep))