%{
        int qtdDecimal = 0;
        int qtdOctal = 0;
        int qtdHexadecimal = 0;
        int qtdReal = 0;
%}

decimal         [1-9][0-9]*
octal           0[0-7]*
hexadecimal     0x[0-9A-Fa-f]+
real       (?:[0-9]*\.[0-9]*)*
branco          [ ]

%%

{decimal}       { printf("Decimal -  %s\n", yytext); qtdDecimal++; }
{octal}         { printf("Octal - %s\n", yytext); qtdOctal++; }
{hexadecimal}   { printf("Hexa - %s\n", yytext); qtdHexadecimal++; }
{real}     { printf("Real -  %s\n", yytext); qtdReal++; }
{branco}        ;

%%


void main(){
        yylex();

        printf("\n %d Decimal \n", qtdDecimal);
        printf("%d Octal \n", qtdOctal);
        printf("%d Hexadecimal \n", qtdHexadecimal);
        printf("%d Real \n", qtdReal);
}
