num=24

# Verifica se o valor é um inteiro negativo ou positivo.
if [[ $num = ?(+|-)+([0-9]) ]];then
    echo 'nuero'
else
    echo 'string'
fi
