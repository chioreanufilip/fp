import random
def scherre_stein_papier():
    stein = '''
        ___
    ---'   __)
          (___)
          (___)
          (__)
    ---._(__)
    '''

    papier = '''
        ___
    ---'   _)_
              __)
              ___)
             ___)
    ---.____)
    '''

    scherre = '''
        ___
    ---'   _)_
              __)
           ____)
          (__)
    ---._(__)
    '''
    spiel = [scherre, stein, papier]        #Hier wahlt der Computer sein Zeichen
    random_choice = random.choice(spiel)
    score_player = 0
    score_pc = 0
    while score_pc + score_player <= 2:
        choice = input(
        """
        scherre                     
        stein
        papier
        """)
        if choice == 'scherre':
            print('Du:'+scherre + '\nGegner:'+random_choice)
            if random_choice == stein:      #Mit alle diesen if-Funktionen wird der Score definiert
                score_pc += 1
            elif random_choice == papier:
                score_player += 1
        elif choice == 'stein':
            print('Du:'+stein + '\nGegner:'+random_choice)
            if random_choice == papier:
                score_pc += 1
            elif random_choice == scherre:
                score_player += 1
        elif choice == 'papier':
            print('Du:'+papier + '\nGegner:'+random_choice)
            if random_choice == scherre:
                score_pc += 1
            elif random_choice == stein:
                score_player += 1
        print('Du: ' + str(score_player))
        print('Gegner: ' + str(score_pc))
    if score_player > score_pc:
        print("Ich gratuliere Sie um ihren Gewinn")
    else :
        print('Du hast verloren, bitte versuchen Sie noch ein Mal ')

scherre_stein_papier()