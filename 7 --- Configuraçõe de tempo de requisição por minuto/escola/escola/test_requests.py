import  requests

#GET AVALIAÇÕES

# avaliacoes = requests.get('http://localhost:8081/api/v2/avaliacoes/')

# acessando o código de status http
# print(avaliacoes.status_code)

# Acessando os dados da resposat

# print(avaliacoes.json())
# print(type(avaliacoes.json()))


# Acessando a quantidade de resgustros

# print(avaliacoes.json()['count'])
# print(avaliacoes.json()['results'])



#GET AVALIAÇÃO

# avaliacao = requests.get('http://localhost:8081/api/v2/avaliacoes/2')
# print(avaliacao.json())



# get CUSROS

headers= {'Authorization':'Token 38f0ff3cccfb85b3ee4eacf85e8e47e08b50754b'}

cursos =  requests.get(url='http://localhost:8081/api/v2/cursos/', headers=headers)
print(cursos.status_code)
print(cursos.json())