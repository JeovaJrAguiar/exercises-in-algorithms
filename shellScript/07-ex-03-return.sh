# Expressão
FRASE='Estou aprendendo muito sobre Linux, soh liberdade'

# Busca a palavra 'Linux' na expressão armazenada em 'FRASE'
# executando o grep em modo silencioso.
if echo $FRASE | grep -iwq 'Linux'; then
    echo 'Você está falando sobre Linux.'
fi
