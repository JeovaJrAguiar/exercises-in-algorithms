#!/bin/bash

if [ $# -eq 1 ]; then
        RANDOM=$$

        ps
        correct=$(( RANDOM % $1 ))
        correct=$(( correct + 1 ))

        guess=0

        echo "O numero esta correto"

        count=0

        while [ $guess -ne $correct ]; do
                echo "Adivinhe o numero: "
                read guess

                count=$(( count + 1 ))
                if [ $guess -gt $correct ]; then
                        echo 'Muito alto, tente de novo: '
                elif [ $guess -lt $correct ]; then
                        echo 'Muito baixo, tende novamente: '
                else
                        echo 'Correto'
                fi
        done
else
        echo 'Uso: Adivinhe um numero, onde estara entre 1 e o número passado como parametro'
fi
