from random import *

tabChoice = ['rock', 'paper', 'scissors']
tabColor = ['\033[1;36m', '\033[1;34m', '\033[1;35m']
score = 0
manche = 3
i = 1
print('\033[1;37m----------------------------------\n The rock - paper - scissors game\n----------------------------------\n')
mode = int(input('\033[1;32m[1] : Beginner\n\033[1;33m[2] : Apprentice\n\033[1;34m[3] : Warrior\n\033[1;31m[4] : Grand Master\n\033[1;37mMode : '))
while i <= manche:
    print(f'\033[1;37m\n-------\nRound {i}\n-------')
    joueur = int(input('\033[1;36m[1] : Rock\n\033[1;34m[2] : Paper\n\033[1;35m[3] : Scissors\033[1;37m\nYour choice : ')) - 1
    ordi = randint(0,2)
    if joueur + 1 == 82:
        score += 8050
        print(f'You chose ancestral well of the great divine !\n\033[1;32mYou won : \033[1;37mwell VS {tabColor[ordi]}{tabChoice[ordi]}\033[0m')
        break
    else:
        print(f'{tabColor[joueur]}You chose {tabChoice[joueur]}\033[1;37m')
        if joueur == ordi - 1 or joueur == ordi + 2:
            print('\033[1;31mYou lost :', end=' ')
        elif joueur == ordi - 2 or joueur == ordi + 1:
            print('\033[1;32mYou won :', end=' ')
            score += 1
        elif joueur == ordi:
            print('Equality :', end=' ')
            manche += 1
            if mode == 1 or mode == 2:
                score += 1
        print(f'{tabColor[joueur]}{tabChoice[joueur]}\033[1;37m VS {tabColor[ordi]}{tabChoice[ordi]}\033[0m')
        i += 1
if score >= 8020:
    print(f'\n\033[1;33;43mRoyal victory !\nScore : {score}, computer : {manche - score}\033[0m')
elif score >= manche / 2 and (mode == 1 or mode == 3):
    print(f'\n\033[1;37;42mVictory !\nScore : {score}, computer : {manche - score}\033[0m')
elif score > manche / 2:
    print(f'\n\033[1;37;42mVictory !\nScore : {score}, computer : {manche - score}\033[0m')
else:
    print(f'\n\033[1;37;41mDefeat !\nScore : {score}, computer : {manche - score}\033[0m')