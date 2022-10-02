import pygame
from time import sleep
print('-=-' * 20)
# COLOQUE SEU NOME PARA COMEÇAR
nome = str(input(f'Digite seu nome para começar: '))
print('-=-' * 20)
print(f'Olá \033[0;34m{nome}\033[m seja bem vindo ao \033[1;31mJOGO DA ADIVINHAÇÃO \033[m\033[1;97mV1.0\033[m')
print('-=-' * 20)
sleep(2.2)
print(f'Você gostaria de jogar acompanhado da trilha sonora? \033[1;92m(Digite SIM ou NAO)\033[m')
print('')
sleep(0.1)
al1 = str(input('Resposta: ')).upper()
if al1 == 'NAO':
    print('OK! Então vamos continuar a apresentação do jogo')
    sleep(1.5)
    print('')
    print('-=-' * 16)
    print("""Logo abaixo mostraremos o menu do jogo:

              [1] \033[1;97mIniciar\033[m
              [2] \033[1;97mInformações\033[m
              [3] \033[1;97mCreditos\033[m
              [4] \033[1;97mLigar a Música\033[m
              """)
    escolha1 = ''
    if escolha1 == '4':
        print('-=-' * 20)
        print('\033[1mVocê acaba de iniciar a música do jogo\033[m')
        print('-=-' * 20)
        pygame.init()
        pygame.mixer.music.load('C:/Users/Conta/Downloads/anime1.mp3')
        pygame.mixer.music.play()
        pygame.event.wait()
        print(' ')
        iniciov1 = input('\033[4;97mPRESSIONE ENTER PARA CONTINUAR PARA O JOGO:\033[m ').strip()
        sleep(1.5)
        print('')
        print('-=-' * 16)
        # MENU DO JOGO:
        print("""Logo abaixo mostraremos o menu do jogo:

                  [1] \033[1;97mIniciar\033[m
                  [2] \033[1;97mInformações\033[m
                  [3] \033[1;97mCreditos\033[m
                  [4] \033[1;97mDesligar a Música\033[m
                  """)



else:
    print('-=-' * 20)
    print('\033[1mVocê acaba de iniciar a música do jogo\033[m')
    print('-=-' * 20)
    pygame.init()
    pygame.mixer.music.load('C:/Users/Conta/Downloads/anime1.mp3')
    pygame.mixer.music.play()
    pygame.event.wait()
    print(' ')
    iniciov1 = input('\033[4;97mPRESSIONE ENTER PARA CONTINUAR PARA O JOGO:\033[m ').strip()
    sleep(1.5)
    print('')
    print('-=-' * 16)
    # MENU DO JOGO:
    print("""Logo abaixo mostraremos o menu do jogo:

          [1] \033[1;97mIniciar\033[m
          [2] \033[1;97mInformações\033[m
          [3] \033[1;97mCreditos\033[m
          [4] \033[1;97mDesligar a Música\033[m
          """)

# OPÇÕES ALTERNATIVAS:
s1 = input('Digite alguma opção para continuar: ')
print('')
# OPÇÃO ALTERNATIVA (N1)
if s1 == '1':
    print(), sleep(1)
# OPÇÃO ALTERNATIVA (N2)
if s1 == '2':
    print(), sleep(0.6)
    print('\033[1;37m-=-\033[m' * 50)
    print()
    print("""       \033[1;97mEste jogo foi desenvolvido por uma única pessoa com o objetivo de fazer com que as pessoas possam se divertir,
                      e exercitar seu cérebro em um jogo, na qual tem a simples proposta de testar seu raciocínio\033[m.
             \033[1;97mO jogo consiste em você adivinhar "palavras aleatorias", com base em dicas que o jogo lhe proporciona 
                  para que você possa adivinhar palavras relativamente difíceis e ai subindo de nivel\033[m.

              \033[7;91m      OBS: O jogo está ainda em desenvolvimento e sofrerá atualizações constantes!!\033[m""")
    print()
    print('\033[1;37m-=-\033[m' * 50)
    print()
    input('Digite a opção \033[1;97m[4]\033[m para voltar ao menu do jogo: ')
    print()
    print('-=-' * 30)
    print('\033[1;93mProcessando...\033[m'), sleep(3.5)
    print('-=-' * 30)
    print()
