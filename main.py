from classes_herois import * #***** Comentario Grazyele: Má pratica de programação  - Importar tudo pode pode causar futuros conflitos *******
# Comentario Grazyele:  Use imports específicos: from classes_herois import Mago, Guerreiro, Arqueiro

# Chama o inicio do jogo e a seleção de classe do personagem
print("\nBEM VINDO AO SIMULADOR DE BATALHAS RPG DE TEXTO DO ELTON\n")

# ***Comentario Grazyele:Falta validação de entrada  -  precisa de uma validação caso o usuario digite string vazia, números ou caracteres especiais***
jogador_nome = input("Digite o nome do seu jogador: ")

# ***Comentario Grazyele: E se digitar texto ? numero inválido? Não válida entrada. Não deve continuar caso ele não digitar uma opção válida***

print(f"\n Escolha sua classe :"
      "\n 1 - 🧙‍♂️  Mago"
      "\n 2 - ⚔️  Guerreiro"
      "\n 3 - 🏹  Arqueiro")

classe_escolhida = input("\n Digite o número da classe escolhida: ")

# *******Comentario Grazyele: Código duplicado - Deve usar Factory Pattern (Estudar ele, pois faz parte do POO) *******
# instancia um jogador de acordo com a opção escolhida

#*** Comentario Grazyele: númeos sem explicações (deveria usar constantes configuráveis)**** 
if classe_escolhida == "1":
    jogador = Mago(jogador_nome, 100, 40, 20) #De onde vêm esses valores?
elif classe_escolhida == "2":
    jogador = Guerreiro(jogador_nome, 120, 30, 30) #De onde vêm esses valores?
elif classe_escolhida == "3":
    jogador = Arqueiro(jogador_nome, 90, 35, 25) #De onde vêm esses valores?
else:
    print("Opção inválida. Vai jogar de Mago fraquinho então.")
    jogador = Mago(jogador_nome, 50, 20, 10)

# instancia um inimigo com a classe e status predefinidos
inimigo = Guerreiro("Jubileu", 100, 30, 20)

# loop que continua a batalha enquanto um dos dois estiverem vivos
while jogador.esta_vivo() and inimigo.esta_vivo():
    jogador.atacar(inimigo)
    if inimigo.esta_vivo():
        inimigo.atacar(jogador)

# mensagem de encerramento do jogo
print("\nFIM DA BATALHA\n")
#******* Comentario Grazyele: Falta tratamento de erro se ambos morrem simultaneamente
if jogador.morreu():
     print(f"{jogador.nome} morreu.\n")

if inimigo.morreu():
    print(f"{jogador.nome} venceu a luta! Parabéns, {jogador_nome}.\n")
