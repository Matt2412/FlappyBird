## Import et initialisation des modules
from random import randint
import pygame
import sys 
import pygame.sprite as sprite
from pygame.locals import*
pygame.init()

## Definition de la fonction jeu()

def jeu():
    
## Chargement des images

    FlappyHasard = randint(1,5) # A CHANGER CAD ON MET CA COMME DES RECOMPENSES A DEBLOQUER EN FONCTION
    if FlappyHasard == 1 :      # DU NOMBRE DE TUYAU PARCOURUS
        flappy = pygame.image.load('50x50jaune.png')
    elif FlappyHasard == 2 :
        flappy = pygame.image.load('50x50rouge.png')
    elif FlappyHasard == 3 :
        flappy = pygame.image.load('50x50bleu.png')
    elif FlappyHasard == 4 :   
        flappy = pygame.image.load('50x50vert.png')    
    elif FlappyHasard == 5 :
        flappy = pygame.image.load('50x50gris.png')
    
    fond = pygame.image.load('500x500.png')
    tuyaubas = pygame.image.load('50x500bas.png')
    tuyauhaut = pygame.image.load('50x500haut.png')
    tuyaubas2 = pygame.image.load('50x500bas.png')
    tuyauhaut2 = pygame.image.load('50x500haut.png')
    tuyaubas3  = pygame.image.load('50x500bas.png')
    tuyauhaut3 = pygame.image.load('50x500haut.png')
    tuyaubas4 = pygame.image.load('50x500bas.png') 
    tuyauhaut4 = pygame.image.load('50x500haut.png')
    tuyaubas5 = pygame.image.load('50x500bas.png')
    tuyauhaut5 = pygame.image.load('50x500haut.png')
    sol = pygame.image.load('1000x40.png')
    FlappyMort = pygame.image.load('50x50FlappyMort.png')
    
    kamikaze1 = pygame.image.load('kamikaze1.png')
    kamikaze2 = pygame.image.load('kamikaze2.png')
    kamikaze3 = pygame.image.load('kamikaze3.png')
    kamikaze4 = pygame.image.load('kamikaze4.png')

