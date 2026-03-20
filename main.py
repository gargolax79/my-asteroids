import pygame
from constants import *
from logger import log_state
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # creamos grupos para los players
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    # creamos un grupo para los asteroides
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)

    # creamos un grupo para el campo de asteroides
    AsteroidField.containers = (updatable)
    

    # instanciamos un objeto player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    while True:
        log_state()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")
        
        updatable.update(dt)
        #player.update(dt)
        
        # re renderizamos al jugador en cada frame de la pantalla
        player.draw(screen)
        for s in drawable:
            s.draw(screen)
        

        pygame.display.flip()
        clock.tick(60)  # Limit to 60 FPS
        dt = clock.tick(60) / 1000
        #print(f"Delta time: {dt:.4f} seconds")

    # print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Screen height: {SCREEN_HEIGHT}")




if __name__ == "__main__":
    main()
