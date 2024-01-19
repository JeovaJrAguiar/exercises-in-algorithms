// Play Hash
// Aguiar - computer science
// University Federal of Ceará - campus Crateus

#include <stdio.h>

int main(){
    printf("\n===== Play Hash - C =====");
    printf("\nWhile((exist a free square) and (nobody lost(has won) game))");
    printf("\n  await play adversary, continues");
    printf("\n  If(exist a free square)");
    printf("\n      If(free center)");
    printf("\n          play in the center");
    printf("\n      Else");
    printf("\n          If(adversary has 2 squares inline with the third free)");
    printf("\n              play in this free square");
    printf("\n          Else");
    printf("\n              If(exist any free corner)");
    printf("\n                  play in this free corner");
    printf("\n");
    
    return 0;
}