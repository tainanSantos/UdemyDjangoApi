import  requests

class TestCursos:
    headers = {'Authorization': 'Token 38f0ff3cccfb85b3ee4eacf85e8e47e08b50754b'}
    url_base_cursos = 'http://localhost:8081/api/v2/cursos/'
    url_base_avaliacoes = 'http://localhost:8081/api/v2/avaliacoes/'

    def test_get_cursos(self):
        cursos  = requests.get(url=self.url_base_cursos, headers= self.headers)
        assert cursos.status_code == 200

    def test_get_curso(self):
        cursos = requests.get(url=f'{self.url_base_cursos}2/', headers=self.headers)
        assert cursos.status_code == 200

    def test_post_curso(self):
        novo = {
            "titulo": "Novo Cusro de Scrum 3",
            "url": "http://wwwgetuniversity.com.br/scrum12"
        }
        resultado = requests.post(url=self.url_base_cursos, headers=self.headers, data=novo)
        assert resultado.status_code == 201

    def test_put_curso(self):
        atualizado = {
            "titulo": "Novo Cusro de Scrum 3",
            "url": "http://wwwgetuniversity.com.br/scrum13"
        }
        resposta = requests.put(url=f'{self.url_base_cursos}2/', headers=self.headers, data=atualizado)

        assert resposta.status_code==200
        assert resposta.json()['titulo'] == atualizado['titulo']

    def test_delete_curso(self):
        resposta = requests.put(url=f'{self.url_base_cursos}2/', headers=self.headers)

        assert resposta.status_code == 204 and len(resposta.text) == 0


