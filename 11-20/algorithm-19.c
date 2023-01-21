// Basic operations
// Aguiar - computer science
// Federal University of Ceara - crateus campus

#include <stdio.h>
#include <stdlib.h>

// analisar algoritmo logaritmo em <https://linux.ime.usp.br/~lucasmmg/livecd/documentacao/documentos/mac122/floor-lg.html>

float raiz(float numero){
	float precisao = 0.000001;
	float b = numero, a = 1;
	
	while((b-a) >= precisao){
		b = (a+b)/2;
		a = numero / b;
	}
	return b;
}

float powAux(float x, float y){
	float aux = x;
	for(int i=1; i <= y; i++){
		aux = aux * x;
	}
	return aux;
}

int powAuxByInteger(int x, int y){
        float aux = x;
        for(int i=1; i < y; i++){
                aux = aux * x;
        }
        return aux;
}

int main(){
	printf("\n===== Basic Operations - C =====\n");
	
	printf("raiz: %.2f          raiz(64)\n", raiz(64));
	printf("exponencial: %d     expo(%d, %d)\n", powAuxByInteger(4, 3), 4, 3);

	return 0;
}
