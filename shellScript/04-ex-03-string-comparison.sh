
# Testa se a variável de ambiente 'PATH' está vazia.            
if [ -z "$PATH" ];then
        echo 'Vazia'
else
        echo $PATH
fi
