# Plano (5 minutos). 
# Dominio: Sistema ecommerce
# *Classes: 1) Categoria: __nome (string) | 2) Produto: __nome (string), __preco (float), __categoria (objeto Categoria)
# *Validações pretendidas: 1) O preço do produto deve ser sempre maior que zero. | 2) Os nomes (Categoria e Produto) não podem ser 
# nulos ou espaços vazios/branco.
# *Tempo previsto: 50 minutos (15m implementação inicial, 25m validações/encapsulamento, 10m testes).
# 

# Mão na massa (50 minutos).

class Categoria:
    #Criterio 3 e 4: construtor validando atraves do setter possuindo um parametro padrão para simular sobrecarga
    def __init__(self, nome="Categoria Padrao"): 
        self.nome = nome
        
    @property # decorador property
    def nome(self):
        return self.__nome
    
    @nome.setter #decorador setter
    def nome(self, valor):
        if not valor or not str(valor).strip():
            # evanta o erro quando é vazio
            raise ValueError("Erro: o nome da categoria nao pode ser vazio.")
        #Criterio 2: Atributo protegido
        self.__nome = str(valor).strip()
            
    def __str__(self):
        return self.nome
    


class Produto:
    #Criterio 4: duas formas de criacao viabilizadas por paramentros padrao 
    def __init__(self, nome, preco, categoria=None): 
        # Criterio 3: O construtor exige o indispensavel e repassa para os setters 
        self.nome = nome
        self.preco = preco
        
        if categoria is None:
            self.categoria = Categoria("Sem Categoria")
        else:
            self.categoria = categoria
            
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, valor):
        if not valor or not str(valor).strip():
            raise ValueError("Erro: o nome do produto nao pode ser vazio.")
        self.__nome = str(valor).strip()
        
    @property
    def preco(self):
        return self.__preco
        
    @preco.setter
    def preco(self, valor):
        # Criterio 5: Segunda regra de validacao
        if not isinstance(valor, (int, float)) or valor <= 0:
            # f serve para formatar a string corretamente
            raise ValueError(f"Erro: O preco deve ser maior que zero. Recebido: {valor}")
        self.__preco = float(valor)

    @property
    def categoria(self):
        return self.__categoria

    @categoria.setter
    def categoria(self, valor):
        # Criterio 1: Produto utiliza internamente um objeto Categoria
        if not isinstance(valor, Categoria):
            raise TypeError("Erro: A categoria deve ser uma instancia da classe Categoria.")
        self.__categoria = valor

    def __str__(self):
        return f"Produto: {self.nome} | Preco: R$ {self.preco:.2f} | Categoria: {self.categoria.nome}"

#Criterio 6
if __name__ == "__main__":
    print("Atividade em Sala -Fundamentos de OO")
    #criação valida demonstrando as duas formas, com e sem paramentro default
    try:
        print("\n 1. Testando criacoes validas:")
        cat_eletronicos = Categoria("Eletronicos")
        
        prod1 = Produto("Notebook Dell", 4500.00, cat_eletronicos)
        print(f"Forma A -> {prod1}") 
        
        prod2 = Produto("Cabo HDMI", 45.90)
        print(f"Forma B -> {prod2}") 
    except Exception as e:
        print(f"Falha inesperada: {e}") 
    #demonstracao de recusa (Nome vazio)
    try:
        print("\n 2. Testando recusa (Nome vazio):")
        prod_invalido1 = Produto(" ", 100.00)
    except ValueError as e:
        print(f"Bloqueado pelo setter com sucesso: {e}") 
    #demonstracao de recusa (Preco negativo)
    try:
        print("\n>> 3. Testando recusa (Preco invalido):")
        prod_invalido2 = Produto("Mouse", -50.00, cat_eletronicos)
    except ValueError as e:
        print(f"Bloqueado pelo setter com sucesso: {e}") 
        
        
        
        
        
# Passo 3: AUTOAVALIACAO
#* Criterios que foram atingidos: Os criterios 1 a 6 foram atingidos corretamente, foram realizadas
#  encapsulamento, validação centralizada e demonstração completa no console.
#* Trecho mais trabalhoso: Entender que, dentro do __init__, a atribuição 
 # precisa ser self.atributo (acionando o setter) e não self.__atributo (o 
  #que pularia a validação e comprometeria o objeto).
#* Uso de IA: Sugestão de temas, utilização correta do f-string corretamente que eu havia esquecido e o comando raise que serve para lançar ou forçar uma excecao de (erro) manualmente
# durante a execução do programa