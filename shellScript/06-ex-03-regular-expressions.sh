nome='marcos'

#casa qualquer nome iniciado com 'mar'
if [[ $nome = mar* ]]; then
    echo 'nome valido'
else
    echo 'nome invalido'
fi
