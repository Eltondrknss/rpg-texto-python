from classes_herois import *

print("\nBEM VINDO AO SIMULADOR DE BATALHAS RPG DE TEXTO DO ELTON\n")
jogador_nome = input("Digite o nome do seu jogador: ")

print(f"\n Escolha sua classe :"
      "\n 1 - 🧙‍♂️  Mago"
      "\n 2 - ⚔️  Guerreiro"
      "\n 3 - 🏹  Arqueiro")

classe_escolhida = input("\n Digite o número da classe escolhida: ")

if classe_escolhida == "1":
    jogador = Mago(jogador_nome, 100, 40, 20)
elif classe_escolhida == "2":
    jogador = Guerreiro(jogador_nome, 120, 30, 30)
elif classe_escolhida == "3":
    jogador = Arqueiro(jogador_nome, 90, 35, 25)
else:
    print("Opção inválida. Vai jogar de Mago fraquinho então.")
    jogador = Mago(jogador_nome, 50, 20, 10)

inimigo = Guerreiro("Jubileu", 100, 30, 20)

while jogador.esta_vivo() and inimigo.esta_vivo():
    jogador.atacar(inimigo)
    if inimigo.esta_vivo():
        inimigo.atacar(jogador)

print("\nFIM DA BATALHA\n")

if jogador.morreu():
     print(f"{jogador.nome} morreu.\n")

if inimigo.morreu():
    print(f"{jogador.nome} venceu a luta! Parabéns, {jogador_nome}.\n")























# from classes_herois import *

# elton = Mago("Elton", 200, 50, 20)
# jubileu = Arqueiro("Jubileu", 200, 50, 20)

# elton.status()
# jubileu.status()

# while jubileu.esta_vivo() and elton.esta_vivo():
#     elton.atacar(jubileu)
#     if jubileu.esta_vivo():
#         jubileu.atacar(elton)
#     # elton.status()
#     # jubileu.status()

# if elton.morreu():
#     print(f"\n {elton.nome} morreu. \n")

# if jubileu.morreu():
#     print(f"\n {jubileu.nome} morreu. \n")