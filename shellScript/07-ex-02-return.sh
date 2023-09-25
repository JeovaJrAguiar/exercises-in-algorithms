#executa o comando e testa o código de retorno.
if ls /etc/group &>/dev/null;then
    echo 'Arquivo existe'
else
    echo 'Arquivo não encontrado'
fi
