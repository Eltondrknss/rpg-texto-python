from personagem import Personagem

class Mago(Personagem):
    def atacar(self, outro):
        dano = (self.ataque * 2) - outro.defesa
        if dano > 0:
            outro.perder_vida(dano)
            print(f"\n 🧙‍♂️ {self.nome} lançou uma bola de fogo e causou {dano} de dano, deixando {outro.nome} com {outro.valor_vida()} de vida")
        else:
            print(f"\n 🧙‍♂️ {self.nome} lançou uma bola de fogo mas errou feio...")

class Guerreiro(Personagem):
    def atacar(self, outro):
        dano = self.ataque - (outro.defesa // 2)
        if dano > 0:
            outro.perder_vida(dano)
            print(f"\n ⚔️ {self.nome} meteu a espadada no {outro.nome} e causou {dano} de dano, deixando {outro.nome} com {outro.valor_vida()} de vida")
        else:
            print(f"\n ⚔️ {self.nome} tentou atacar mas foi bloqueado pelo {outro.nome}.")

class Arqueiro(Personagem):
    def atacar(self, outro):
        from random import randint
        critico = randint(1,10) == 1
        dano = self.ataque - outro.defesa
        if critico:
            dano *= 2
            outro.perder_vida(dano)
            print(f"\n 🏹 {self.nome} ACERTOU UMA FLECHADA CRÍTICAAAAAAA 🏹🏹🏹 sobrou só {outro.valor_vida()} de vida pro {outro.nome}")
        elif dano > 0:
            outro.perder_vida(dano)
            print(f"\n 🏹 {self.nome} causou {dano} de dano com uma flechada, deixando {outro.nome} com {outro.valor_vida()} de vida")
        else:
            print(f"\n 🏹 {self.nome} errou a flechada e acertou um passarinho que estava voando por alí...")