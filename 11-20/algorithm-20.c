// Basic operations
// Aguiar - computer science
// Federal University of Ceara - crateus campus

#include <stdio.h>
#include <stdlib.h>

int main(){
	char word[30], word2[30], d[30], d2[30];

	printf("\n===== String Manipulatoin - C =====\n");
	printf("Write WORD: ");
        scanf(" %s", &word);
	printf("Write WORD: ");
        scanf(" %s", &word2);	
	 
	printf("\nSize first word: %d", strlen(word));
	strcat(word, word2);
	printf("\nConcatenation: %s", word);

	printf("\nFirst letter: %c", word[0]);
	printf("\nLast letter: %c", word[strlen(word) - 1]);
	
	printf("\nAll but  the first letter: ");
	for(int i=1; i< strlen(word); i++)
		printf("%c", word[i]);
	
	
	printf("\n");
	return 0;
}

