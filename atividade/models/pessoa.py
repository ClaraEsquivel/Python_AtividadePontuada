class Pessoa:
    def __init__(self, nome:str, idade:int) -> None:
        if idade < 0:
            raise ValueError("Idade inválida! A idade não pode ser negativa.")
        self.nome = nome 
        self.idade = idade

    def __str__(self) -> str:
        return(
            f"\nNome: {self.nome}"
            f"\nIdade: {self.idade}"
        )    