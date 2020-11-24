import  requests

headers ={'Authorization': 'Token 38f0ff3cccfb85b3ee4eacf85e8e47e08b50754b'}
url_base_cursos= 'http://localhost:8081/api/v2/cursos/'
url_base_avaliacoes= 'http://localhost:8081/api/v2/avaliacoes/'


resultado =  requests.delete(url=f'{url_base_cursos}1/', headers=headers)

# testando o cógio http
assert resultado.status_code == 204

# testando se o tamanho do conteúdo retornado é 0
assert  len(resultado.text) == 0
