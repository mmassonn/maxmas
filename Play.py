import pygame ##Importe le module pygame
from pygame.locals import* #le programme va chercher la localistion de pygame
import sys ##Importe le module sys

## definit la fonction principale
def main():

    ##Initialisation de pygame
    pygame.init()
    #creation d'une fenetre de largeur l de 600 pixels et de hauteur h de 600 pixels
    l=600
    h=600
    fenetre=pygame.display.set_mode((l, h))
    
    ##def variable programme
    program=True

    ##Création d'un  carré
    carre_b=pygame.Surface((l/10,h/10))
    carre_b.fill ((45,62,200))
    carre_o=pygame.Surface((l/10,h/10))
    carre_o.fill ((241,125,12))
    
    ##Boucle de python (tant que le programme est vrai faire marcher le programme)
    while program==True :

        #pour l'evenemnt dans l'evenement donné de pygame
        for event in pygame.event.get():
            
            #Si le type de l'evenement est quit ou pressage de la touche escape alors le programme est faux et donc le programme se ferme
            if event.type == QUIT or (event.type == KEYDOWN and event.key==K_ESCAPE):
                program = False
                
                

        ##Pour la variable i dans la gamme de 0 à 10 si i est PAIR pour la variable j dans la gamme de 0 à 10 si j est PAIR mettre un carré bleu
        ##Sinon pour la variable i dans la gamme de 0 à 10 si i est PAIR pour la variable j dans la gamme de 0 à 10 si j est IMPAIR mettre un carré orange
        ##Sinon pour la variable i dans la gamme de 0 à 10 si i est IMPAIR pour la variable j dans la gamme de 0 à 10 si j est PAIR mettre un carré bleu
        ##Sinon pour la variable i dans la gamme de 0 à 10 si i est IMPAIR pour la variable j dans la gamme de 0 à 10 si j est IMPAIR mettre un carré orange 
        for i in range(10):
            if i%2==0:
                for j in range(10):
                    if j%2==0:
                        fenetre.blit(carre_b, (60*i,60*j))
                    else :
                        fenetre.blit(carre_o, (60*i,60*j))
            else:
                for j in range(10):
                    if j%2==0:
                        fenetre.blit(carre_o, (60*i,60*j))
                    else :
                        fenetre.blit(carre_b, (60*i,60*j))
                        
        ##Si le type de l'evenement est d'enfoncer une touche faire l'inverse
                        
        
        for event in pygame.event.get():

            if event.type == KEYDOWN %2==0 :
                    for i in range(10):
                        if i%2==0:
                            for j in range(10):
                                if j%2==0:
                                    fenetre.blit(carre_o, (60*i,60*j))
                                else :
                                    fenetre.blit(carre_b, (60*i,60*j))
                        else:
                            for j in range(10):
                                if j%2==0:
                                    fenetre.blit(carre_b, (60*i,60*j))
                                else :
                                    fenetre.blit(carre_o, (60*i,60*j))

                                    
            
            
                            
      

##1)press touche change la positin des carrés (deux façons differente a)press change et reviens lors keydown b) press change et press rechange)
##  2) regarder les cercles (alliasing circle)#   3) 10*10 4) dame une case sur deux afficher
                    
            
        
    

        
        pygame.display.flip()
    pygame.quit()
    sys.exit()
    

if __name__ == '__main__':
    main()
