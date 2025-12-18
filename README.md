# Program-man

Projeto desenvolvido pela **Equipe 8** como entrega final da disciplina de **Introdução à Computação**.

## 1. Equipe

* Vinícius Baumel Macedo
* Luiz Gustavo São Mateus Lima
* Matheus Alcântara Pereira da Silva
* Maria Eduarda Soares Machado
* Avir Katz

## 2. Visão Geral do Projeto

**Program-man** é um jogo em Python, inspirado na mecânica clássica de navegação em labirintos com coleta de itens e fuga de inimigos. O projeto prioriza:

* Estrutura modular
* Programação orientada a objetos
* Manipulação de sprites
* Uso de tiles para construção de mapas

## 3. Ferramentas e Bibliotecas

* **Python 3**
* **pygame** (biblioteca principal de desenvolvimento)
* **VS Code** (IDE utilizada)
* **Gemini**: criação de sprites dos personagens
* Playlist utilizada como trilha de aprendizagem em pygame

## 4. Arquitetura do Jogo

### 4.1 Entidades (Sprites)

As principais entidades (player, parede, pellet e inimigos) herdam de `pygame.sprite.Sprite`, o que permite:

* Organização por meio de `Groups`
* Atualização centralizada
* Colisões otimizadas (`spritecollide`)
* Ciclo de vida claro de cada elemento

**Responsabilidades-chave**

* **Player**: movimentação, leitura de inputs e colisões
* **Parede**: obstáculo estático
* **Pellet**: item coletável
* **Inimigos**: perseguição e lógica de ameaça

### 4.2 Mapa (Labirinto baseado em tiles)

O labirinto é gerado a partir de uma matriz/grade de caracteres. Cada caractere representa uma entidade no cenário.

Benefícios do modelo:

* Separação entre lógica e layout
* Facilidade para criação de novos mapas
* Expansão para múltiplos níveis

### 4.3 Loop Principal (`main.py`)

Fluxo de execução:

1. Processamento de eventos
2. Atualização do estado do jogo
3. Renderização da tela

Características:

* Uso de `Clock` para controle de FPS
* Padroniza atualização e sincronização visual

### 4.4 Assets

As imagens utilizadas estão organizadas na pasta `/imagens`.
Isso garante:

* Ausência de caminhos absolutos
* Facilidade de substituição de sprites sem alterar lógica

## 5. Estrutura da Documentação do Projeto (Relatório)

O documento anexado ao repositório apresenta:

* Arquitetura do código
* OOP aplicada ao pygame
* Componentes gráficos
* Desenho estrutural do labirinto
* Conceitos de modularização e sprites
* Estratégias de atualização/render loop
* Screenshots e galerias
* Desafios enfrentados e soluções encontradas
* Lições aprendidas em equipe

## 6. Divisão do Trabalho

* **Avir Katz**: artes visuais dos personagens e coletáveis
* **Matheus Alcantara**: sistema de movimentação e placar
* **Maria Eduarda**: composição do mapa e tela inicial
* **Luiz Gustavo**: sistema de pontuação e coleta
* **Vinicius Baumel**: lógica dos fantasmas e integração final dos módulos

## 7. Conceitos Aplicados

* Lógica sequencial, condicional e de repetição
* Funções e modularização
* Programação orientada a objetos
* Arquitetura básica de jogos
* Sprites, tiles, colisões, render pipeline

## 8. Desafios Enfrentados

Principais barreiras do projeto:

* Curva de aprendizado em orientação a objetos
* Inexperiência inicial com GitHub
* Comunicação remota por mensagens
* Pressão de tempo na conclusão

Como o grupo superou:

* Tentativa e erro orientada
* Auxílio de colegas mais experientes
* Consumo de vídeos explicativos e referências
* Adoção de reuniões frequentes via Discord

## 9. Lições Aprendidas

1. Organização e padronização aceleram o desenvolvimento
2. Dedicação + paciência produzem resultados funcionais
3. Recorrer à equipe e monitores maximiza eficiência

## 10. Como Executar

(Preencha ao finalizar)
Exemplo:

```
pip install pygame
python main.py
```

## 11. Galeria do Projeto

Inserir:

* Tela inicial
* Labirinto
* Pontuação
* Inimigos
* Coleta de pellets


