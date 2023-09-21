# Testa se o usuario tem permissao de escrita em um determinado arquivo:
if [ ! -w /etc/shadow ]; then
	echo 'Voce nao possui permissao de escrita neste arquivo'
	exit 1
fi
