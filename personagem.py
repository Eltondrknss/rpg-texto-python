class Personagem:
    def __init__ (self, nome, vida, ataque, defesa):
        self.nome = nome
        self.__vida = vida
        self.ataque = ataque
        self.defesa = defesa

    def valor_vida(self):
        return self.__vida
    
    def perder_vida(self, dano):
        self.__vida -= dano
        if self.__vida < 0:
            self.__vida = 0

    def atacar(self, outro):
        raise NotImplementedError("A subclasse precisa implementar o método atacar()")

    def status (self):
        print(f"\n{self.nome} - Vida: {self.__vida}, Ataque: {self.ataque}, Defesa: {self.defesa}")

    def esta_vivo(self):
        return not self.morreu()
    
    def morreu(self):
        return self.__vida <= 0
    
    