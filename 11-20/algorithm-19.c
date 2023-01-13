// Basic operations
// Aguiar - computer science
// Federal University of Ceara - crateus campus

#include <stdio.h>
#include <stdlib.h>

// analisar algoritmo logaritmo em <https://linux.ime.usp.br/~lucasmmg/livecd/documentacao/documentos/mac122/floor-lg.html>

float raiz(float numero){
	float precisao = 0.000001;
	float b = numero, a = 1;
	
	printf("\nprecisao - a        - b        - numero");
	while((b-a) >= precisao){
		b = (a+b)/2;
		a = numero / b;

		printf("\n%.6f - %.6f - %.6f - %f", precisao, a, b, numero);
	}

	printf("\n\n%.6f - %.6f - %.6f - %f\n", precisao, a, b, numero);
	return b;
}

int main(){
	printf("\n===== Basic Operations - C =====\n");


	printf("raiz: %.2f . raiz(64)\n", raiz(9));

	return 0;
}
