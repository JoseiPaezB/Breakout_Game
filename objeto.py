import pygame
import random
import time

screen_width = 780
screen_height = 600
brick_width = 60
brick_height = 20
brick_spacing = 5
fps = 30

COLORS = [(0, 255, 255), (255, 255, 0), (255, 0, 0)]

difficulty_hashmap = {
    "Beginner": 1,
    "Intermediate": 2,
    "Professional": 3
}


def set_power_up():
    choice = random.randint(1, 30)
    if choice == 1:
        return "Faster Paddle"
    elif choice == 5:
        return "Stronger Ball"
    elif choice == 15:
        return "Slower Ball"
    else:
        return ""
    
class PowerUp(pygame.sprite.Sprite):
    def __init__(self, _brick):
        super().__init__()

        self.image = pygame.Surface((5, 5))
        self.image.fill((0, 255, 0))  # Color del power up (verde en este ejemplo)
        self.rect = self.image.get_rect(center=_brick.rect.center)
        self.powerMsg = set_power_up()

        self.speed = 2  # Ajustar la velocidad del power up
        self.brick = _brick  # Ladrillo al que está asociado el power up

    def move_down(self):
        # Manda al power up hacia abajo
        self.rect.y += self.speed

        # verifica si el power up ha llegado hasta el fondo de la pantalla
        if self.rect.y > 600:
            self.kill()  # quita el powerup del juego 


class Ball(pygame.sprite.Sprite):
    def __init__(self, x_lower_limit, x_upper_limit):
        super().__init__()
        self.x_lower_limit = x_lower_limit
        self.x_upper_limit = x_upper_limit
        self.alive = True
        self.strength = 1

        self.image = pygame.Surface((20, 20))
        self.image.fill((255, 255, 255))  # color de la bola (blanco en este ejemplo)
        self.rect = self.image.get_rect(center=((x_upper_limit // 2) + (x_lower_limit/2), screen_height // 2))
        self.speed = [5, 5]  # Da la velocidad inicial de la bola

    def update(self):
        # Esto es lo que causa el mover de la pelota
        self.rect.x += self.speed[0]
        self.rect.y += self.speed[1]

        # Esto es lo que causa que la pelota rebote en los bordes de la pantalla
        if self.rect.left <= self.x_lower_limit or self.rect.right >= self.x_upper_limit:
            self.speed[0] = -self.speed[0]
        if self.rect.top <= 0:
            self.speed[1] = -self.speed[1]
        if self.rect.bottom >= screen_height:
            self.alive = False
            self.kill()
    
    def get_x_pos(self):
        return self.rect.x


class Paddle(pygame.sprite.Sprite):
    def __init__(self, x_lower_limit, x_upper_limit):
        super().__init__()
        self.x_lower_limit = x_lower_limit
        self.x_upper_limit = x_upper_limit
        self.speed = 10

        self.image = pygame.Surface((100, 20))
        self.image.fill((0, 0, 255))  # el color del paddle (azul en este ejemplo)
        self.rect = self.image.get_rect(center=((x_upper_limit // 2) + (x_lower_limit/2), screen_height - 30))

    def update(self):
        # esto es lo que hace el movimiento del padel segun las flechas izquierda y derecha
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > self.x_lower_limit:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < self.x_upper_limit-5:
            self.rect.x += self.speed

class PaddleBot(pygame.sprite.Sprite):
    def __init__(self, x_lower_limit, x_upper_limit):
        super().__init__()
        self.x_lower_limit = x_lower_limit
        self.x_upper_limit = x_upper_limit

        self.image = pygame.Surface((100, 20))
        self.image.fill((0, 0, 255))  # color del paddle (azul en este ejemplo)
        self.rect = self.image.get_rect(center=((x_upper_limit // 2) + (x_lower_limit/2), screen_height - 30))

    def move(self, ball_x):
        if ball_x <= self.rect.x and ball_x >= screen_width/2:
            self.rect.x -= 10
        if ball_x >= self.rect.x and ball_x <= screen_width-90:
            self.rect.x += 10
            
            

class CenterLine(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.Surface((3, y * 2))
        self.image.fill((255, 255, 255))

        self.rect = self.image.get_rect(center=(x - 3, 0))

        self.alive = True
        self.power_up = False
        self.hits = 0


class Brick(pygame.sprite.Sprite):
    def __init__(self, x, y, randLimit):
        super().__init__()

        self.tipoBrick = random.randint(1, randLimit)
        self.image = pygame.Surface((brick_width, brick_height))
        self.image.fill(COLORS[self.tipoBrick - 1])

        self.rect = self.image.get_rect(topleft=(x, y))

        self.alive = True
        self.power_up = False
        self.hits = 0

    def is_alive(self):
        return self.hits < self.tipoBrick

    def contact_ball(self, ballStrength):
        self.hits += ballStrength
        if self.is_alive():
            self.image.fill(COLORS[self.tipoBrick - 1 - self.hits])
        else:
            self.kill()


class Wall:
    def __init__(self, x_lower_limit, x_upper_limit, difficulty):
        self.difficulty = difficulty_hashmap[difficulty]
        self.bricks = pygame.sprite.Group()
        self.power_ups = pygame.sprite.Group()
        self.x_start_pos = x_lower_limit
        self.columns = int((x_upper_limit - x_lower_limit) // (brick_width + brick_spacing))
        self.rows = int((screen_height // 2) // (brick_height + brick_spacing))

    def add_bricks(self):

        x_pos = self.x_start_pos
        y_pos = 0

        for i in range(0, self.rows):
            for j in range(0, self.columns):
                new_brick = Brick(x_pos, y_pos, self.difficulty)
                self.bricks.add(new_brick)

                new_power_up = PowerUp(new_brick)
                self.power_ups.add(new_power_up)

                x_pos += brick_width + brick_spacing

            x_pos = self.x_start_pos
            y_pos += brick_height + brick_spacing


def contar_tiempo():
    global minuto_pasado,salir
    tiempo_inicial = time.time()
    while not minuto_pasado:
        time.sleep(1)
        tiempo_transcurrido = time.time() - tiempo_inicial
        if tiempo_transcurrido > 20:
            print("¡Han pasado más de 1 minuto!")
            minuto_pasado = True
            salir=True
            
            
