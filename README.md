Relatório do Projeto Program-man |Equipe 8
Título: Program-man
Participantes:
 Vinícius Baumel Macedo
 Luiz Gustavo São Mateus Lima
 Matheus Alcântara Pereira da Silva
 Maria Eduarda Soares Machado
 Avir Katz
Organização do Projeto:
1. Entidades do jogo(Sprites):
As entidades principais (jogador, paredes, pellets, inimigos)
herdam de pygame.sprite.Sprite. Isso permite:
 Uso de Group para atualização e renderização
 Colisões eficientes com spritecollide
 Organização clara do ciclo de vida dos objetos
Exemplos de responsabilidades:
 Jogador: movimento, entrada do usuário, colisões
 Parede: obstáculo estático
 Pellet: item coletável
2. Mapa / Labirinto:
O labirinto é construído a partir de uma representação em
grade (tiles). Cada caractere ou valor do mapa gera uma
entidade correspondente.
Benefícios dessa abordagem:
 Fácil criação de novos mapas
 Separação entre lógica e layout
 Escalável para múltiplos níveis
3. Loop principal do jogo (Main.py):
O loop principal segue o padrão:
1. Processar eventos
2. Atualizar estado do jogo
3. Renderizar na tela
Isso garante:
 Taxa de quadros controlada ( Clock )
 Atualizações consistentes
 Código previsível e organizado
4. Assets desacoplados do código
As imagens ficam na pasta imagens/ , evitando caminhos
absolutos e facilitando a troca de sprites sem alterar a lógica do
jogo.
Galeria:
Ferramentas e Bibliotecas:
 Python 3 é o programa de linguagem base de todo o projeto
 Vs.code é a principal plataforma utilizada durante todo o projeto
 Toda a estrutura do jogo foi feita na base da biblioteca pygame, devido a
sua gama de possibilidades ser suficiente para o projeto, e seu uso ser
simples
 Ferramenta Gemini foi utilizada para o desenho dos personagens
 A lista de reprodução foi utilizada como ferramenta de aprendizagem
sobre a biblioteca pygame, e suas funcionalidades
ttps://www.youtube.com/playlist?list=PLJ8PYFcmwFOxtJS4EZTGEPxMEo4YdbxdQ
Divisão do Trabalho:
 Avir Katz: Responsável pelos aspectos visuais dos personagens e coletáveis
 Matheus Alcantara: Responsável pelo sistema de movimentação, acabou
também agindo na composição visual do placar
 Maria Eduarda: Responsável pela composição do mapa, acabou também agindo
na composição da tela inicial
 Luiz Gustavo: Responsável pelo sistema de pontuação e de coleta dos coletáveis
 Vinicius Baumel: Responsável pelos fantasmas, e agiu na união e organização
dos códigos em um projeto único
Conceitos utilizados:
 A exorbitante maioria dos conceitos aprendidos ao longo da cadeira de
Introdução a computação foram utilizados, como as funções(def), loops
lógicos
 Arquitetura de jogos
 Programação orientada a objetos
 Organização de código em módulos
 Manipulação de sprites, mapas e colisões
Maiores Desafios:
 Maior erro cometido foi o uso da orientação a objeto, problema foi
contornado pela tentativa e erro, e orientações do componente do grupo
Vinicius Baumel que possui maior experiencia no assunto
 Maior Desafio encontrado foi a falta de tempo aliada a inexperiência no
uso do github e a comunicação inicial (feita exclusivamente via
mensagens). Para isso, recorremos a vídeos explicativos na internet e a
ajuda de componentes do grupo, além de começarmos a ter ligações via
Discord mais recorrentes
 Lições Aprendidas:
1. Importância de organização e padronização no código para eficiência
no desenvolvimento de projetos
2. A dedicação e paciência são fundamentais para o funcionamento
3. É necessário ser humilde, e recorrer a colegas e monitores, caso
necessário 
