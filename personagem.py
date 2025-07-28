#classe base para todas as outras
class Personagem:
    #*** comentario Grazyele: Falta documentação, type hints(inteiro, float, string etc.) e validação de tipos. Isso ajuda a IDE a entender melhor o código e evitar erros. ***
    def __init__ (self, nome, vida, ataque, defesa):
        self._nome = nome
        self._vida = vida
        self._vida_maxima = vida
        self._ataque = ataque
        self._defesa = defesa

    # atributos encapsulados
    @property
    def nome(self):
        return self._nome
    
    @property
    def vida(self):
        return self._vida
    
    @property
    def ataque(self):
        return self._ataque
    
    @property
    def defesa(self):
        return self._defesa
    
    # lógica de receber dano
    def receber_dano(self, quantidade_dano): 
        dano_real = quantidade_dano - self._defesa # *** Comentario Grazyele: isso é um bug, pois está subtraindo a defesa novamente! Ele já vem calculado das subclasses ***
        if dano_real < 0:
            dano_real = 0

    # Impedir a vida de ficar negativa
        self._vida -= dano_real
        if self._vida < 0:
            self._vida = 0

    #***Comentario Grazyele: codigos comentados deve ser removidos se não for mais utilizado, se tiver inseguro versiona ele, criando uma branch nova, mas na branch principal deve ser evitado.   *******

    # lógica de curar o personagem (não implementada)
    # def curar(self, quantidade_cura):
    #     self._vida += quantidade_cura
    #     if self._vida > self._vida_maxima:
    #         self._vida = self._vida_maxima

    #     print (f"{self._nome} curou {quantidade_cura}. Vida atual: {self._vida}")

    # retorna personagem vivo se vida estiver acima de zero
    def esta_vivo(self):
        return self._vida > 0
    
    # base da função atacar que é implementada individualmente em cada classe
    def atacar(self, outro):
        raise NotImplementedError("A subclasse precisa implementar o método atacar()")
    
    # exibir status do personagem
    def status (self):
        print(f"\n{self._nome} - Vida: {self._vida}, Ataque: {self._ataque}, Defesa: {self._defesa}")

    # retorna personagem morto se a vida estiver zerada
    def morreu(self): # ***Comentario Grazyele: Redundância, Não é necessário, pois já tem a função esta_vivo() que retorna o inverso dela.***
        return self._vida <= 0 
    
    
