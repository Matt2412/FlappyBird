## 1)Import et initialisation des modules
from random import randint
import pygame
import sys
import os
#import pygame.sprite as sprite
from pygame.locals import *
pygame.init()

def charger_image(fichier_image):
    img = pygame.image.load(fichier_image)
    img.convert()
    img.set_colorkey(img.get_at((0, 0)))
    return img


def charger_image2(fichier_image):
    img = pygame.image.load(fichier_image)
    img.convert()
    return img


def charger_image_credits(ecran, chrono, fond):
    creditsimagex = 30
    creditsimagey = 500
    creditsimage = charger_image('credits.png')
    while creditsimagey > -60:
        creditsimagey -= 2
        chrono.tick(70)
        ecran.blit(fond, (0, 0))
        ecran.blit(creditsimage, (creditsimagex, creditsimagey))
        pygame.display.flip()


def mouvement_objet(chrono, ecran, fond, objet, x, y):
    chrono.tick(80)
    ecran.blit(fond, (0, 0))
    ecran.blit(objet, (x, y))
    pygame.display.flip()

def faire_anim_debut(ecran, chrono, fond, titre, credits, playbutton, image_flappies, tout_rejouer):
    titrex_fixe = 100
    titrey_final = 180
    playbuttonx_fixe = 150
    playbuttony_final = 260
    creditsx_final = playbuttonx_fixe
    creditsy_fixe = 300
    
    flappies_x_final = (350, 290, 230, 170, 110)
    flappies_y_fixe = (130, 110, 110, 120, 130)

    if tout_rejouer:
        titrex = 100
        titrey = 0
        playbuttonx = 150
        playbuttony = 500
        creditsx = 500
        creditsy = 300
        flappies_x = [0, 0, 0, 0, 0]

        while titrey < titrey_final:
            titrey += 2
            mouvement_objet(chrono, ecran, fond, titre, titrex, titrey)

        while playbuttony > playbuttony_final:
            playbuttony -= 2
            mouvement_objet(chrono, ecran, fond, playbutton, playbuttonx, playbuttony)

        while creditsx > creditsx_final:
            creditsx -= 2
            mouvement_objet(chrono, ecran, fond, credits, creditsx, creditsy)

        for i, img_flappy in enumerate(image_flappies):
            while flappies_x[i] < flappies_x_final[i]:
                flappies_x[i] += 3
                mouvement_objet(chrono, ecran, fond, img_flappy, flappies_x[i], flappies_y_fixe[i])

    ecran.blit(titre, (titrex_fixe, titrey_final))
    ecran.blit(playbutton, (playbuttonx_fixe, playbuttony_final))
    ecran.blit(credits, (creditsx_final, creditsy_fixe))
    for i, img_flappy in enumerate(image_flappies):
        ecran.blit(img_flappy, (flappies_x_final[i], flappies_y_fixe[i]))
    pygame.display.flip()

def menuprincipal():
    ecran = pygame.display.set_mode((500, 500))
    ecran.fill((38, 196, 236))
    ecran_rect = ecran.get_rect()
    fond = pygame.Surface((500, 500))
    fond.fill((38, 196, 236))

    ## Chargement des images du menu principal et définition de leurs coordonnées

    titre = charger_image('Titre-Flappy.png')
    playbutton = charger_image('Bouton-Play.png')
    image_flappies = (charger_image('50x50bleu.png'), charger_image('50x50gris.png'), 
                      charger_image('50x50jaune.png'), charger_image('50x50rouge.png'), charger_image('50x50vert.png'))
    credits = charger_image('credits-titre.png')

    ## Animation du menu

    chrono = pygame.time.Clock()

    faire_anim_debut(ecran, chrono, fond, titre, credits, playbutton, image_flappies, True)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:  # Croix rouge
                pygame.display.quit()
            elif event.type == KEYDOWN:
                if event.key == K_y:
                    score = jeu()
                    ecrire_score(score)
                    faire_anim_debut(ecran, chrono, fond, titre, credits, playbutton, image_flappies,True)
                elif event.key == K_n:
                    pygame.display.quit()    
                elif event.key == K_c:
                    charger_image_credits(ecran, chrono, fond)
                    faire_anim_debut(ecran, chrono, fond, titre, credits, playbutton, image_flappies, False)

