// Basic operatons
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

int main(){
	printf("\n===== Basic Operations - C =====\n");


	printf("raiz: %.2f . raiz(64)\n", raiz(64));
	
	return 0;
}
