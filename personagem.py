class Personagem:
    def __init__ (self, nome, vida, ataque, defesa):
        self._nome = nome
        self._vida = vida
        self._vida_maxima = vida
        self._ataque = ataque
        self._defesa = defesa


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
    
    def receber_dano(self, quantidade_dano): 
        dano_real = quantidade_dano - self._defesa
        if dano_real < 0:
            dano_real = 0

    # Impedir a vida de ficar negativa
        self._vida -= dano_real
        if self._vida < 0:
            self._vida = 0

        print (f"{self._nome} recebeu {dano_real} de dano. Sobrou: {self._vida}")

    def curar(self, quantidade_cura):
        self._vida += quantidade_cura
        if self._vida > self._vida_maxima:
            self._vida = self._vida_maxima

        print (f"{self._nome} curou {quantidade_cura}. Vida atual: {self._vida}")

    def esta_vivo(self):
        return self._vida > 0

    def atacar(self, outro):
        raise NotImplementedError("A subclasse precisa implementar o método atacar()")

    def status (self):
        print(f"\n{self._nome} - Vida: {self._vida}, Ataque: {self._ataque}, Defesa: {self._defesa}")

    def morreu(self):
        return self._vida <= 0
    
    