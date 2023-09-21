# Verifica se a opcao 'noclobber' esta ativada
if [ -o noclobber ]; then
	echo 'Seus arquivos estao protegidos'
fi
