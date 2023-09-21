# Verifica se o arquivo 'etc/group' existe:
if [ -e /etc/group ]; then
	echo 'Arquivo existe'
else
	echo 'Arquivo nao existe'
fi
