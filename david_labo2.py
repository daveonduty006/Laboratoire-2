import math

# fonction controllant le flux du programme 
def execution():
    dico_teams = compil_equipes()
    exit = False
    while not exit: 
        user_sel = menu()
        while not 0 < user_sel <= 5:
            print("Choix invalide, choisissez une option svp: ")
            user_sel = menu()        
        if user_sel == 1:
            affichage_stats(dico_teams)
        elif user_sel == 2:
            sauvegarde_stats(dico_teams)
        elif user_sel == 3:
            affichage_ecart_type(dico_teams)
        elif user_sel == 4:
            ajout_faute()
        else:
            exit = True

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
    user_selection = int(input("\nMenu d'accueil \n"
                               "1. Afficher les statistiques \n"
                               "2. Sauvegarder les statistiques \n"
                               "3. Afficher l'équipe avec les coureurs les plus similaires \n"
                               "4. Ajouter une faute à une équipe \n"
                               "5. Terminer \n"
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

# fonction présentant un menu à l'utilisateur pour l'ajout de faute dans le fichier txt stats
def ajout_faute():
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




execution()

