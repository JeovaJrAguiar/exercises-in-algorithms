num=14

#verifica se o numero esta dentro do intervalo                  
# (num >= 10) ou (num <=20)                                     
echo 'Intervalo MAIOR OU IGUAL A 10 e MENOR OU IGUAL A 20'

if [ $num -ge 10 -o $num -lt 20 ];then
        echo 'Dentro do intervalo'
else
        echo 'Fora do intervalo'
fi
