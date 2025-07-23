# RPG de Texto com Python

Projeto simples feito em Python, onde o jogador escolhe uma classe (Mago, Guerreiro ou Arqueiro) e enfrenta batalhas automáticas em estilo RPG de texto.
Essa versão em específico foi feita cumprindo os pilares de Programação Orientada a Objetos.

---

## 🎮 Como funciona

Ao iniciar o programa:

1. O jogador digita seu nome.
2. Escolhe sua classe preferida.
3. Um inimigo é gerado.
4. Os dois personagens lutam até que um deles morra.

Tudo acontece no terminal, com mensagens temáticas pra cada classe.

---

## 🚀 Como executar o projeto
```sh
git clone https://github.com/Eltondrknss/rpg-texto-python.git
cd rpg-texto-python
python main.py
```
---

## 🧠 Conceitos aplicados

**Programação Orientada a Objetos**

O projeto foi estruturado utilizando os 4 pilares da programação orientada a objetos pra criar um código mais seguro e organizado.

- **Classes e objetos**: Foram utilizadas classes (`Personagem`, `Arqueiro`, `Guerreiro`, `Mago` e `Inimigo`) para modelar as entidades no jogo. No arquivo `main.py` são criadas as instâncias dessas classes para representar os personagens da batalha.

- **Encapsulamento**: Pra garantir a integridade dos dados, os atributos das classes foram protegidos (`_nome`, `_vida`, `_ataque`, `_defesa`), e a manipulação desses dados é controlada por métodos como `receber_dano()` e `curar()`, que contem as regras do jogo (ex: a vida não pode ficar negativa). O acesso a esses dados é feito de forma segura através de `@property`.

- **Herança**: As classes (Mago, Guerreiro, etc) herdam da classe base Personagem. Isso permite o reuso do código, já que todos os personagens compartilham atributos e métodos em comum, como a lógica de dano, por exemplo.

- **Polimorfismo**: O método `atacar()` é definido na classe Personagem e em seguida é sobrescrito em cada subclasse. Isso permite que o mesmo comando `jogador.atacar(inimigo)` execute uma ação completamente diferente,  com lógicas e mensagens personalizadas, tornando o código principal da batalha mais limpo e flexível.

**Código versionado**

**Commits organizados**


---

## 📁 Estrutura do projeto
```
rpg-texto-python/

├── main.py            #Arquivo principal. Inicia o jogo e controla o loop da batalha
├── personagem.py      #Contém a classe Personagem que serve de base para todas as outras.
├── classes_herois.py  #Centraliza todas as subclasses do jogo (mago, guerreiro, arqueiro)
└── README.md          #Este documento
```