## Definition de la fonction jeu()
def jeu():
    ## Chargement des images

    FlappyHasard = randint(1, 5)  # A CHANGER CAD ON MET CA COMME DES RECOMPENSES A DEBLOQUER EN FONCTION
    if FlappyHasard == 1:  # DU NOMBRE DE TUYAU PARCOURUS
        flappy = charger_image('50x50jaune.png')
    elif FlappyHasard == 2:
        flappy = charger_image('50x50rouge.png')
    elif FlappyHasard == 3:
        flappy = charger_image('50x50bleu.png')
    elif FlappyHasard == 4:
        flappy = charger_image('50x50vert.png')
    elif FlappyHasard == 5:
        flappy = charger_image('50x50gris.png')

    musique = pygame.mixer.Sound('bip-flappy.wav')
    fond = charger_image2('500x500.png')
    tuyaubas = charger_image2('50x500bas.png')
    sol = charger_image2('1000x40.png')

    kamikaze1 = charger_image2('kamikaze1.png')
    kamikaze2 = charger_image2('kamikaze2.png')
    kamikaze3 = charger_image2('kamikaze3.png')
    kamikaze4 = charger_image2('kamikaze4.png')

    ## Definition des variables

    ecran = pygame.display.set_mode((500, 500))  # fenetre couples_tuyau[0].haut_haut_y'affichage

    # Coordonnees de depart de Flappy
    x = 30  #Coordonnees bout en haut couples_tuyau[0].x gauche Flappy x
    y = 0  #Coordonnees bout en haut couples_tuyau[0].x gauche Flappy  y
    xx = 80  #Bout en bas couples_tuyau[0].x droite de Flappy x
    yy = 50  #Bout en bas couples_tuyau[0].x droite de Flappy y

    #Coordonnees de depart du sol
    solX = 0
    solY = 460
    
    couples_tuyau = [CoupleTuyau() for i in range(5)]
    #1ere rangee de tuyaux au depart
    couples_tuyau[0].x = 700  #Coordonnees Tuyaubas en haut à gauche x
    couples_tuyau[0].etablir_haut_haut_y(None)

    #2eme rangee de tuyaux au depart  
    couples_tuyau[1].x = couples_tuyau[0].x + 130
    couples_tuyau[1].etablir_haut_haut_y(couples_tuyau[0])

    #3eme rangee de tuyaux au depart
    couples_tuyau[2].x = couples_tuyau[1].x + 130
    couples_tuyau[2].etablir_haut_haut_y(couples_tuyau[1])

    #4eme rangee de tuyaux au depart
    couples_tuyau[3].x = couples_tuyau[2].x + 130
    couples_tuyau[3].etablir_haut_haut_y(couples_tuyau[2])

    #5eme rangee de tuyaux au depart
    couples_tuyau[4].x = couples_tuyau[3].x + 130
    couples_tuyau[4].etablir_haut_haut_y(couples_tuyau[3])

    # Variable pour FLAPPYMORT
    IndiceFlappyMort = 0  #Indice pour afficher FlappyMort

    # Comptage tuyau    
    score = 0
    AfficheScore = str(score)
    RectangleScore = pygame.image.load('50x50Score.png')
    score_rect = RectangleScore.get_rect()
    pygame.draw.circle(RectangleScore, (0, 0, 0), score_rect.center, 10)
    font = pygame.font.Font(None, 50)  #police, taille de la police
    surface_font = font.render(AfficheScore, 1, (255, 255, 255))
    font_rect = surface_font.get_rect()
    font_rect.center = score_rect.center

    # Definition des variables de position des kamikazes
    kamikaze1X = 80
    kamikaze2X = -10
    kamikaze3X = -10
    kamikaze4X = 100
    kamikaze1Y = 400

    # Definition de la variable 'chrono' couples_tuyau[0].x la fonction chronometre
    chrono = pygame.time.Clock()  # On attribue la variable 'chrono' couples_tuyau[0].x la fonction chronometre

    ## Boucle d'animation
    while True:  # Tant que le programme fonctionne
        chrono.tick(40)  # 40 best

        ## Action de l'utilisateur (clavier)
        for event in pygame.event.get():
            if event.type == QUIT:  # Croix rouge
                pygame.display.quit()
                musique.stop()
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    y -= 30
                    yy -= 30
                elif event.key == K_p:
                    pygame.time.wait(2000)

            ## Gestion des mouvements
        # Mouvements du sol
        if solX <= -500:
            solX = 0
        solX -= 2

        # Mouvements verticaux de flappy
        y += 3  # Ce qui fait descendre flappy
        yy += 3

        # Mouvements horizontaux des tuyaux
        for ct in couples_tuyau:
            ct.x -= 2

        ## Remplacement des tuyaux
        for k in range(len(couples_tuyau)):
            if couples_tuyau[k].est_sorti():
                couples_tuyau[k].x = 600
                couples_tuyau[k].etablir_haut_haut_y(couples_tuyau[k-1])

         ##Gestion des collisions
        if any(ct.impact_oiseau(x, y, xx, yy) for ct in couples_tuyau) or (y >= 410):  #Remarque:Le sommet du sol est couples_tuyau[0].x y=460.
            #musique.stop()
            return score

        ##Gestion des blits au sein de la boucle

        ecran.blit(fond, (0, 0))  # fond + flappy
        ecran.blit(flappy, (x, y))

        for ct in couples_tuyau:
            ecran.blit(tuyaubas, (ct.x, ct.bas_haut_y())) 
            ecran.blit(tuyauhaut, (ct.x, ct.haut_haut_y))

        ecran.blit(sol, (solX, solY))

        ecran.blit(kamikaze1, (kamikaze1X, kamikaze1Y))  #kamikazes
        ecran.blit(kamikaze2, (kamikaze2X, 120))
        ecran.blit(kamikaze3, (kamikaze3X, 220))
        ecran.blit(kamikaze4, (kamikaze4X, 10))

        ## Mouvement des Kamikazes 
        if score <= 1:
            # 5 minimum
            kamikaze1X += 5  # marron
            kamikaze1Y -= 1  # marron
            kamikaze2X += 7  # petit cyan
            kamikaze3X += 8  # bleu fonce
            kamikaze4X += 10  # violet
            ## Comptage tuyaux
        son = pygame.mixer.Sound('bip-flappy.wav')

        for ct in couples_tuyau:
            if ct.x == x:
                score += 1
                son.play()
                #musique.stop()

            ## Affichage du score
        AfficheScore = str(score)
        surface_font = font.render(AfficheScore, 1, (255, 255, 255))
        ecran.blit(surface_font, (10, 465))

        ##Mise à jour de l'affichage
        pygame.display.flip()

