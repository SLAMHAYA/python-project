from players import personnages

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
           "un"]
listverb = ["abandonnant",
            "suivant",
            "luisant",
            "etant",
            "éblouissant",
            "abrutissant",
            "affligeant",
            "aggravant",
            "alertant",
            "certifie",
            "es"]
listnom = ["escrement",
           "chef",
           "enfant",
           "Super",
           "cuisto",
           "rat",
           "gosse",
           "crabe",
           "toto",
           "tata",
           "Tu"]
listlink = ["et",
            "mais",
            "aussi",
            "de",
            "qui"]

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
print(listadj, listnom, listverb, listlink)

scorej1 = 0
scorej2 = 0
p1 = None
p2 = None
while p1 != "f" or p2 != "f":

    print(" veuillez composer votre phrase ou tapez f si vous voulez terminer votre phrase", nom1)
    p1 = input()

    for word in p1.split():
        if(word in p1 == "f"):
            break
        elif(word in personnages(j1).Pfort):
            scorej1 += 3
        else:
            scorej1 += 1
    print("votre score est", scorej1)

    print("veuillez composer votre phrase ou tapez f si vous voulez terminer votre phrase", nom2)
    p2 = input()
    for word in p2.split():
        if(word in p2 == "f"):
            break
        elif(word in personnages(j2).Pfort):
            scorej2 += 3
        else:
            scorej2 += 1
    print("votre score est", scorej2)

if(scorej1 > scorej2):
    print(nom1, "a gagné")
elif(scorej2 > scorej1):
    print(nom2, "a gagné")
else:
    print("match nul")

print("------------------------------AND OF THE GAME--------------------------------------")
