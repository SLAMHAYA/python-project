import itertools


class personnages:

    def __init__(self, classe):

        listadj = ["Absolu",
                   "Admirable",
                   "Agréable",
                   "Aimable",
                   "Amusant"]
        listverb = ["abandonner",
                    "accepter",
                    "accompagner",
                    "acheter",
                    "adorer"
                    ]
        listnom = ["aide",
                   "chef",
                   "enfant",
                   "garde",
                   "gauche",
                   "geste",
                   "gosse",
                   "livre"]

        if classe == "toto":
            self.Pfort = list(itertools.chain(
                listadj[3:], listverb[3:], listnom[3:]))
            self.Pfaible = list(itertools.chain(
                listadj[0:3], listverb[0:3], listnom[0:3]))

        elif classe == "tata":
            self.Pfort = listadj[0:3]+listverb[0:3] + listnom[0:3]
            self.Pfaible = listadj[3:]+listverb[3:] + listnom[3:]

    def __str__(self):
        return " faiblesses sont " + self.Pfort + " , points forts sont " + str(self.Pfaible)
