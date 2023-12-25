Primeiro deve-se entender que toda entrada numerica vinda do teclado é tratada em assembly como sendo uma sequencia de caracteres ou seja, uma string. Mesmo transformando inicialmente cada caractere para seu valor correspondente da tabela ASCII e posteriormente para o correspondente em binario esse resultado na maioria dos casos está fora do valor difitado no teclado. Para resolver esse problema deve-se realizar o tratamento dessa entrada.

### Transformar valor decimal em ASCII para Decimal
Imagine uma string dada pelo terminal, possui o valor "123", crie uma variável total, a idéia é iterar sobre essa string e para cada iteração sobre essa string multiplicar o valor de total por 10 (assim garantimos as casas decimais de dezena, centena, milhar e por aí vai) e adicionar em total o valor inteiro daquele caractere.

pseudo-codigo:
```
str = "123"
total = 0

for ch in str:
 total *= 10
 total += (int) ch

print(total) // 123
```
### Link onde assistir o conteúdo
https://www.youtube.com/watch?v=3VVbnwXv2_Y