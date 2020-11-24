import  requests

headers ={'Authorization': 'Token 38f0ff3cccfb85b3ee4eacf85e8e47e08b50754b'}

url_base_cursos= 'http://localhost:8081/api/v2/cursos/'
url_base_avaliacoes= 'http://localhost:8081/api/v2/avaliacoes/'

resultado = requests.get(url=url_base_cursos, headers=headers)

print(resultado.json())

#  O QUE TESTAR ???

# testando se o endpoit está correto
assert resultado.status_code == 200

# Testando a quantidade de registros

# assert resultado.json()['count'] == 3


# Tesntado  se o título do primeiro curso esta correto
