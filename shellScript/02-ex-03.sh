#testes condicionais aninhados
idade=30

if [ $idade -eq 24 ];then
        echo 'hmmm suspeito demais '
else [ $idade -eq 24 ];then
        echo 'rico bem novinho'
else [ $idade -eq 24 ];then
        echo 'fica esperto, ta ficando velho'
fi
