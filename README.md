# EP1-Projeto-Integrador-V-HexGame

# Game Básico

Você deverá fazer uma engine do game que possa jogar de forma que possa jogar humano x humano. 

Deverá ter uma interface simples de exibição e entrada dos dados via terminal. Pode fazer interface gráfica se desejar.

Deverá usar os conceitos do curso como espaço de estados, ações, funções de utilidade, função sucessora.

Pode-se e deve-ser usar pesquisa da internet (referenciar as fontes) para a construção do seu agente.

### Modelagem - Montar uma apresentação e vídeo

- Introdução ao trabalho e explicação do game
- Explicar as regras do jogo
- Espaço de estados: Como é modelado um estado com as posições?
    - Próximos movimentos
    - Quando é um estado final?
    - Como vai se serializar o espaço de estados para criar novos?
- Como se calcula a função de utilidade?
    - Para este tipo de problema, a função utilidade não é possível ser -1, 0, 1 pela complexidade do jogo. Pede-se para que se pense um cálculo numérico com as peças e configurações
- Referências: de onde tirou as informações?
    - Sites
    - Livros ou Revistas
    - Códigos-fonte

### Código fonte e código executado - Exibição do código e detalhamento

Deverá ser entregue o repositório no Github. 

**Não será permitido** de uso de bibliotecas de software de Inteligência Artificial, usar apenas a biblioteca padrão da linguagem.

O que será avaliado:

- Apresentação do tabuleiro, interação com o usuário
- Espaço de estados, função sucessora e utilidade.

O que não será avaliado

- Componentes gráficos. Não me importa se vai ser gráfico 3D ou imprimir no terminal. (Sugestão: imprimir no terminal é trivial)
- Interação com o usuário: não se esperar nenhuma interface homem-máquina sofisticada. Se o usuário digitar qual o seu movimento usando o terminal, é o suficiente.
