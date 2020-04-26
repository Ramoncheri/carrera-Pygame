#primera version. Siempre sale Hong Kong Fui y salen varios nombres

import pygame
import sys
import random


class Runner():
    
    __customs =('HK1', 'PR', 'Penelope', 'rocomovil')
    
    def __init__(self, x=0, y=0, custom='HK1'):
        self.custom= pygame.image.load("Images/{}.gif".format(custom))
        self.position=[x,y]
        self.name= ''
        
    def avanzar(self):
        self.position[0] += random.randint(1,3)
        

class Game():
    
    runners= []
    __posicY=(100, 175, 250, 320)
    __names =('Hong kong Fui', 'Pierre', 'Penelope', 'rocomovil')
    __startLine= 0
    __finishLine= 620
    
    def __init__(self):
        self.__screen= pygame.display.set_mode((640, 480))  #creacion de la pantalla  
        pygame.display.set_caption("Carrera de bichos")     # titulo de la pantalla
        self.__screen.fill((200,250,0))  #imagen de fondo
        #self.background= pygame.image.load("ruta a la imagen")->para cargar una imagen de fondo
       
        for i in range (4):
            pilot= Runner(self.__startLine, self.__posicY[i])
            pilot.name= self.__names[i]
            self.runners.append(pilot)
        
        
    def competir(self):
        
        gameOver= False
        
        while not gameOver:
            #comprobacion de eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver= True
                    
            for pilot in self.runners:
                pilot.avanzar()
            
                if pilot.position[0] >= self.__finishLine:
                    print("{} es el ganador".format(pilot.name))
                    gameOver= True
            
            #renderizado de pantalla
            
            #self.__screen.blit(self.__background,(0,0))  #coloca el fondo en la posicion (0,0)
            
            for pilot in self.runners:
                self.__screen.blit(pilot.custom, pilot.position)
                
                
            pygame.display.flip()  #refresca la pantalla
                
        pygame.quit()
        sys.exit()
        
if __name__=="__main__":
    game= Game()
    pygame.init()
    game.competir()
    
    