# MENU ALTERNATIVO 1 (N2):
    print("""Voltamos ao menu do jogo:

      [1] \033[1;97mIniciar\033[m
      [2] \033[1;97mCreditos\033[m
      [3] \033[1;97mDesligar a Música\033[m
      """)
    s1 = input('Digite alguma opção para continuar: ')
    if s1 == '2':
        sleep(1)
        print('-=-' * 20)
        print()
        print('\033[1;97m             Desenvolvedor do Jogo: \033[1;36mCrowZek\033[m')
        print()
        print('-=-' * 20)
        print(' ')
        sleep(1)
        input('Digite a opção \033[1;97m[4]\033[m para voltar ao menu do jogo: ')
        print()
        print('-=-' * 20)
        print('\033[1;93mProcessando...\033[m'), sleep(3.5)
        print('-=-' * 20)
        print()
# MENU ALTERNATIVO 2 (N2):
        print("""Voltamos ao menu do jogo:

                 [1] \033[1;97mIniciar\033[m
                 """
              )
        print(' ')
        s1 = input('Digite alguma opção para continuar: ')
# OPÇÃO ALTERNATIVA (N3)
if s1 == '3':
    sleep(1)
    print('-=-' * 20)
    print()
    print('\033[1;97m             Desenvolvedor do Jogo: \033[1;36mCrowZek\033[m')
    print()
    print('-=-' * 20)
    sleep(1)
    input('Digite a opção \033[1;97m[4]\033[m para voltar ao menu do jogo: ')
    print(' ')
    print('-=-' * 20)
    print('\033[1;93mProcessando...\033[m'), sleep(2.5)
    print('-=-' * 20)
    print(' ')
# MENU ALTERNATIVO 1 (N3)
    print("""Voltamos ao menu do jogo:

          [1] \033[1;97mIniciar\033[m
          [2] \033[1;97mInformações\033[m
          """)
    s1 = input('Digite alguma opção para continuar: ')
    if s1 == '2':
        print(' '), sleep(1.1)
        print('\033[1;37m-=-\033[m' * 50)
        print(' ')
        print("""       \033[1;97mEste jogo foi desenvolvido por uma única pessoa com o objetivo de fazer com que as pessoas possam se divertir,
                    e exercitar seu cérebro em um jogo, na qual tem a simples proposta de testar seu raciocínio\033[m.
           \033[1;97mO jogo consiste em você adivinhar "palavras aleatorias", com base em dicas que o jogo lhe proporciona 
                para que você possa adivinhar palavras relativamente difíceis e ai subindo de nivel\033[m.

            \033[7;91m      OBS: O jogo está ainda em desenvolvimento e sofrerá atualizações constantes!!\033[m""")
        print(' ')
        print('\033[1;37m-=-\033[m' * 50)
        print(' ')
        sleep(2.1)
        sleep(1)
        input('Digite a opção \033[1;97m[4]\033[m para voltar ao menu do jogo: ')
        print(' ')
        print('-=-' * 20)
        print('\033[1;93mProcessando...\033[m'), sleep(2.5)
        print('-=-' * 20)
        print(' ')
        print("""Voltamos ao menu do jogo:

                        [1] \033[1;97mIniciar\033[m
                        """

              ), sleep(2)
        print()
        s1 = input('Digite alguma opção para continuar: ')
