# import du package csv
import csv

#création de la fonction  qui récupère les données du fichier csv
la_liste= []
def extraire(url):
    with open(url, "r") as file:
        
        lire= csv.DictReader(file) #cette variable parcours le fichier csv
        for ligne in lire:
            la_liste.append(ligne)  #ajoute chaque ligne du fichier csv dans la liste "la_liste"
            

#création de la fonction "transform" qui transforme chaque élément de la liste en float et ajoute le nom  et le salaire dans une nouvelle liste"la_liste_off"
la_liste_off= []
def transform(la_liste):
    for element in la_liste:
        transformation1=(element['heures_travaillees'])
        salaire= float(transformation1) * 15
        la_liste_off.append({"nom": element['nom'], "salaire": salaire})    #récupère la valeur de nom dans élément de la_liste et l'attribut puis ajoute la valeur de salaire qu'on vient de calculer 
    print(la_liste_off)

#création de la fonction "load" qui charge les données dans un fichier CSV
en_tete=("nom", "salaire")
def load(la_liste_off):
    with open("output_off.csv", "w") as fichier:
        ajouter= csv.writer(fichier, delimiter=",")
        ajouter.writerow(en_tete)

        for element2 in la_liste_off:
            ajouter.writerow((element2["nom"], element2["salaire"]))

#appel des fonctions
etape1= extraire("input.csv")
etape2= transform(la_liste)
etape3= load(la_liste_off)
print(la_liste_off)
