import itertools

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
           "toto",
           "chef",
           "enfant",
           "Super",
           "cuisto",
           "rat",
           "gosse",
           "crabe",
           "tata",
           "Tu"]
listlink = ["et",
            "mais",
            "aussi",
            "de",
            "qui"]


class personnages:

    def __init__(self, classe):

        if classe == "toto":
            self.Pfort = list(itertools.chain(
                listadj[3:], listverb[3:], listnom[3:], listlink[3:]))
            self.Pfaible = list(itertools.chain(
                listadj[0:3], listverb[0:3], listnom[0:3], listlink[0:3]))

        elif classe == "tata":
            self.Pfort = listadj[0:3]+listverb[0:3]+listnom[0:3]+listlink[0:3]
            self.Pfaible = listadj[3:]+listverb[3:]+listnom[3:]+listlink[3:]

    def __str__(self):
        return " faiblesses sont " + self.Pfort + " , points forts sont " + str(self.Pfaible)
