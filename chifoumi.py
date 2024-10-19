from random import *

tabChoice = ['pierre', 'feuille', 'ciseaux']
tabColor = ['\033[1;36m', '\033[1;34m', '\033[1;35m']
score = 0
manche = 3
i = 1
print('\033[1;37m-----------------------------------\nLe Jeu du pierre - feuille - ciseau\n-----------------------------------\n')
mode = int(input('\033[1;32m[1] : Débutant\n\033[1;33m[2] : Apprentie\n\033[1;34m[3] : Combattant\n\033[1;31m[4] : Grand Maître\n\033[1;37mMode : '))
while i <= manche:
    print(f'\033[1;37m\n-------\nManche {i}\n-------')
    joueur = int(input('\033[1;36m[1] : Pierre\n\033[1;34m[2] : Feuille\n\033[1;35m[3] : Ciseaux\033[1;37m\nVotre choix : ')) - 1
    ordi = randint(0,2)
    if joueur + 1 == 82:
        score += 8050
        print(f'Vous avez choisi puit ancestrale du grand divin !\nPuit\033[1;37m VS {tabColor[ordi]}{tabChoice[ordi]}\033[0m')
        break
    else:
        print(f'{tabColor[joueur]}Vous avez choisi {tabChoice[joueur]}\033[1;37m')
        if joueur == ordi - 1 or joueur == ordi + 2:
            print('\033[1;31mVous avez perdu :', end=' ')
        elif joueur == ordi - 2 or joueur == ordi + 1:
            print('\033[1;32mVous avez gagné :', end=' ')
            score += 1
        elif joueur == ordi:
            print('Egalite :', end=' ')
            manche += 1
            if mode == 1 or mode == 3:
                score += 1
        print(f'{tabColor[joueur]}{tabChoice[joueur]}\033[1;37m VS {tabColor[ordi]}{tabChoice[ordi]}\033[0m')
        i += 1
if score >= 8020:
    print(f'\n\033[1;33;43mVictoire Royal !\nScore : {score}, ordinateur : {manche - score}\033[0m')
elif score >= manche // 2 and (mode == 1 or mode == 2):
    print(f'\n\033[1;37;42mVictoire !\nScore : {score}, ordinateur : {manche - score}\033[0m')
elif score > manche // 2:
    print(f'\n\033[1;37;42mVictoire !\nScore : {score}, ordinateur : {manche - score}\033[0m')
else:
    print(f'\n\033[1;37;41mDéfaite !\nScore : {score}, ordinateur : {manche - score}\033[0m')