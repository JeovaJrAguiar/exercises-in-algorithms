### Registros na arquitetura x86. 
É fato que existem registradores que são compostos por outros retistradores, é como se um fosse formado por mais de um.

### Os principais registradores são: EAX, EBX, ECX, EDX, ESI, EDI, ESP, EBP.

EAX -> AX (acumulator) usado em instruções e operacoes aritméticas para receber valores de cálculos.  
EBX -> BX (base) usado para enderecamento de memória apra referir ao endereço inicial.  
ECX -> CX (counter) usado em loops apra controlar o número de repeticoes.  
EDX -> DX (data) usado em operacoes de entrada e saida por portas fisicas para armazenar entradas e saidas de dados.  
ESI -> (extended source index) usado como indice em operacoes de dados, especialmente em movimentações de blocos de dados, geralmente em indica a FONTE dos dados.  
EDI -> (extended destination index) usado como indice em operacoes de dados, especialmente em movimentações de blocos de dados, geralmente em indica o DESTINO dos dados.  
ESP -> (extended stack pointer) usado para manipular pilha na memória, armazenando dados temporários, endereços de retorno de chamadas de funções e outros dados importantes durante a execução do programa.  
EBP -> (extended base pointer) usado para acessar parâmetros de função e variáveis locais dentro de uma função, facilitando o acesso a dados na pilha, em muitas funções, você verá o EBP sendo configurado no início da função para criar um "quadro de pilha" (stack frame), que fornece um contexto para as variáveis locais e parâmetros.  
  
Outro fato a ser notado é que cada um desses registradores pode ser sub-dividido em outros artefatos os de AH (Hiher Bit, ou bit mais significativo) e AL (Lower Bit, ou bit menos significativo), outro fato é que os regsitradores utilzia o sufixo X para o reconhecimento de um registrador e o sufixo H ou L é usado para mapeamento dos bits Hihg e Low.  
