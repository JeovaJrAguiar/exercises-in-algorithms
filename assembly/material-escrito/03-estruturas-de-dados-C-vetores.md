### Estruturas de dados em C: matriz, nada mais que um vetor multidimencional.

Pelo o que entendi aqui a gente vai discorrer sobre como eh a construcao e compisicao do que conhecemos de algumas estruturas em C e em Assemble, e claro ambos na visao da memoria MIPS.  

Entenda aqui por *TED* como um tipo estruturado de dados, ou mesmo um tipo de dado, eh como eu quero representar os tipos basicos de variaveis e constantes representaveis em C, pode ser que em outra literatura autores nomeiem de outra forma, tudo bem? Pois bem! Em C existe a funcao chamada **sizeof()** que retorna a quantidade de bytes nescessarios para representar o respectivo *TED* entao fica atento que voce pode sim usar esse recurso durante a sua jornada.  

Outro ponto que devo trazer a voce eh que **ponteiros para qualquer *TED* possui exatamente o mesmo tamanho** independente de qual tipo de estrutura de dados ele seja, o ponteiro em si possui um tamanho definido.

![Alt text](./imagens/figura-11-2.png)

Aqui na figura 11.4 vai mostrar um exemplo de como se comporta a alocacao em memoria. Para esse exemplo temos 3 vetores de tipos diferentes **char**, **short** e **int**.


![Alt text](./imagens/figura-11-4.png)

Note que elementos contiguos de vetores e estruturas de dados sao alocados sempre em enderecos contiguos, ou seja V[i+1] eh alocado no endereco seguinte a V[i]. O que voce deve entender eh que existe uma dependencia do proximo valor a ser indexado, e essa dependencia eh dada pelo atual endereco alocado, assim o endereco do 'elemento seguinte' depende do tipo dos elementos do vetor V, então se foi alocado um vetor char[5] partindo do M[x], o próximo endereço 'livre' para ser utilizado eh o M[x+5].

Quem programa em *assebly* controla **todas** as estrutuas de dados, e quando digo controla eh literalmente controla todas as estruturas de dados, sendo assim do ponto de vista de alto nivel essa eh uma responsabilidade importante. A controladora fica responssavel por acessar palavras de 4 em 4 *bytes*, elementos de vetores que dependem diretamente do tipos dos elementos, elementos de vetores em enderecos que dependem do **sizeof()** dos elementos e por ai vai. Nao sendo permitido o luxo de utilizar abstracoes de linguagens de alto nivel como C quando programa-se em *assembly*.  

Em C por exemplo uma matriz eh alocada como um vetor de vetores, ja em *assembly* o programador tera que alocar precisamente a memoria para poder tiliza-la de maneira eficaz. E *assembly* para elementos do tipo **T**, linhas com **m** linhas e **n** colunas, o endereco do elemento de indices ***i, j*** eh obtido com a equacao 11.2. E na figura 11.5, eh mostrado o diagrama que relaciona o endereco base da matriz ( M = &(M[0][0]) ), linhas e colunas de uma matriz de elementos do tipo *T*.

```
Equacao 11.2
&(M[i][j]) = &(M[0][0]) + |T|(n * i+j) 
``` 

![alt text](./imagens/figura-11-5.png)

