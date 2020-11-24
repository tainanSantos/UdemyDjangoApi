import requests
import jsonpath

# jsonpath
#   vai sempre te dar uam lista de dicionários


avaliacoes = requests.get('http://localhost:8081/api/v2/avaliacoes/')
# resultados = jsonpath.jsonpath(avaliacoes.json(), 'results')
#
# print(resultados)

# resultados = jsonpath.jsonpath(avaliacoes.json(), 'results[0]')
#
# print(resultados)

# resultados = jsonpath.jsonpath(avaliacoes.json(), 'results[0].nome')
#
# print(resultados)
#
# resultados = jsonpath.jsonpath(avaliacoes.json(), 'results[0].avaliacao')
#
# print(resultados)



# Todos os nomes da pessoas qye avaliaram o curso

# resultados = jsonpath.jsonpath(avaliacoes.json(), 'results[*].nome')
# print(resultados)

# resultados = jsonpath.jsonpath(avaliacoes.json(), 'results[*].avaliacao')
# print(resultados)


