from rest_framework import serializers
from django.db.models import Avg # class para calcular média

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
    #  a validação deve seguir este padrão
    # validate_nome_do_campo_aqui
    def validate_avaliacao(self, valor):
        if valor in range(1, 6): # 1, 2, 3, 4, 5
            return valor
        raise serializers.ValidationError('A avaliação precisa ser um inteiro entre 1 e 5')


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

    media_avaliacoes = serializers.SerializerMethodField()

    class Meta:
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo',
            'avaliacoes',
            'media_avaliacoes'
        )

    # Aqui o padrão tem que ser
    # get_nome_do_campo_aqui
    def get_media_avaliacoes(self, obj):
        media = obj.avaliacoes.aggregate(Avg('avaliacao')).get('avaliacao_avg')

        if media is None:
            return 0
        return round(media * 2) / 2