#### Sobre o assembly

Um programa assembly eh formado por um conjunto de linhas, contendo uma instrucao por linha. Outro fator relevante eh que cada linha pode ser composta por 3 partes: 
 - Label, eh um nome simbolico usado para representar o endereco da instrucao associada
 - Instrucao, eh a operacao a ser realizada naquela linha
 - Comentario, como o nome sugere, eh usado para comentar algo daquela linha

Note que o que divide a parte label e instrucao eh o caractere ":".
Note também que o que separa a instrucao do comentario é o caractere "#"

###### Exemplo
"""
.L1:    add r1, r2, r3      # r1 <- r2+r3
        sub r5, r6, r7      # r5 <- r6+r7
fim:    j   .L1             # salta para o endereco de L1
"""


#### Nomeclatura
Veja que o Assembler eh diferente do Assembly. Assembler eh um programa montador que traduz a linguagem de montagem (Assembly) para uma linguagem de maquina, que eh o codigo de maquina interpretado pelo processador