## Definition des variables

    ecran = pygame.display.set_mode((500,500)) # fenetre d'affichage
    
    #Coordonnees de depart de Flappy
    x = 30  #Coordonnees bout en haut a gauche Flappy x
    y = 0   #Coordonnees bout en haut a gauche Flappy  y
    xx = 80 #Bout en bas a droite de Flappy x    
    yy = 50 #Bout en bas a droite de Flappy y
    
    #Coordonnees de depart du sol
    solX = 0
    solY = 460
    
    #1ere rangee de tuyaux au depart
    a = 700 #Coordonnees Tuyaubas en haut à gauche x  
    aa = 750  #Bout en bas a droite de tuyaubas  x 
    d = randint(-400,-240)
    print('d est egal a',d)
    dd = d+500
    b=dd+150
    bb=b+500      
    
    #2eme rangee de tuyaux au depart    
    a2 = a + 130
    aa2 = aa + 130
    d2 = randint((d-90),(d+90))
    if (d2<-450):
        d2 = d+90
    elif (d2>-240):
        d2 = d-90  
    print('d2 est egal a',d2)
    dd2 = d2 + 500
    b2 = dd2 + 150
    bb2 = b2 + 500
    
    #3eme rangee de tuyaux au depart
    a3 = a2 + 130
    aa3 = aa2 + 130
    d3 = randint((d2-90),(d2+90))
    if (d3<-450):
        d3 = d2+90
    elif (d3>-240):
        d3 = d2-90  
    print('d3 est egal a',d3)
    dd3 = d3 + 500
    b3 = dd3 + 150
    bb3 = b3 + 500
    
    #4eme rangee de tuyaux au depart    
    a4 = a3 + 130
    aa4 = aa3 + 130
    d4 = randint((d3-90),(d3+90))
    if (d4<-450):
        d4 = d3+90
    elif (d4>-240):
        d4 = d3-90  
    print('d4 est egal a', d4)
    dd4 = d4 + 500
    b4 = dd4 + 150
    bb4 = b4 + 500
    
    #5eme rangee de tuyaux au depart    
    a5 = a4 + 130
    aa5 = aa4 + 130
    d5 = randint((d4-90),(d4+90))
    if (d5<-450):
        d5 = d4+90
    elif (d5>-240):
        d5 = d4-90  
    print('d5 est egal a',d5)
    dd5 = d5 + 500
    b5 = dd5 + 150
    bb5 = b5 + 500  
    
    # Variable pour FLAPPYMORT
    IndiceFlappyMort = 0 #Indice pour afficher FlappyMort
    
    # Comptage tuyau    
    score = 0 
    AfficheScore = str(score)
    RectangleScore = pygame.image.load('50x50Score.png')
    score_rect = RectangleScore.get_rect()
    pygame.draw.circle(RectangleScore, (0,0,0), score_rect.center ,10)
    font = pygame.font.Font(None,50) #police, taille de la police
    surface_font = font.render(AfficheScore, 1 , (255,255,255))
    font_rect = surface_font.get_rect()
    font_rect.center = score_rect.center
    
    
    # Definition des variables de position des kamikazes
    kamikaze1X = 80
    kamikaze2X = -10
    kamikaze3X = -10
    kamikaze4X = 100
    kamikaze1Y = 400
    
    # Definition de la variable 'chrono' a la fonction chronometre
    chrono = pygame.time.Clock() # On attribue la variable 'chrono' a la fonction chronometre
    
    ## Boucle d'animation
    BoucleFonctionnement = 1   # Variable permettant le fonctionnement de la boucle
    while BoucleFonctionnement == 1  :  # Tant que le programme fonctionne
        chrono.tick(40) # 40 best
        
        ## Action de l'utilisateur (clavier)
        for event in pygame.event.get():
            if event.type == QUIT : # Croix rouge   
                pygame.display.quit()
            elif event.type == KEYDOWN : 
                if event.key == K_SPACE :
                    y -= 30     
                    yy -= 30 
                    ecran.blit(flappy, (x,y))
                    pygame.display.flip()
                elif event.key == K_p : 
                    pygame.time.wait(2000)
                    
    ##Gestion des collisions 
        """"""
        if (a <= xx <= aa and yy >= b) or (a <= x <= aa and yy >= b) or (a<= xx <= aa and y <= dd) or (a<= x <= aa and y <= dd) :
            pygame.display.quit() 
        if (a2 <= xx <= aa2 and yy >= b2) or (a2 <= x <= aa2 and yy >= b2) or (a2<= xx <= aa2 and y <= dd2) or (a2<= x <= aa2 and y <= dd2) :
            pygame.display.quit()    
        if (a3 <= xx <= aa3 and yy >= b3) or (a3 <= x <= aa3 and yy >= b3) or (a3<= xx <= aa3 and y <= dd3) or (a3<= x <= aa3 and y <= dd3) :
            pygame.display.quit()  
        if (a4 <= xx <= aa4 and yy >= b4) or (a4 <= x <= aa4 and yy >= b4) or (a4<= xx <= aa4 and y <= dd4) or (a4<= x <= aa4 and y <= dd4) :
            pygame.display.quit()        
        if (a5 <= xx <= aa5 and yy >= b5) or (a5 <= x <= aa5 and yy >= b5) or (a5<= xx <= aa5 and y <= dd5) or (a5<= x <= aa5 and y <= dd5) :
            pygame.display.quit()  
            
        if (y >= 410):
            pygame.display.quit()    #Remarque:Le sommet du sol est a y=460.
        """  """  
                
    ## Gestion des mouvements
        # Mouvements du sol
        if solX <= -500:
            solX = 0   
        solX -=2         
        
        # Mouvements verticaux de flappy
        y += 3 # Ce qui fait descendre flappy
        yy += 3
        
        # Mouvements horizontaux des tuyaux
        a -= 2 
        aa -= 2 
        a2 -= 2
        aa2 -= 2
        a3 -= 2
        aa3 -= 2
        a4 -= 2
        aa4 -= 2
        a5 -= 2
        aa5 -= 2
    
    ## Remplacement des tuyaux.  
                                
        if aa < 0 :    
            aa = 650   
            a = 600
            d = randint(d5-90,d5+90)
            if (d<-450):
                d = d5+90   
            elif (d>-240): 
                d = d5-90  
            print('d est egal a',d)
            dd = d+500
            b=dd+150
            bb=b+500
        if aa2 < 0 :
            aa2 = 650
            a2 = 600
            d2 = randint((d-90),(d+90))
            if (d2<-450):
                d2 = d+90
            elif (d2>-240):
                d2 = d-90  
            print('d2 est egal a',d2)
            dd2 = d2 + 500
            b2 = dd2 + 150
            bb2 = b2 + 500
        if aa3 < 0 :
            aa3 = 650
            a3 = 600
            d3 = randint((d2-90),(d2+90))
            if (d3<-450):
                d3 = d2+90
            elif (d3>-240):
                d3 = d2-90  
            print('d3 est egal a',d3)
            dd3 = d3 + 500
            b3 = dd3 + 150
            bb3 = b3 + 500
        if aa4 < 0 :
            aa4 = 650
            a4 = 600
            d4 = randint((d3-90),(d3+90))
            if (d4<-450):
                d4 = d3+90
            elif (d4>-240):
                d4 = d3-90  
            print('d4 est egal a', d4)
            dd4 = d4 + 500
            b4 = dd4 + 150
            bb4 = b4 + 500
        if aa5 < 0 :
            aa5 = 650
            a5 = 600
            d5 = randint((d4-90),(d4+90))  
            if (d5<-450):      
                d5 = d4+90   
            elif (d5>-240): 
                d5 = d4-90  
            print('d5 est egal a',d5)
            dd5 = d5 + 500 
            b5 = dd5 + 150
            bb5 = b5 + 500  
    
    ##Gestion des blits au sein de la boucle    
        
        ecran.blit(fond, (0,0)) # fond + flappy
        ecran.blit(flappy, (x,y))  
        
        ecran.blit(tuyaubas, (a,b)) #collisions
        ecran.blit(tuyauhaut, (a,d))
        ecran.blit(tuyaubas2, (a2,b2)) 
        ecran.blit(tuyauhaut2, (a2,d2))
        ecran.blit(tuyaubas3, (a3,b3))
        ecran.blit(tuyauhaut3, (a3,d3))
        ecran.blit(tuyaubas4, (a4,b4))
        ecran.blit(tuyauhaut4, (a4,d4))
        ecran.blit(tuyaubas5, (a5,b5))      
        ecran.blit(tuyauhaut5, (a5,d5)) 
        ecran.blit(sol, (solX,solY))  
        
        ecran.blit(kamikaze1, (kamikaze1X, kamikaze1Y) ) #kamikazes
        ecran.blit(kamikaze2, (kamikaze2X, 120))
        ecran.blit(kamikaze3, (kamikaze3X, 220))
        ecran.blit(kamikaze4, (kamikaze4X, 10))
        
    ## Mouvement des Kamikazes
        if score <= 1 :
            # 5 minimum
            kamikaze1X += 5   # marron
            kamikaze1Y -= 1   # marron 
            kamikaze2X += 7   # petit cyan
            kamikaze3X += 8   # bleu fonce
            kamikaze4X += 10  # violet
        
                
    ## FLAPPYMORT
    
        if IndiceFlappyMort == 0: # while 1st T != 0
            ecran.blit(FlappyMort, (aa-50 ,dd-90))
            if aa <= 0 :           # after forever 
                IndiceFlappyMort += 1 
        if IndiceFlappyMort == 1 :
            ecran.blit(FlappyMort, (501, 501)) # hors de l'ecran
        
        
    ## Comptage tuyaux 
        
        if a == x:               
            score += 1     
        elif a2 == x :                              
            score += 1  
        elif a3 == x :
            score += 1    
        elif a4 == x :    
            score += 1
        elif a5 == x :            
            score += 1
    
    ## Affichage du score
        AfficheScore = str(score)
        surface_font = font.render(AfficheScore, 1 , (255,255,255))           
        ecran.blit(surface_font, (10,465))       
            
        pygame.display.flip()    
        

