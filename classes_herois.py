from personagem import Personagem

# mago = ataque dobrado
class Mago(Personagem):
    def atacar(self, outro):
        dano = (self.ataque * 2) - outro.defesa
        if dano > 0:
            outro.receber_dano(dano)
            print(f"\n 🧙‍♂️ {self.nome} lançou uma bola de fogo e causou {dano} de dano, deixando {outro.nome} com {outro.vida} de vida")
        else:
            print(f"\n 🧙‍♂️ {self.nome} lançou uma bola de fogo mas errou feio...")

# guerreiro = ignora metade da defesa do oponente
class Guerreiro(Personagem):
    def atacar(self, outro):
        dano = self.ataque - (outro.defesa // 2)
        if dano > 0:
            outro.receber_dano(dano)
            print(f"\n ⚔️ {self.nome} meteu a espadada no {outro.nome} e causou {dano} de dano, deixando {outro.nome} com {outro.vida} de vida")
        else:
            print(f"\n ⚔️ {self.nome} tentou atacar mas foi bloqueado pelo {outro.nome}.")

# arqueiro = 10% de chance de acerto crítico (dano x2)
class Arqueiro(Personagem):
    def atacar(self, outro):
        from random import randint
        critico = randint(1,10) == 1
        dano = self.ataque - outro.defesa
        if critico:
            dano *= 2
            outro.receber_dano(dano)
            print(f"\n 🏹 {self.nome} ACERTOU UMA FLECHADA CRÍTICAAAAAAA 🏹🏹🏹 sobrou só {outro.vida} de vida pro {outro.nome}")
        elif dano > 0:
            outro.receber_dano(dano)
            print(f"\n 🏹 {self.nome} causou {dano} de dano com uma flechada, deixando {outro.nome} com {outro.vida} de vida")
        else:
            print(f"\n 🏹 {self.nome} errou a flechada e acertou um passarinho que estava voando por alí...")
