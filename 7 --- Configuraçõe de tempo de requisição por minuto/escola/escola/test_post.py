import  requests
from django.conf.urls import url

headers ={'Authorization': 'Token 38f0ff3cccfb85b3ee4eacf85e8e47e08b50754b'}

url_base_cursos= 'http://localhost:8081/api/v2/cursos/'
url_base_avaliacoes= 'http://localhost:8081/api/v2/avaliacoes/'

novo_curso ={
    "titulo":"Gerência Ágil de projetos com Scrum",
    "url":"http://wwwgetuniversity.com.br/scrum2"
}

resultado = requests.post(url=url_base_cursos, headers=headers, data=novo_curso)

# testando o códiogo de status HTTP 201
assert resultado.status_code == 201

# titulo d curso criado é o mesmo d informado
assert resultado.json()['titulo'] == novo_curso['titulo']