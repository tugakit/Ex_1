import random
chiffre1 = int(input(" Choisissez votre premier numéro de 1 à 100"))
chiffre2 = int(input(" Choisissez votre second numéro de 1 à 100"))
chiffre3 = int(input(" Choisissez votre troisième numéro de 1 à 100"))
win = 1 #random.randint(0, 100)
diff1 = abs(chiffre1 - win)
diff2 = abs(chiffre2 - win)
diff3 = abs(chiffre3 - win)
diflist = [diff1, diff2, diff3]

proche = min(diflist)
if win == chiffre1:
  print ("Vous avez gagné avec votre premier chiffre")
elif win == chiffre2:
  print("Vous avez gagné avec votre deuxeme chiffre")
elif win == chiffre3:
  print("Vous avez gagné avec votre troisieme chiffre")
else:
  print("Aucun de vos chiffres étaient corrects")

if chiffre1 == win:
    print("Chiffre 1") #Dire plus tard quel numéro entre les 3
elif chiffre2 == win:
    print("Chiffre 2") #Dire plus tard quel numéro entre les 3
elif chiffre3 == win:
    print("Chiffre 3")
else:
  print("Vous avez perdu")


print("chiffre 1: \n", chiffre1, "\nchiffre 2:\n", chiffre2, "\nchiffre 3:\n", chiffre3, "\nChiffre gagnant:\n", \
win)