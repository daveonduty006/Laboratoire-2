#Laboratoire 2:
#Vous devez implémenter un simple programme permettant à une ligue de course maison d'interpréter
#leurs statistiques. Vous recevez 3 documents texte ayant le nom de chaque équipe suivi du temps
# de course de la semaine des 5 coureurs par équipe.

#Étape 1:
#Lire les trois documents: data1.txt, data2.txt et data3.txt

#Étape 2:
#Offrir un menu à l'utilisateur avec les options suivantes:
#Afficher les statistiques
#Sauvegarder les statistiques
#Afficher l'équipe avec les coureurs les plus similaires
#Ajouter une faute à une équipe.

#Étape 3 (afficher les statistiques):
#Vous devez afficher les statistiques suivantes :
#Équipe ayant le coureur le plus rapide et le temps de ce dernier.
#Temps moyens par équipe présenté en ordre croissant, donc de l'équipe la plus rapide à la plus 
#lente. Vous devez y afficher le nom de l'équipe et leur temps de course moyen.

#Étape 4:
#Vous devez sauvegarder les statistiques de l'étape 3 dans un fichier intitulé stats.txt.

#Étape 5:
#Vous devez calculer l'écart type de chaque équipe et afficher à la console celle avec le plus 
#petit écart type.
#La formule de l'écart type pour une équipe de 5 est la suivante:
#écart type = sqrt(Sum(pow(data - avg, 2))/5)
#Faites attention d'utiliser la moyenne de l'équipe respective.

#Étape 6:
#Vous devez offrir un sous-menu permettant à l'utilisateur d'ajouter une faute à chaque équipe 
#sans avoir à exécuter votre programme plusieurs fois. Les fautes ajoutée, s'il y a lieu, doivent 
#être ajoutée à la fin du document stats.txt. (Vous pouvez assumer que l'utilisateur va utiliser 
#l'option 2 avant l'option 4).
#Assurez-vous de ne pas effacer les statistiques déjà présentes.

import math

# fonction controllant le flux du programme 
def appels_fonctions():
    dico_teams = compil_equipes()
    user_sel = menu()
    if user_sel == 1:
        affichage_stats(dico_teams)
    elif user_sel == 2:
        sauvegarde_stats(dico_teams)
    elif user_sel == 3:
        affichage_ecart_type(dico_teams)
    elif user_sel == 4:
        ajout_faute(dico_teams)
    else:
        print("Votre choix est invalide")
    return 

# fonction compilant les bases de données dans un dictionnaire 
def compil_equipes():
    f1 = open("data1.txt", "r", encoding="utf8")
    f2 = open("data2.txt", "r", encoding="utf8")
    f3 = open("data3.txt", "r", encoding="utf8")

    liste_equipeA = f1.readlines() 
    liste_equipeB = f2.readlines()
    liste_equipeC = f3.readlines() 

    f1.close()
    f2.close()
    f3.close()
    # début d'avoir hâte de pouvoir utiliser des boucles
    liste_equipeA[1] = float(liste_equipeA[1])
    liste_equipeA[2] = float(liste_equipeA[2])
    liste_equipeA[3] = float(liste_equipeA[3])
    liste_equipeA[4] = float(liste_equipeA[4])
    liste_equipeA[5] = float(liste_equipeA[5])

    liste_equipeB[1] = float(liste_equipeB[1])
    liste_equipeB[2] = float(liste_equipeB[2])
    liste_equipeB[3] = float(liste_equipeB[3])
    liste_equipeB[4] = float(liste_equipeB[4])
    liste_equipeB[5] = float(liste_equipeB[5])

    liste_equipeC[1] = float(liste_equipeC[1])
    liste_equipeC[2] = float(liste_equipeC[2])
    liste_equipeC[3] = float(liste_equipeC[3])
    liste_equipeC[4] = float(liste_equipeC[4])
    liste_equipeC[5] = float(liste_equipeC[5])
    # fin d'avoir hâte de pouvoir utiliser des boucles 
    dico_equipes = {'A' : liste_equipeA[1:6], 'B' : liste_equipeB[1:6], 'C' : liste_equipeC[1:6]}

    return dico_equipes

# fonction présentant un menu de sélection à l'utilisateur
def menu():
    user_selection = int(input("Menu d'accueil \n"
                               "1. Afficher les statistiques \n"
                               "2. Sauvegarder les statistiques \n"
                               "3. Afficher l'équipe avec les coureurs les plus similaires \n"
                               "4. Ajouter une faute à une équipe \n"
                               "Choisissez l'une des options: "))

    return user_selection

# fonction affichant à l'écran les statistiques demandées à l'étape 3 
def affichage_stats(dico_entrant):
    cle_meilleur_temps = min(dico_entrant, key=dico_entrant.get)
    print(f"\nLe meilleur coureur se trouve dans l'équipe {cle_meilleur_temps} et son "
          f"temps est {min(dico_entrant[cle_meilleur_temps])}\n")

    moyenne_equipeA = f"{sum(dico_entrant['A'])/len(dico_entrant['A']):.3f}"
    moyenne_equipeB = f"{sum(dico_entrant['B'])/len(dico_entrant['B']):.3f}"
    moyenne_equipeC = f"{sum(dico_entrant['C'])/len(dico_entrant['C']):.3f}"
    liste_moyenne = [moyenne_equipeA+": Équipe A", moyenne_equipeB+": Équipe B", \
                     moyenne_equipeC+": Équipe C"]
    print(f"Moyennes des équipes: \n" 
          f"{sorted(liste_moyenne)}\n")

    return 

