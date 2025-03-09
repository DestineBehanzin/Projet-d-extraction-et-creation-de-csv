# Écrivez votre code ici !
import csv

la_liste= []
def extraire(url):
    with open(url, "r") as file:
        
        lire= csv.DictReader(file)
        for ligne in lire:
            la_liste.append(ligne)
            

la_liste_off= []
def transform(la_liste):
    for element in la_liste:
        transformation1=(element['heures_travaillees'])
        salaire= float(transformation1) * 15
        la_liste_off.append({"nom": element['nom'], "salaire": salaire})
    print(la_liste_off)

en_tete=("nom", "salaire")
def load(la_liste_off):
    with open("output_off.csv", "w") as fichier:
        ajouter= csv.writer(fichier, delimiter=",")
        ajouter.writerow(en_tete)

        for element2 in la_liste_off:
            ajouter.writerow((element2["nom"], element2["salaire"]))

etape1= extraire("input.csv")
etape2= transform(la_liste)
etape3= load(la_liste_off)
print(la_liste_off)
