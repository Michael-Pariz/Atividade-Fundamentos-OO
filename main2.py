
# Plano (5 minutos). 
# Dominio: Sistema de Jogos (Personagens e Guildas)
# *Classes: 1) Guilda: __nome (string) | 2) Personagem: __nome (string), __nivel (int), __guilda (objeto Guilda)
# *Validações pretendidas: 1) O nivel do personagem deve ser sempre maior que zero. | 2) Os nomes (Guilda e Personagem) não podem ser 
# nulos ou espaços vazios/branco.
# *Tempo previsto: 50 minutos (15m implementação inicial, 25m validações/encapsulamento, 10m testes).
# 

# Mão na massa (50 minutos).

class Guilda:
    # Criterio 3 e 4: construtor validando atraves do setter possuindo um parametro padrão para simular sobrecarga
    def __init__(self, nome="Sem Guilda"): 
        self.nome = nome
        
    @property # decorador property
    def nome(self):
        return self.__nome
    
    @nome.setter #decorador setter
    def nome(self, valor):
        if not valor or not str(valor).strip():
            # levanta o erro quando é vazio
            raise ValueError("Erro: o nome da guilda nao pode ser vazio.")
        # Criterio 2: Atributo protegido
        self.__nome = str(valor).strip()
            
    def __str__(self):
        return self.nome


class Personagem:
    # Criterio 4: duas formas de criacao viabilizadas por paramentros padrao 
    def __init__(self, nome, nivel, guilda=None): 
        # Criterio 3: O construtor exige o indispensavel e repassa para os setters 
        self.nome = nome
        self.nivel = nivel
        
        if guilda is None:
            self.guilda = Guilda("Aventureiros Independentes")
        else:
            self.guilda = guilda
            
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, valor):
        if not valor or not str(valor).strip():
            raise ValueError("Erro: o nome do personagem nao pode ser vazio.")
        self.__nome = str(valor).strip()
        
    @property
    def nivel(self):
        return self.__nivel
        
    @nivel.setter
    def nivel(self, valor):
        # Criterio 5: Segunda regra de validacao (Nivel deve ser int e maior que 0)
        if not isinstance(valor, int) or valor <= 0:
            # f serve para formatar a string corretamente
            raise ValueError(f"Erro: O nivel deve ser maior que zero. Recebido: {valor}")
        self.__nivel = valor

    @property
    def guilda(self):
        return self.__guilda

    @guilda.setter
    def guilda(self, valor):
        # Criterio 1: Personagem utiliza internamente um objeto Guilda
        if not isinstance(valor, Guilda):
            raise TypeError("Erro: A guilda deve ser uma instancia da classe Guilda.")
        self.__guilda = valor

    def __str__(self):
        return f"Personagem: {self.nome} | Nivel: {self.nivel} | Guilda: {self.guilda.nome}"

# Criterio 6
if __name__ == "__main__":
    print("Atividade em Sala - Fundamentos de OO")
    
    # criação valida demonstrando as duas formas, com e sem paramentro default
    try:
        print("\n>> 1. Testando criacoes validas:")
        guilda_principal = Guilda("Inevitável")
        
        pers1 = Personagem("Guerreiro Místico", 45, guilda_principal)
        print(f"Forma A -> {pers1}") 
        
        pers2 = Personagem("Mago Iniciante", 1)
        print(f"Forma B -> {pers2}") 
    except Exception as e:
        print(f"Falha inesperada: {e}") 
        
    # demonstracao de recusa (Nome vazio)
    try:
        print("\n>> 2. Testando recusa (Nome vazio):")
        pers_invalido1 = Personagem(" ", 10)
    except ValueError as e:
        print(f"Bloqueado pelo setter com sucesso: {e}") 
        
    # demonstracao de recusa (Nivel zero ou negativo)
    try:
        print("\n>> 3. Testando recusa (Nivel invalido):")
        pers_invalido2 = Personagem("Arqueiro das Sombras", -5, guilda_principal)
    except ValueError as e:
        print(f"Bloqueado pelo setter com sucesso: {e}") 
        
        
# Passo 3: AUTOAVALIACAO
#* Criterios que foram atingidos: Os criterios 1 a 6 foram atingidos corretamente, foram realizadas
#  encapsulamento, validação centralizada e demonstração completa no console.
#* Trecho mais trabalhoso: Entender que, dentro do __init__, a atribuição 
#  precisa ser self.atributo (acionando o setter) e não self.__atributo (o 
#  que pularia a validação e comprometeria o objeto).
#* Uso de IA: Sugestão de temas, utilização correta do f-string corretamente que eu havia esquecido e o comando raise que serve para lançar ou forçar uma excecao de (erro) manualmente
#  durante a execução do programa
