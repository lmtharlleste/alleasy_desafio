# Desafio de Categorização de Textos - Análise de Resultados

## Introdução

Este repositório contém a implementação de uma solução para o **Problema 2: Categorização de Textos**. A solução utiliza uma base de regras definidas para categorizar textos com base em condições específicas relacionadas a características dos textos, como o número de sentenças, tokens, presença de expressões e outros fatores.

### Objetivo do Problema

A tarefa é aplicar um conjunto de regras pré-definidas para categorizar textos. Cada regra segue o formato de **"Se condição, então implicação"**, onde as condições podem incluir comparações sobre o número de sentenças, o número de tokens, a presença de expressões específicas, e outros aspectos. O resultado é uma lista de categorias inferidas para cada texto.

### Descrição do Problema Específico (id 4)

Durante a execução da solução, o sistema categorizou o texto com **id 4** como pertencente à categoria **"B"**, enquanto o enunciado do problema especifica que a categoria correta seria **"C"**.

A seguinte explicação busca analisar por que o código retorna a categoria **"B"** para o texto de id 4 e discutir se o enunciado pode estar errado ou se houve algum equívoco no código.

---

## Análise do Comportamento do Código

O sistema de categorização é baseado em uma série de regras que analisam as propriedades dos textos, como o número de sentenças, tokens e a presença de expressões. O código implementa essas regras da seguinte forma:

### Regras Definidas no Código

A base de regras utilizada tem as seguintes condições:

1. **Número de sentenças com expressões**
2. **Número de sentenças**
3. **Número de tokens**
4. **Presença de token específico**
5. **Presença de expressões**
6. **Número de vírgulas** - **Regra importante para o caso do id 4**

Em particular, a categoria **"C"** é atribuída quando o **número de vírgulas** é **menor que 10**, conforme indicado na regra correspondente.

### O Texto com id 4

O texto referente ao **id 4** contém **2 sentenças** e **9 vírgulas**, o que está dentro das condições que deveriam atribuir a categoria **"C"**. Contudo, o sistema categoriza esse texto como pertencente à categoria **"B"**.

### Por que o código retornou "B" em vez de "C"?

O problema ocorre porque o código, ao processar as regras, não prioriza adequadamente a categoria **"C"** quando as condições para ela são atendidas. O código considera as categorias conforme as regras são aplicadas e, quando várias condições são atendidas para diferentes categorias, a primeira que corresponde é atribuída. 

Como as condições para a categoria **"B"** também são atendidas e são avaliadas antes das condições para a categoria **"C"**, o código acaba retornando a categoria **"B"**.

### O que precisa ser ajustado?

Para garantir que a categoria **"C"** seja atribuída corretamente quando o número de vírgulas for menor que 10, independentemente das outras categorias, seria necessário aplicar uma **priorização explícita de categorias** no código. Isso garantiria que, sempre que a categoria **"C"** fosse atendida, ela fosse mantida como a única categoria atribuída, mesmo que outras regras para outras categorias fossem atendidas.

---

## Enunciado vs. Código

O enunciado especifica que a categoria correta para o **id 4** é **"C"**, dada a condição de número de vírgulas **menor que 10**. Isso é consistente com as regras definidas no enunciado, mas o código não está priorizando a categoria **"C"** corretamente.

### Possíveis Causas

1. **Equívoco na Prioridade das Regras**: O código não está aplicando as regras de forma a garantir que a categoria **"C"** seja sempre atribuída quando suas condições forem atendidas, mesmo que outras categorias possam ser inferidas para o mesmo texto.
2. **Erro no Enunciado**: Embora o enunciado tenha especificado a categoria **"C"** como correta, há a possibilidade de que a interpretação das condições e das regras no enunciado tenha sido equivocada ou mal definida. Neste caso, o código e as regras que ele segue podem estar corretos e o erro poderia estar no enunciado.

---

## Conclusão

- **Código**: A lógica de categorização no código está quase correta, mas há um pequeno ajuste necessário na priorização das categorias para garantir que a categoria **"C"** seja aplicada corretamente quando suas condições forem atendidas.
  
- **Enunciado**: O enunciado especifica que a categoria correta para o **id 4** é **"C"**, e isso é consistente com a regra de **número de vírgulas**. Portanto, é possível que a categorização como **"B"** seja um erro no código ou uma falha na implementação da priorização das categorias.

---

## Próximos Passos

Para corrigir o problema:

1. **Revisão da Lógica de Priorização**: Implementar uma lógica que garanta que, quando a categoria **"C"** for inferida, ela seja atribuída, independentemente das outras categorias que possam ser inferidas.
2. **Verificação de Outras Regras**: Certificar-se de que todas as regras estejam sendo aplicadas corretamente e sem sobreposição indevida de categorias.

---

## Contribuições

Se você identificar melhorias ou ajustes que podem ser feitos no código para corrigir esse comportamento, fique à vontade para contribuir com uma **pull request**!

---

Essa versão está formatada para exibição no GitHub, com títulos, listas e ênfases apropriadas para facilitar a leitura e a compreensão.
