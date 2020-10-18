from rest_framework import serializers
from .models import Curso, Avaliacao

class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        # o email não vai ser apresentado quando alguem consultar as avaliações
        # o email vai ser exigido apenas quando a gente for fazer cadastro
        extra_kwargs = {
            'email': {'write_only': True}
        }
        model = Avaliacao
        fields = (
            'id',
            'curso',
            'nome',
            'email',
            'comentario',
            'avaliacao',
            'criacao',
            'ativo'
        )

# avaliacoes = AvaliacaoSerializer(many=True, read_only=True)
# o dado avaliacoes é apenas de leitura e apenas no get a gente vai ter acesso a todas as avaliações
class CursoSerializer(serializers.ModelSerializer):
    # Abordagem 1 (PARA POUCOS DADOS)
    # Nested Relationship
    # avaliacoes = AvaliacaoSerializer(many=True, read_only=True)

    # Abordagem 2 (É A IDEAL)
    # Hyperlinked Related Field
    # avaliacoes = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='avaliacao-detail'
    # )

    # Abordagem 3 (PARA MILHARES DE DADOS)
    # Primary Key Related Field
    avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)



    class Meta:
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo',
            'avaliacoes'
        )