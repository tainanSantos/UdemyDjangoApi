import  requests
from django.conf.urls import url

headers ={'Authorization': 'Token 38f0ff3cccfb85b3ee4eacf85e8e47e08b50754b'}
url_base_cursos= 'http://localhost:8081/api/v2/cursos/'
url_base_avaliacoes= 'http://localhost:8081/api/v2/avaliacoes/'


curso_atualido ={
    "titulo": "Novo Cusro de Scrum 3",
    "url":"http://wwwgetuniversity.com.br/scrum5"
}

resultado = requests.put(url=f'{url_base_cursos}1/', headers=headers, data=curso_atualido)

# Testado o código de status HTTP
assert resultado.status_code == 200

# Testando o título
assert resultado.json()['titulo'] ==curso_atualido['titulo']
