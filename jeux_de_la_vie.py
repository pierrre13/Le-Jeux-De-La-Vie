# Le jeux de la vie est une simulation de cellule. Les cellules sont representés par des cases noirs. 
# Une cellule interagit seulement avec les cellules qui sont autour d'elle dans rayon de une case, diagonale compris.
# Le jeux de la vie fonctionne grace a quatre regle simple:
# Si à un endroit il n'y pas de cellule une cellules va se crée si elle entourer de 3 cellules.
# Une cellule reste en vie si elle entourer de 2 ou 3 cellules.
# Une cellule meure si elle entourer de plus de 4 cellule.
# Une cellule meure si elle entourer de moins de 1 cellule
# Le jeux de la vie n'est pas vraiment un jeux c'est une simulation pour observer comment des organismes qui sont régie par des règles simple peuvent former des choses complexes. 
# Je vous renvoie a la video de Science Etonante sur le sujet qui permet de mieux comprendre la puissance du jeux de la vie.
import random
import copy
import pygame
#def de variable
virgule = ","
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((500,500))
nbr1a500 = list(range(0,500,10))
backround = pygame.Surface((500,500))
backround.fill("White")
lignehorizontal = pygame.Surface((500,1))
lignevertical = pygame.Surface((1,500))
pygame.display.set_caption("Le Jeux De La Vie")
donnes = {}
t = 0
nbraletoire = random.randint(1,10)
noiroublanc = False
case_temporaire = range(1,2500)
#set up case boir ou blanc
for w in nbr1a500:
    for a in nbr1a500:
        nbraletoire = random.randint(1,10)
        if nbraletoire == 1:
            noiroublanc = True
        else:
            print(nbraletoire)
            noiroublanc = False
        donnes[w,a] = noiroublanc

#fenetre de jeux
while True:
    case_temporaire = 0
    #quiter les jeux
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    #actualisation du jeux
    screen.blit(backround,(0,0))
    for i in nbr1a500:
        screen.blit(lignehorizontal,(0,i))
    for i in nbr1a500:
        screen.blit(lignevertical,(i,0))
    
    #transfert donnes
    donnnes_temp = copy.deepcopy(donnes)
    #gestion de noir ou blanc
    for r,p in zip(donnes,donnnes_temp):
        escpace = donnes[r]
        x_carre = r[0]
        y_carre = r[1]
        if escpace == True:
            case_temporaire += 1
            lol = "lol"+str(case_temporaire) 
            lol = pygame.Surface((10,10))
            lol.fill("black")
            screen.blit(lol,(x_carre,y_carre))
            
        nbr_autour = 0
        #droite
        if donnes.get(((x_carre+10),(y_carre)),"nop") == True:
            nbr_autour += 1
        #gauche
        if donnes.get(((x_carre-10),(y_carre)),"nop") == True:
            nbr_autour += 1
        #haut
        if donnes.get(((x_carre),(y_carre-10)),"nop") == True:
            nbr_autour += 1
        #bas
        if donnes.get(((x_carre),(y_carre+10)),"nop") == True:
            nbr_autour += 1
        #bas_gauche
        if donnes.get(((x_carre-10),(y_carre+10)),"nop") == True:
            nbr_autour += 1
        #bas_droite
        if donnes.get(((x_carre+10),(y_carre+10)),"nop") == True:
            nbr_autour += 1
        #haut_gauche
        if donnes.get(((x_carre-10),(y_carre-10)),"nop") == True:
            nbr_autour += 1
        #haut_droite
        if donnes.get(((x_carre+10),(y_carre-10)),"nop") == True:
            nbr_autour += 1

        #gestioncellule:
        if nbr_autour >=4:
            donnnes_temp[p] = False
        if nbr_autour <=1:
            donnnes_temp[p] = False

        if nbr_autour == 3:
            donnnes_temp[p] = True
    donnes = copy.deepcopy(donnnes_temp)
        

    pygame.display.update()
    clock.tick(1)
