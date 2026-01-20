import random

numero_secreto = random.randint(1, 1000000)
tentativas = 0

print("Bienvenue dans le jeu le plus complexe qui ait jamais existé !!")
print("J'ai pensé à un numéro entre 1 et 1 000 000, peux-tu deviner ? ")

while True:
    palpite = input("Quel est ton numéro ?")
    palpite = int(palpite) 
    tentativas = tentativas +1

    if palpite == numero_secreto:
        print("Félicitations ! Tu as réussi à"+ str(tentativas)+ " tentatives!")
        break
    elif palpite <numero_secreto:
        print("Très bas")
    else:
        print("Très fort")