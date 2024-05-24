### Exemplos de estruturas de dados em C: vetores e matrizes.

**EXEMPLO 11.1**
```
C                           assemble
int V[NNN]                  la      r1, V           # r1 <- &(V[0]) 
...                         lw      r4, 4(r1)       # r4 <- M[r1 + 1*4]
V[0] = V[1] + V[2]*16       lw      r6, 8(r1)       # r6 <- M[r1 + 2*4]
                            sll     r6, r6, r4      # r6*16 = r6<<r4
                            add     r7, r4, r6      
                            sw      r7, 0(r1)       # M[r1 + 0*4] <- r4+r6
``` 

O trecho acima considera o acesso ao vetor de inteiros V, que mostra um exemplo em linguagem C e o equivalente em assemble. Destaca-se o deslocamento de 4 bytes para acessar os interios, haja vista o vetor ser de inteiros. Ao registrador r4 é atribuido o valor de V[1], ao r6 o valor de V[2], ao r7 o valor a ser armazenado em V[0]. Os comentarios mostram o calculo do *endereço efetivo* usando como base o V[0] inicial e usando o deslocamento de 4 bytes. 

A caracteristica importante que voce deve observar eh o tempo de compilacao (quando o compialdor examina o codigo), note que nao ha ambiguidade dos deslocamentos com relacao ao vetor, isso se da pelo deslocamento fixo nas instrucoes lw e sw. A figura 11.6 apresenta os deslocamentos com relacao a base do vetor, que nesse contexto eh &(V[0]).

![alt text](./imagens/figura-11-6.png)

**EXEMPLO 11.2**
```
C                           assemble
int V[NNN]                  la      r1, V           # r1 <- &(V[0]) 
...                         sll     r2, rj, 2       # r2 <- j * 4
V[0] = V[1] + V[2]* 16      addu    r3, r2, r1      # r3 <- V + j*4
                            lw      r4, 0(r3)       # r4 <- M[V + j*4]
                            sll     r2, rk, 2      # r2 <- M[V + j*4] 
                            addu    r3, r2, r1      # r3 <- k * 4
                            lw      r6, 0(r3)       # r6 V + V + k*4
                            add     r7, r4, r6
                            sll     r2, r1, 4           # r6 <- r6*16
                            addu    r3, ri, 4           # r3 <- V + i*14
                            sw      r7, 0(r2)       # M[V + i*4] <- r7
``` 

**EXEMPLO 11.3**
```
C                                   Assemble
typedef struct A {                  
    int x;                          
    int y;                          
    int z;                          
    int w;                          
} aType;                            
...                                 
aType V[16]                         la      r5, 0x008000000     # r5 <- &(V[0])
...                                 lw      r8, (48+4)(r5)      # r8 <- V[3].y
    m = V[3].y;                     lw      r9, (48+8)(r5)      # r9 <- V[3].z
    n = V[3].z;                     add     r5, r8, r9          # r5 <- r8 + r9 (soma de V[3].y e V[3].z)
    V[3].x = m+n                    sw      r5, (48+0) (r5)     # V[3].x <- m+n
```                             

Acima está disposto em C e em Assemble um trecho de código que demonstra a aplicabilidade de operações de acesso, registro e  alteração de vetores. Ou seja, manipulação da memória a partir do conceito de tipos de dados.  

Ademais, para o exemplo citado acima temos a definição de um tipo de dado definido como aType que possui 4 atributos (x, y, z e w), cada um sendo um inteiro assim como temos disposto o vetor V com 16 elementos do tipo aType.  

Agora vamos destrinchar um pouco mais sobre esse trecho acima citado. Relembrando, estamos aqui tratando de um assemble para a memória MIPS(Microprocessor without Interlocked Pipelina Stages) então as instruções a seguir são referentes a esse modelo de memória. As instruções para esse exemplo são *la*, *lw*, *add* e *sw*.  

- **la** -> Load Address: é uma pseudo-instrução usada para carregar um endereço em um registrador.
  - sintaxe: ```la reg, address``` 
  - exemplo: ```la r5, 0x008000000``` quer dizer que o endereço '00x8000000' será carregado no registrador 'r5'

- **lw** -> Load Word: é usado para carregar um valor de 32 bits (ou um "word") da memória para um registrador
  - sintaxe: ```lw reg, offset(base_reg)``` 
  - exemplo: ```lw r8, (48+4)(r5)``` significa que o valor armazenado na posição de memória calculada como 'base_address + offset' (onde 'base_address' é o valor contido em 'r5' e 'offset' é 52 no caso) é carregado no registrador 'r8'

- **add** -> Addition: como o nome sugere é usado para somar os valores de dois registradores e armazenar o resultado em um registrador de destino.
  - sintaxe: ```add destination_reg, source_reg1, source_reg2```
  - exemplo: ```add r5, r8, r9``` soma os valores dos registradores 'r8' (que contém V[3].y) e 'r9' (que contém V[3].z), armazenando o resultado em 'r5'.

- **sw** -> Storage Word: é usado para armazenar um valor de 32 bits de um registrador na memória
  - sintaxe: ```sw reg, offset(base_reg)```
  - exemplo: ```sw r5, (48+0)(r5)``` significa que o valor no registrador 'r5' é armazenado na posição de memória calculada como 'base_address + offset' (onde 'base_address' é o valor contido em 'r5' e 'offset' é o 48 no caso).

Talvez surga uma dúvida na diferença entre **lw** e **sw** pois ambas as pseudo-instruções manipulam sim os valores contidos os registradores, porém elas realizam operações opostas, enquanto *lw* transfere dados da memória para o registrador o *sw* transfere dados do registrador para a memória. Esse fato trivial acredito que você já tenha sub-entendido mas deixarei claro, você na função de programador está manipulado diretamente com duas partes do computador: a memória principal (que geralmente é a memória RAM) e uma parte do processador (CPU) que se chama Registradores que nada mais são que pequenos e rápidos artefatos de armazenamento. Então:

Direção da Transferência de Dados:
  - lw (Load Word) transfere dados da memória para um registrador.
  - sw (Store Word) transfere dados de um registrador para a memória.
Uso:
  - lw é usado quando você precisa ler ou carregar dados da memória para trabalhar com eles em registradores.
  - sw é usado quando você precisa salvar ou armazenar dados de um registrador para a memória.