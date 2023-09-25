# o arquivo de retorno do ultmo camando executado fica armazenado na variavel $?
# Informando se o comando foi executado corretamente (retorn: 0) ou ocorreu alguma falha (diferente de: 0)

ls arquivo &>/dev/null

# verificando o codigo de retorno
if [ $? -eq 0 ];then
        echo 'Arquivo existe'
else
        echo 'Arquivo nao encontrado'
fi
