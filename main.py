import pygame as pg
from figura_class import Pelota, Raqueta



pg.init()

pantalla_principal = pg.display.set_mode((800,600))
pg.display.set_caption("pong")
tasa_refresco = pg.time.Clock()



pelota = Pelota(400,300)
raqueta1 = Raqueta(10,300)
raqueta2 = Raqueta(790,300)



game_over = False

while not game_over:

    valor_tasa = tasa_refresco.tick(260)

    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            game_over = True

    raqueta1.mover(pg.K_w,pg.K_s)
    raqueta2.mover(pg.K_UP,pg.K_DOWN)
    pelota.mover()
    print("punto Derecho:",pelota.contadorDerecho)
    print("punto Izquierdo:",pelota.contadorIzquierdo)


    pantalla_principal.fill((0,128,94))
    pg.draw.line(pantalla_principal,(255,255,255),(400,0),(400,600),10)
    
    """
    pg.draw.rect(pantalla_principal,(0,0,0),(133,20),10)
    """


    pelota.dibujar(pantalla_principal)
    raqueta1.dibujar(pantalla_principal)
    raqueta2.dibujar(pantalla_principal)
   

    pg.display.flip()

pg.quit()