def ecrire_score(score):
    # si oui, remplace dansle fichier
    f = open('score.txt', 'a')
    f.write(str(score) + os.linesep)
    f.close()

class CoupleTuyau(object):

    largeur_tuyau = 50
    espacement = 150
    hauteur_tuyau = 500

    def __init__(self):
        self.x = 0
        self.haut_haut_y = 0

    def etablir_haut_haut_y(self, tuyau_precedent):
        if not tuyau_precedent:
            self.haut_haut_y = randint(-400, -240)
            return
        self.haut_haut_y = randint((tuyau_precedent.haut_haut_y - 90), (tuyau_precedent.haut_haut_y + 90))
        if (self.haut_haut_y < -450):
            self.haut_haut_y = tuyau_precedent.haut_haut_y + 90
        elif (self.haut_haut_y > -240):
            self.haut_haut_y = tuyau_precedent.haut_haut_y - 90

    def est_sorti(self):
        return self.x + CoupleTuyau.largeur_tuyau < 0

    def touche_plat_tuyau(self, x_oiseau):
        return self.x <= x_oiseau <= self.x + CoupleTuyau.largeur_tuyau

    def impact_oiseau(self, x, y, xx, yy):
        return ((self.touche_plat_tuyau(xx) and yy >= self.bas_haut_y()) 
                                        or (self.touche_plat_tuyau(x) and yy >= self.bas_haut_y()) 
                                        or (self.touche_plat_tuyau(xx) and y <= self.haut_bas_y()) 
                                        or (self.touche_plat_tuyau(x) and y <= self.haut_bas_y()))

    def bas_haut_y(self):
        return self.haut_bas_y() + CoupleTuyau.espacement

    def haut_bas_y(self):
        return self.haut_haut_y + CoupleTuyau.hauteur_tuyau

    def bas_bas_y(self):
        return self.bas_haut_y() + CoupleTuyau.hauteur_tuyau

menuprincipal()