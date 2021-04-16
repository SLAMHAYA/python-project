from players import personnages
import random

listadj = ["rude",
           "affreux",
           "fichu",
           "satané",
           "pauvre",
           "avare",
           "faible",
           "maiprisable",
           "ennuyeux",
           "sombre",
           ]
listverb = ["abandonnant",
            "suivant",
            "luisant",
            "étant",
            "éblouissant",
            ]
listnom = ["escrement",
           "chef",
           "enfant",
           "Super",
           "cuisto",
           "rat",
           "gosse",
           "crabe",
           "toto",
           "tata", ]
EnsembledeMots = [
    "Je ne comprends pas",
    "Qu est-ce que c est ?",
    "Je voudrais poser une question",
    "Je n ai pas bien compris",
    "les cheveux raides",
]
print("------------------------------OH...SIR GAME--------------------------------------")
player1 = None
player2 = None
print(" joueur1 veuillez entrer votre nom")
nom1 = input()
print("veuiller choisir votre personnage toto/tata ")
j1 = input()
if (j1 == "toto"):
    print("super", nom1, "vous avez choisi toto")
    player1 = personnages(j1)
else:
    print("super", nom1, "vous avez choisi tata")
    player1 = personnages(j1)


print(" joueur2 veuillez entrer enter votre nom")
nom2 = input()
print("veuiller choisir votre personnage toto/tata")
j2 = input()
if (j2 == "toto"):
    print("super", nom2, "vous avez choisi toto")
    player2 = personnages(j2)

else:
    print("super", nom2, "vous avez choisi tata")
    player2 = personnages(j2)

print("veuillez choisir des mots parmis les listes suivantes")
print(listadj, listnom, listverb, EnsembledeMots)

print(" veuillez composer votre phrase", nom1)
p1 = input()
scorej1 = 0
for word in p1.split():
    if(word in personnages(j1).Pfort):
        scorej1 += 3
    else:
        scorej1 += 1
print("votre score est", scorej1)

print(" veuillez composer votre phrase", nom2)
p2 = input()
scorej2 = 0
for word in p2.split():
    if(word in personnages(j2).Pfort):
        scorej2 += 3
    else:
        scorej2 += 1
print(scorej2)

if(scorej1 > scorej2):
    print(nom1, "a gagné")
elif(scorej2 > scorej1):
    print(nom2, "a gagné")

print("------------------------------AND OF THE GAME--------------------------------------")
