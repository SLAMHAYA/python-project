import itertools


class personnages:

    def __init__(self, classe):

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