# OPÇÃO DA MUSICA OUTRA ALTERNATIVA
if s1 == '4':
    pygame.mixer.music.stop()
    print('-=-' * 15)
    print('Você acabou de desligar a música do jogo')
    print('-=-' * 15)
    print(' ')
    iniciov1 = input('\033[4;97mPRESSIONE ENTER PARA CONTINUAR PARA O JOGO:\033[m ').strip()
    sleep(1.5)
    print('')
    print('-=-' * 16)
    # MENU DO JOGO:
    print("""Logo abaixo mostraremos o menu do jogo:

          [1] \033[1;97mIniciar\033[m
          [2] \033[1;97mInformações\033[m
          [3] \033[1;97mCreditos\033[m
          """)
    s1 = input('Digite alguma opção para continuar: ')
    if s1 == '2':
        print(), sleep(0.6)
        print('\033[1;37m-=-\033[m' * 50)
        print()
        print("""       \033[1;97mEste jogo foi desenvolvido por uma única pessoa com o objetivo de fazer com que as pessoas possam se divertir,
                              e exercitar seu cérebro em um jogo, na qual tem a simples proposta de testar seu raciocínio\033[m.
                     \033[1;97mO jogo consiste em você adivinhar "palavras aleatorias", com base em dicas que o jogo lhe proporciona 
                          para que você possa adivinhar palavras relativamente difíceis e ai subindo de nivel\033[m.

                      \033[7;91m      OBS: O jogo está ainda em desenvolvimento e sofrerá atualizações constantes!!\033[m""")
        print()
        print('\033[1;37m-=-\033[m' * 50)
        print()
        input('Digite a opção \033[1;97m[4]\033[m para voltar ao menu do jogo: ')
        print()
        print('-=-' * 30)
        print('\033[1;93mProcessando...\033[m'), sleep(3.5)
        print('-=-' * 30)
        # MENU ALTERNATIVO 1 (N2):
        print("""Voltamos ao menu do jogo:

              [1] \033[1;97mIniciar\033[m
              [2] \033[1;97mCreditos\033[m""")
        print(' ')
        s1 = input('Digite alguma opção para continuar: ')
        if s1 == '2':
            sleep(1)
            print('-=-' * 20)
            print()
            print('\033[1;97m             Desenvolvedor do Jogo: \033[1;36mCrowZek\033[m')
            print()
            print('-=-' * 20)
            print(' ')
            sleep(1)
            input('Digite a opção \033[1;97m[4]\033[m para voltar ao menu do jogo: ')
            print()
            print('-=-' * 20)
            print('\033[1;93mProcessando...\033[m'), sleep(3.5)
            print('-=-' * 20)
            print()
            print("""Voltamos ao menu do jogo:

                         [1] \033[1;97mIniciar\033[m""")

    if s1 == '3':
        sleep(1)
        print('-=-' * 20)
        print()
        print('\033[1;97m             Desenvolvedor do Jogo: \033[1;36mCrowZek\033[m')
        print()
        print('-=-' * 20)
        print(' '),  sleep(1)
        input('Digite a opção \033[1;97m[4]\033[m para voltar ao menu do jogo: ')
        print()
        print('-=-' * 20)
        print('\033[1;93mProcessando...\033[m'), sleep(3.5)
        print('-=-' * 20)
        print()
        print("""Voltamos ao menu do jogo:

          [1] \033[1;97mIniciar\033[m
          [2] \033[1;97mInformações\033[m""")

        print('')
        s1 = input('Digite alguma opção para continuar: ')
        if s1 == '2':
            print(), sleep(0.6)
            print('\033[1;37m-=-\033[m' * 50)
            print()
            print("""       \033[1;97mEste jogo foi desenvolvido por uma única pessoa com o objetivo de fazer com que as pessoas possam se divertir,
                                  e exercitar seu cérebro em um jogo, na qual tem a simples proposta de testar seu raciocínio\033[m.
                         \033[1;97mO jogo consiste em você adivinhar "palavras aleatorias", com base em dicas que o jogo lhe proporciona 
                              para que você possa adivinhar palavras relativamente difíceis e ai subindo de nivel\033[m.

                          \033[7;91m      OBS: O jogo está ainda em desenvolvimento e sofrerá atualizações constantes!!\033[m""")
            print()
            print('\033[1;37m-=-\033[m' * 50)
            print()
            input('Digite a opção \033[1;97m[4]\033[m para voltar ao menu do jogo: ')
            print()
            print('-=-' * 30)
            print('\033[1;93mProcessando...\033[m'), sleep(3.5)
            print('-=-' * 30)
            print()
            # MENU ALTERNATIVO MUSICA:
            print("""Voltamos ao menu do jogo:

                  [1] \033[1;97mIniciar\033[m""")

            if s1 == '3':
                sleep(1)
                print('-=-' * 20)
                print()
                print('\033[1;97m             Desenvolvedor do Jogo: \033[1;36mCrowZek\033[m')
                print()
                print('-=-' * 20)
                print(' ')
                sleep(1)
                input('Digite a opção \033[1;97m[4]\033[m para voltar ao menu do jogo: ')
                print()
                print('-=-' * 20)
                print('\033[1;93mProcessando...\033[m'), sleep(3.5)
                print('-=-' * 20)
                print()
                print("""Voltamos ao menu do jogo:

                             [1] \033[1;97mIniciar\033[m""")

