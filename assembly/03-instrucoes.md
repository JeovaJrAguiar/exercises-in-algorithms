### Aritmeticas
- INC: incrementa 1, na variavel ou registrador 
- DEC: decrementa 1 de forma semelhante
- ADD: soma entre fonte e destino
- SUB: subtracao entre fonte e destino
- CMP: compara a diferenca, entre nenhum é alterado
- IMUL: multiplica dois inteiros
- IDIV: divide dois inteiros

### Logicas
- AND: 
- NEG: 
- NOT: 
- OR : 
- XOR: 

### Salto
- JMP: a execucao eh transferida para instrucao identificada no rotulo
- JE: salta se igual
- JG: salto se maior
- JL: salto de menor
- JGE: salto de maior ou igual
- JNE: salto se nao for igual

### Laco
- LOOP: reduz o valor do contador e verifica se é maior que 0
- LOOPE: reduz o valor do contador e verifica se é maior que 0 e se ZF(zero flag) esta definido
- LOOPNE: reduz o valor do contador e verifica se é maior que 0 e requer que ZF nao esteja definido

### Fluxo e Manipulacao
- MOV: mode o valor para o destino
- RET: retorna um procedimento
- CALL: chama um procedimento no endereco especificado
- PUSH: grava um valor no topo de uma pilha
- POP: restaura o valor no topo da pilha em um registrador
- OFFSET: indica o número de locais de endereco para chegar a um endereco absoluto especifico
- END: encerra o procedimento principal
- ENDP: encerra um procedimento especificado
- INVOKE: exclusivamente do MASM de 32bits, chma o procedimento no endereço fornecido