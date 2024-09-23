import pytest
from atividade.models.pessoa import Pessoa

@pytest.fixture
def pessoa_valida():
    pessoa = Pessoa ("Clara", 21)
    return pessoa

def test_pessoa_alternar_nome_valido(pessoa_valida):
    #Alternando o nome da pessoa "Clara" para "Vitoria"
    pessoa_valida.nome = "Vitoria"
    assert pessoa_valida.nome == "Vitoria"

def test_pessoa_nome_valido(pessoa_valida):
    assert pessoa_valida.nome == "Clara"

def test_pessoa_idade_valido(pessoa_valida):
    assert pessoa_valida.idade == 21

def test_pessoa_idade_invalido_retorna_mensagem_excecao(pessoa_valida):
    with pytest.raises(ValueError, match="Idade inválida! A idade não pode ser negativa."):
        Pessoa("Clara", -21)




