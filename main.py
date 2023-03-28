import pygame as pg
from figura_class import Pelota, Raqueta



pg.init()

pantalla_principal = pg.display.set_mode((800,600))
pg.display.set_caption("pong")
tasa_refresco = pg.time.Clock()



pelota = Pelota(400,300)
raqueta1 = Raqueta(10,300-(120//2))
raqueta2 = Raqueta(790 - 20,300-(120//2))

game_over = False

while not game_over:

    valor_tasa = tasa_refresco.tick(60)

    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            game_over = True



    pantalla_principal.fill((0,128,94))
    pg.draw.line(pantalla_principal,(255,255,255),(400,0),(400,600),10)

    pelota.dibujar(pantalla_principal)
    raqueta1.dibujar(pantalla_principal)
    raqueta2.dibujar(pantalla_principal)


    pg.display.flip()

pg.quit()