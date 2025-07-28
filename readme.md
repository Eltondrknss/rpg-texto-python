
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

O projeto foi estruturado utilizando os 4 pilares da programação orientada a objetos para criar um código mais seguro e organizado.

- **Classes e objetos**: Foram criadas as classes `Personagem` (classe base), `Arqueiro`, `Guerreiro`, `Mago` e `Inimigo` para modelar as entidades do jogo. No arquivo `main.py` são instanciados objetos dessas classes para representar o jogador e o inimigo na batalha.

- **Encapsulamento**: Os atributos das classes são protegidos com underscore (`_nome`, `_vida`, `_ataque`, `_defesa`) e só podem ser acessados através de propriedades (`@property`) e métodos específicos como `receber_dano()` e `curar()`. Isso garante que as regras do jogo sejam respeitadas (ex: vida não pode ser negativa).

- **Herança**: As classes `Mago`, `Guerreiro` e `Arqueiro` herdam da classe base `Personagem`, reutilizando atributos comuns (`_nome`, `_vida`, `_ataque`, `_defesa`) e métodos como `receber_dano()` e `esta_vivo()`, evitando repetição de código.

- **Polimorfismo**: O método `atacar()` é implementado de forma diferente em cada classe filha. Quando chamamos `jogador.atacar(inimigo)`, o comportamento varia conforme a classe: o Mago pode usar magia, o Guerreiro golpes físicos, e o Arqueiro ataques à distância, mas todos respondem ao mesmo método.

**Outras práticas aplicadas:**
- Controle de versão com Git
- Separação de responsabilidades em arquivos diferentes

**Código versionado**

**Commits organizados**


---

## 📁 Estrutura do projeto
```
rpg-texto-python/
├── main.py                # Arquivo principal, controla o fluxo do jogo
├── personagem.py          # Classe base Personagem
├── classes_herois.py      # Subclasses: Mago, Guerreiro, Arqueiro
├── readme.md              # Instruções básicas e conceitos
├── documentacao.md        # Esta documentação
└── .gitignore             # Arquivos ignorados pelo Git
```