# fonction indiquant dans un fichier txt 'stats' les statistiques demandées à l'étape 3
def sauvegarde_stats(dico_entrant):
    cle_meilleur_temps = min(dico_entrant, key=dico_entrant.get)
    meilleur_temps_equipe = (f"Le meilleur coureur se trouve dans l'équipe {cle_meilleur_temps} et "
                             f"son temps est {min(dico_entrant[cle_meilleur_temps])}")

    moyenne_equipeA = f"{sum(dico_entrant['A'])/len(dico_entrant['A']):.3f}"
    moyenne_equipeB = f"{sum(dico_entrant['B'])/len(dico_entrant['B']):.3f}"
    moyenne_equipeC = f"{sum(dico_entrant['C'])/len(dico_entrant['C']):.3f}"
    liste_moyenne = [moyenne_equipeA+": Équipe A", moyenne_equipeB+": Équipe B", \
                     moyenne_equipeC+": Équipe C"]
    liste_moyenne_croissant = sorted(liste_moyenne)
        
    sauvegarde = open("stats.txt", "w", encoding="utf8")
    sauvegarde.write(f"{meilleur_temps_equipe}\n")
    sauvegarde.write(f"\nMoyennes des équipes: \n"
                     f"{liste_moyenne_croissant}\n")
    sauvegarde.close()
 
    return 

# fonction affichant le plus petit écart-type parmi les équipes 
def affichage_ecart_type(dico_entrant):
    moyenne_equipeA = sum(dico_entrant['A'])/len(dico_entrant['A'])
    moyenne_equipeB = sum(dico_entrant['B'])/len(dico_entrant['B'])
    moyenne_equipeC = sum(dico_entrant['C'])/len(dico_entrant['C'])

    prep_ECTY_equipeA = [(pow(dico_entrant['A'][0]-moyenne_equipeA, 2)), \
                         (pow(dico_entrant['A'][1]-moyenne_equipeA, 2)), \
                         (pow(dico_entrant['A'][2]-moyenne_equipeA, 2)), \
                         (pow(dico_entrant['A'][3]-moyenne_equipeA, 2)), \
                         (pow(dico_entrant['A'][4]-moyenne_equipeA, 2))]
    ecart_type_equipeA = math.sqrt(sum(prep_ECTY_equipeA)/5)

    prep_ECTY_equipeB = [(pow(dico_entrant['B'][0]-moyenne_equipeB, 2)), \
                         (pow(dico_entrant['B'][1]-moyenne_equipeB, 2)), \
                         (pow(dico_entrant['B'][2]-moyenne_equipeB, 2)), \
                         (pow(dico_entrant['B'][3]-moyenne_equipeB, 2)), \
                         (pow(dico_entrant['B'][4]-moyenne_equipeB, 2))]
    ecart_type_equipeB = math.sqrt(sum(prep_ECTY_equipeB)/5)    

    prep_ECTY_equipeC = [(pow(dico_entrant['C'][0]-moyenne_equipeC, 2)), \
                         (pow(dico_entrant['C'][1]-moyenne_equipeC, 2)), \
                         (pow(dico_entrant['C'][2]-moyenne_equipeC, 2)), \
                         (pow(dico_entrant['C'][3]-moyenne_equipeC, 2)), \
                         (pow(dico_entrant['C'][4]-moyenne_equipeC, 2))]
    ecart_type_equipeC = math.sqrt(sum(prep_ECTY_equipeC)/5)

    dico_ECTY_equipes = {'A' : ecart_type_equipeA, 'B' : ecart_type_equipeB, 'C' : ecart_type_equipeC}
    cle_equipe_pp_ECTY = min(dico_ECTY_equipes, key=dico_ECTY_equipes.get)
    print(f"\nL'équipe avec le plus petit écart type est l'équipe {cle_equipe_pp_ECTY} avec "
          f"{dico_ECTY_equipes[cle_equipe_pp_ECTY]:.3f}\n")
                                       
    return

# fonction présentant un menu à l'utilisateur pour l'ajout de faute dans le fichier txt stats
def ajout_faute(dico_entrant):
    user_selection = int(input("\nListe des équipes \n"
                               "1. Équipe A \n"
                               "2. Équipe B \n"
                               "3. Équipe C \n"
                               "4. Toutes les équipes \n"
                               "À quelle équipe voulez-vous ajouter une faute?: "))

    update = open("stats.txt", "a", encoding="utf8")
    update.write("\nFautes accumulées: \n")
    
    if user_selection == 1: 
        update.write("1 faute pour l'équipe A\n")
    elif user_selection == 2:
        update.write("1 faute pour l'équipe B\n")
    elif user_selection == 3:
        update.write("1 faute pour l'équipe C\n")
    elif user_selection == 4:
        update.write("1 faute pour chaque équipe\n")
    else:
        print("Votre choix est invalide")

    update.close()

    return




appels_fonctions()

