import pygame
import sys

class Game():
    
    runners= []
    __startLine= 20
    __finishLine= 620
    
    def __init__(self):
        self.__screen= pygame.display.set_mode((640, 480))  #creacion de la pantalla  
        pygame.display.set_caption("Carrera de bichos")     # titulo de la pantalla
        self.__screen.fill((200,250,0))  #imagen de fondo
        #self.background= pygame.image.load("ruta a la imagen")->para cargar una imagen de fondo

    def competir(self):
        
        gameOver= False
        while not gameOver:
            #comprobacion de eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver= True
                    
            #renderizado de pantalla
            #self.__screen.blit(self.__background,(0,0))  #coloca el fondo en la posicion (0,0)
            pygame.display.flip()  #refresca la pantalla
                
        pygame.quit()
        sys.exit()
        
if __name__=="__main__":
    game= Game()
    pygame.init()
    game.competir()
    
    