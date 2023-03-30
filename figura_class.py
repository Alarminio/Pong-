import pygame as pg

"""
class Marcador:
    def __init__(self,pos_x,pos_y,color=(0,0,0),w=10,h=10): 
        self.pos_x=pos_x
        self.pos_y=pos_y
        self.color=color
        self.w=w
        self.h=h

    def dibujar(self,pantalla):
        pg.draw.rect(pantalla,self.color,self.pos_x,self.pos_y,self.w,self.h)

"""

class Raqueta:
     def __init__(self,pos_x,pos_y,color=(255,255,255),w=20,h=120,vx=1,vy=1):
        self.pos_x= pos_x
        self.pos_y= pos_y
        self.color= color
        self.w= w
        self.h=h
        self.vx=vx
        self.vy=vy

     def dibujar(self,pantalla):
        pg.draw.rect(pantalla, self.color,(self.pos_x-(self.w//2),self.pos_y-(self.h//2),self.w,self.h))

     def mover(self,tecla_arriba,tecla_abajo,y_max=600,y_min=0):
         estado_teclado = pg.key.get_pressed()

         if estado_teclado[tecla_arriba] == True and self.pos_y > y_min+(self.h//2):
             self.pos_y -=1

         if estado_teclado[tecla_abajo] == True and self.pos_y < y_max-(self.h//2):
             self.pos_y +=1



class Pelota:
    def __init__(self,pos_x,pos_y,color=(255,255,255),radio=20,vx=5,vy=5):
         self.pos_x=pos_x
         self.pos_y=pos_y
         self.color=color
         self.radio=radio
         self.vx=vx
         self.vy=vy
         self.contadorDerecho=0
         self.contadorIzquierdo=0


    def dibujar(self,pantalla):
         pg.draw.circle(pantalla,self.color,(self.pos_x-self.radio,self.pos_y-self.radio),self.radio)

    def mover(self,x_max=800,y_max=600):
        self.pos_x += self.vx
        self.pos_y += self.vy

        if self.pos_y >= y_max-self.radio or self.pos_y < 0+self.radio:
            self.vy *= -1

        if self.pos_x >= x_max+self.radio*5:
            self.vx *= -1
            self.contadorIzquierdo +=1

        if self.pos_x < 0-self.radio*5:
            self.vx *= -1
            self.contadorDerecho +=1

    def mostrar_marcador(self,pantalla):
        fuente = pg.font.Font(None, 35)
        jugador1 = fuente.render(str(self.contadorDerecho),0,(255,255,255))
        jugador2 = fuente.render(str(self.contadorIzquierdo),0,(255,255,255))
        pantalla.blit(jugador1,(200,50))
        pantalla.blit(jugador2,(600,50))



    