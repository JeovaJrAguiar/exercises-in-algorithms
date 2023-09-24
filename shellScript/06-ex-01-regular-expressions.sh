num=35623456

# valida se num eh par
if [[ $num =~ ^[0-9]*[02468]$ ]]; then
        echo 'O numero eh par'
else
        echo 'O numero eh impar'
fi
