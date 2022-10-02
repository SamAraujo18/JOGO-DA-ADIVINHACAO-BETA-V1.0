import random
from time import sleep
print(' ')
print("""\033[1mSelecione a Dificuldade do jogo:\033[m

             [1] \033[1;97mFácil\033[m
             [2] \033[1;97mMédio\033[m
             [3] \033[1;97mDificil\033[m
             [4] \033[1;97mMuito Dificil\033[m
             """)
r1 = str(input('\033[1mSelecione a Dificuldade: \033[m'))
print('\033[0;97n-=-\033[m' * 25)
print('\033[0;36mProcessando...\033[m')
print('-=-' * 25) , sleep(5)
print('\033[1;97mLevel\033[m \033[0;31m1\033[m\033[1m\033[1;97m:\033[m')
sleep(0.1)
print('\033[1m1° - Qual é o animal parecido com o cavalo que possui listras brancas e pretas?\033[m')
print('')
r2 = input('\033[1;32mResposta\033[m\033[1;37m:\033[m ').upper()
