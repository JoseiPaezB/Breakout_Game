import pygame
import sys
import threading
import time

from objetos import *
minuto_pasado = False
salir=False
global contador

class Screen:
    def __init__(self, width, height, difficulty, start):
        pygame.init()
        self.width = width
        self.height = height
        self.difficulty = difficulty
        self.start = start
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.current_scene = MainMenu(self)

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.current_scene.handle_events()
            self.current_scene.update()
            self.current_scene.draw()

            pygame.display.flip()
    
class MainMenu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 36)
        self.button0_rect = pygame.Rect(275, 100, 200, 50)
        self.button1_rect = pygame.Rect(300, 300, 200, 50)
        self.button2_rect = pygame.Rect(300, 400, 200, 50)
        self.button3_rect = pygame.Rect(300, 500, 200, 50)

    #Se añade conectividad a los botones con otras interfaces
    def handle_events(self):
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if self.button1_rect.collidepoint(mouse_x, mouse_y):
                self.screen.current_scene = IndividualMode(self.screen)
            elif self.button2_rect.collidepoint(mouse_x, mouse_y):
                self.screen.current_scene = oneVone(self.screen)
            elif self.button3_rect.collidepoint(mouse_x, mouse_y):
                self.screen.current_scene = contrareloj(self.screen)
            elif self.button0_rect.collidepoint(mouse_x, mouse_y):
                pass

    def update(self):
        pass

    def draw(self):
        self.screen.screen.fill((0, 0, 0))
        pygame.draw.rect(self.screen.screen, (0, 0, 0), self.button0_rect)
        text0 = self.font.render("BREAKOUT GAME", True, (255, 255, 255))
        self.screen.screen.blit(text0, (self.button0_rect.x + 10, self.button0_rect.y + 10))
        pygame.draw.rect(self.screen.screen, (255, 0, 0), self.button1_rect)
        text1 = self.font.render("  Individual", True, (255, 255, 255))
        self.screen.screen.blit(text1, (self.button1_rect.x + 10, self.button1_rect.y + 10))
        pygame.draw.rect(self.screen.screen, (0, 255, 0), self.button2_rect)
        text2 = self.font.render("  1 v 1", True, (255, 255, 255))
        self.screen.screen.blit(text2, (self.button2_rect.x + 10, self.button2_rect.y + 10))
        pygame.draw.rect(self.screen.screen, (0, 0, 255), self.button3_rect)
        text3 = self.font.render("  Contrareloj", True, (255, 255, 255))
        self.screen.screen.blit(text3, (self.button3_rect.x + 10, self.button3_rect.y + 10))


class IndividualMode:
    
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 36)
        self.button1_rect = pygame.Rect(300, 200, 200, 50)
        self.button2_rect = pygame.Rect(300, 300, 200, 50)
        self.button3_rect = pygame.Rect(300, 400, 200, 50)
        self.button4_rect = pygame.Rect(300, 500, 200, 50)
        self.screen.screen.fill((0, 0, 0))
        
    #Se añade conectividad a los botones con otras interfaces
    def handle_events(self):
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if self.button1_rect.collidepoint(mouse_x, mouse_y):
               self.begginer_button()  
            elif self.button2_rect.collidepoint(mouse_x, mouse_y):
               self.intermidiate_button() 
            elif self.button3_rect.collidepoint(mouse_x, mouse_y): 
                self.professional_button() 
            elif self.button4_rect.collidepoint(mouse_x, mouse_y): 
                self.screen.current_scene = MainMenu(self.screen)

    def update(self):
        pass
      
    #Se crean los botones de dificultad
    def draw(self):
        pygame.draw.rect(self.screen.screen, (255, 0, 0), self.button1_rect)
        text1 = self.font.render("Beginner", True, (255, 255, 255))
        self.screen.screen.blit(text1, (self.button1_rect.x + 10, self.button1_rect.y + 10))
        pygame.draw.rect(self.screen.screen, (0, 255, 0), self.button2_rect)
        text2 = self.font.render("Intermediate", True, (255, 255, 255))
        self.screen.screen.blit(text2, (self.button2_rect.x + 10, self.button2_rect.y + 10))
        pygame.draw.rect(self.screen.screen, (0, 0, 255), self.button3_rect)
        text3 = self.font.render("Professional", True, (255, 255, 255))
        self.screen.screen.blit(text3, (self.button3_rect.x + 10, self.button3_rect.y + 10))  
        pygame.draw.rect(self.screen.screen, (255, 0, 255), self.button4_rect)
        text4 = self.font.render("Back", True, (255,255,255))
        self.screen.screen.blit(text4, (self.button4_rect.x + 10, self.button4_rect.y + 10))
        
    def begginer_button(self): 
        game_loop("individual","Beginner")
    def intermidiate_button(self):
        game_loop("individual","Intermediate")
    def professional_button(self):
        game_loop("individual","Professional")
    
    
class oneVone:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 36)
        self.button1_rect = pygame.Rect(300, 200, 200, 50)
        self.button2_rect = pygame.Rect(300, 300, 200, 50)
        self.button3_rect = pygame.Rect(300, 400, 200, 50)
        self.button4_rect = pygame.Rect(300, 500, 200, 50)
        self.screen.screen.fill((0, 0, 0))

    #Se añade conectividad a los botones con otras interfaces
    def handle_events(self):
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if self.button1_rect.collidepoint(mouse_x, mouse_y):
               self.begginer_button()
            elif self.button2_rect.collidepoint(mouse_x, mouse_y):
               self.intermidiate_button()
            elif self.button3_rect.collidepoint(mouse_x, mouse_y): 
                self.professional_button()
            elif self.button4_rect.collidepoint(mouse_x, mouse_y): 
                self.screen.current_scene = MainMenu(self.screen)

    def update(self):
        pass
            
    def draw(self):
        pygame.draw.rect(self.screen.screen, (255, 0, 0), self.button1_rect)
        text1 = self.font.render("Beginner", True, (255, 255, 255))
        self.screen.screen.blit(text1, (self.button1_rect.x + 10, self.button1_rect.y + 10))
        pygame.draw.rect(self.screen.screen, (0, 255, 0), self.button2_rect)
        text2 = self.font.render("Intermediate", True, (255, 255, 255))
        self.screen.screen.blit(text2, (self.button2_rect.x + 10, self.button2_rect.y + 10))
        pygame.draw.rect(self.screen.screen, (0, 0, 255), self.button3_rect)
        text3 = self.font.render("Professional", True, (255, 255, 255))
        self.screen.screen.blit(text3, (self.button3_rect.x + 10, self.button3_rect.y + 10))  
        pygame.draw.rect(self.screen.screen, (255, 0, 255), self.button4_rect)
        text4 = self.font.render("Back", True, (255,255,255))
        self.screen.screen.blit(text4, (self.button4_rect.x + 10, self.button4_rect.y + 10))
    def begginer_button(self): 
        game_loop("1v1","Beginner")
    def intermidiate_button(self):
        game_loop("1v1","Intermediate")
    def professional_button(self):
        game_loop("1v1","Professional")


class contrareloj:
    
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 36)
        self.button1_rect = pygame.Rect(300, 200, 200, 50)
        self.button4_rect = pygame.Rect(300, 500, 200, 50)
        self.screen.screen.fill((0, 0, 0))

    def handle_events(self):
        event = pygame.event.wait() 
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if self.button1_rect.collidepoint(mouse_x, mouse_y):
               self.begginer_button()
            elif self.button4_rect.collidepoint(mouse_x, mouse_y): 
                self.screen.current_scene = MainMenu(self.screen)

    def update(self):
        pass
        
    def draw(self):
        pygame.draw.rect(self.screen.screen, (255, 0, 0), self.button1_rect)
        text1 = self.font.render("START", True, (255, 255, 255))
        self.screen.screen.blit(text1, (self.button1_rect.x + 10, self.button1_rect.y + 10)) 
        pygame.draw.rect(self.screen.screen, (255, 0, 255), self.button4_rect)
        text4 = self.font.render("Back", True, (255,255,255))
        self.screen.screen.blit(text4, (self.button4_rect.x + 10, self.button4_rect.y + 10))
    def begginer_button(self): 
        game_loop("contrareloj","Intermediate")
    
    
# Game loop es la funcion principal del juego que permite inicializar cualquier modo de juego, con cualquier dificultad. Estos dos aspectos se le pasan como parámetros
def game_loop(gamemode,difficulty): 
   
    pygame.init()

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Brick Breaker")

    # se inicializan los objetos bases del juego, como los grupos
    all_sprites = pygame.sprite.Group()
    bricks_group = pygame.sprite.Group()
    power_ups_group = pygame.sprite.Group()

    #se crea el mensaje de Game Over para cuando finalice la partida
    printMessage="Game Over"
    font = pygame.font.SysFont("abadi",50)
    text=font.render(printMessage,True, (255, 255, 255), (0, 0, 0))
    textRect=text.get_rect()
    textRect.center = (screen_width/2, screen_height-200)

        
    if(gamemode == "individual"):
        #Se crean los objetos tomando en cuenta la dificultad y modo de juego
        wall = Wall(0,screen_width,difficulty)
        wall.add_bricks()
        bricks_group.add(wall.bricks)
        all_sprites.add(bricks_group)
        ball = Ball(0, screen_width) 
        all_sprites.add(ball)

        paddle = Paddle(0, screen_width )
        all_sprites.add(paddle)

        running = True
        clock = pygame.time.Clock()
        contador=0

        #El loop que mantiene el juego corriendo, revisa colisiones entre todos los objetos, activa powerUps, y finaliza el juego
        while running and not salir:
            contador+=1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    MainMenu(screen)

            for power_up in power_ups_group.sprites():
                if power_up.powerMsg == "":
                    power_up.kill()
                else:
                    power_up.move_down()

            all_sprites.update()

            hits = pygame.sprite.spritecollide(ball, bricks_group, False)
            for brick in hits:

                if ball.rect.colliderect(brick.rect):
                    ball.speed[0] = ball.speed[0]
                    ball.speed[1] = -ball.speed[1]
                    brick.contact_ball(ball.strength)
                    if not brick.is_alive():
                        brick.kill()
                        power_up = PowerUp(brick)
                        if power_up.powerMsg != "":
                            power_ups_group.add(power_up)
            if len(wall.bricks) == 0:
                running = False


            power_up_hits = pygame.sprite.spritecollide(paddle, power_ups_group, True)
            for power_up_hit in power_up_hits:
                print(f"PowerUp Collected: {power_up_hit.powerMsg}")
                if power_up_hit.powerMsg == "Faster Paddle":
                    paddle.speed = 18
                elif power_up_hit.powerMsg == "Stronger Ball":
                    ball.strength = 3
                elif power_up_hit.powerMsg == "Slower Ball":
                    ball.speed[0] = 3
                    ball.speed[1] = 3
                    
            if pygame.sprite.collide_rect(ball, paddle):

                ball.speed[1] = -ball.speed[1]
            if ball.rect.bottom >= screen_height:
                running = False
                


            screen.fill((0, 0, 0))
            
            all_sprites.draw(screen)
            power_ups_group.draw(screen)

            pygame.display.flip()

            clock.tick(fps)
        
    elif (gamemode == "1v1"):
        #Se crean los objetos tomando en cuenta la dificultad y modo de juego
        bricks_groupbot = pygame.sprite.Group()
        power_ups_groupbot = pygame.sprite.Group()
    
        all_sprites = pygame.sprite.Group()
        bricks_group = pygame.sprite.Group()
        power_ups_group = pygame.sprite.Group()
        bricks_groupbot = pygame.sprite.Group()
        power_ups_groupbot = pygame.sprite.Group()
        
        
        wall = Wall(0,screen_width/2,difficulty)
        wall_bot= Wall(screen_width/2,screen_width,difficulty)
        
        wall.add_bricks()
        wall_bot.add_bricks()
        
        bricks_group.add(wall.bricks)
        bricks_groupbot.add(wall_bot.bricks)
        
        all_sprites.add(bricks_group)
        all_sprites.add(bricks_groupbot)
        ball = Ball(0, screen_width/2) 
        ball_bot = Ball(screen_width/2, screen_width)
        all_sprites.add(ball)
        all_sprites.add(ball_bot)

        paddle = Paddle(0, screen_width/2 )
        paddle_bot = PaddleBot(screen_width/2, screen_width)
        all_sprites.add(paddle)
        all_sprites.add(paddle_bot)

        center_line = CenterLine(screen_width / 2, screen_height)
        all_sprites.add(center_line)
        
        running = True
        clock = pygame.time.Clock()
        contador=0
        
        #El loop que mantiene el juego corriendo, revisa colisiones entre todos los objetos, activa powerUps, y finaliza el juego
        while running and not salir:
            contador+=1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            for power_up in power_ups_group.sprites():
                if power_up.powerMsg == "":
                    power_up.kill()
                else:
                    power_up.move_down()

            all_sprites.update()
            paddle_bot.move(ball_bot.get_x_pos())
            
            hits = pygame.sprite.spritecollide(ball, bricks_group, False)
            
            for brick in hits:
                if ball.rect.colliderect(brick.rect):
                    ball.speed[0] = ball.speed[0]
                    ball.speed[1] = -ball.speed[1]
                    brick.contact_ball(ball.strength)
                    if not brick.is_alive():
                        brick.kill()
                        power_up = PowerUp(brick)
                        if power_up.powerMsg != "":
                            power_ups_group.add(power_up)
            if len(wall.bricks) == 0:
                running = False
                
                
            hits_bot = pygame.sprite.spritecollide(ball_bot, bricks_groupbot, False)
            
            for brick_bot in hits_bot:
                if ball_bot.rect.colliderect(brick_bot.rect):
                    ball_bot.speed[0] = ball_bot.speed[0]
                    ball_bot.speed[1] = -ball_bot.speed[1]
                    brick_bot.contact_ball(ball_bot.strength)
                    if not brick_bot.is_alive():
                        brick_bot.kill()
                        print(len(bricks_groupbot))
                        power_up = PowerUp(brick_bot)
                        if power_up.powerMsg != "":
                            power_ups_group.add(power_up)
            if len(wall_bot.bricks) == 0:
                running = False
                
            power_up_hits = pygame.sprite.spritecollide(paddle, power_ups_group, True)
            for power_up_hit in power_up_hits:
                print(f"PowerUp Collected: {power_up_hit.powerMsg}")
                if power_up_hit.powerMsg == "Faster Paddle":
                    paddle.speed = 18
                elif power_up_hit.powerMsg == "Stronger Ball":
                    ball.strength = 3
                elif power_up_hit.powerMsg == "Slower Ball":
                    ball.speed[0] = 3
                    ball.speed[1] = 3
                    
            if pygame.sprite.collide_rect(ball, paddle):
                ball.speed[1] = -ball.speed[1]
            if ball.rect.bottom >= screen_height:
                running = False
            
            power_up_hits_bot = pygame.sprite.spritecollide(paddle_bot, power_ups_groupbot, True)
            for power_up_hit in power_up_hits_bot:
                print(f"PowerUp Collected: {power_up_hit.powerMsg}")
                if power_up_hit.powerMsg == "Faster Paddle":
                    paddle_bot.speed = 18
                elif power_up_hit.powerMsg == "Stronger Ball":
                    ball_bot.strength = 3
                elif power_up_hit.powerMsg == "Slower Ball":
                    ball_bot.speed[0] = 3
                    ball_bot.speed[1] = 3
                    
            if pygame.sprite.collide_rect(ball_bot, paddle_bot):
                ball_bot.speed[1] = -ball_bot.speed[1]
            if ball_bot.rect.bottom >= screen_height:
                running = False

            screen.fill((0, 0, 0))  
            
            all_sprites.draw(screen)
            power_ups_group.draw(screen)

            pygame.display.flip()

            clock.tick(fps) 
    elif(gamemode == "contrareloj"):
        
        all_sprites = pygame.sprite.Group()
        bricks_group = pygame.sprite.Group()
        power_ups_group = pygame.sprite.Group()
        wall = Wall(0,screen_width,"Beginner")
        wall.add_bricks()
        bricks_group.add(wall.bricks)
        all_sprites.add(bricks_group)

        ball = Ball(0, screen_width) 
        all_sprites.add(ball)

        paddle = Paddle(0, screen_width )
        all_sprites.add(paddle)

        running = True
        clock = pygame.time.Clock()
        contador=0
        tiempo_transcurrido = 0

        #El loop que mantiene el juego corriendo, revisa colisiones entre todos los objetos, activa powerUps, y finaliza el juego cuando se pierde o se acaba el tiempo

        while running and not salir:
            contador+=1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            for power_up in power_ups_group.sprites():
                if power_up.powerMsg == "":
                    power_up.kill()
                else:
                    power_up.move_down()

            all_sprites.update()

            hits = pygame.sprite.spritecollide(ball, bricks_group, False)
            for brick in hits:

                if ball.rect.colliderect(brick.rect):
                    ball.speed[0] = ball.speed[0]
                    ball.speed[1] = -ball.speed[1]
                    brick.contact_ball(ball.strength)
                    if not brick.is_alive():
                        brick.kill()  
                        power_up = PowerUp(brick)
                        if power_up.powerMsg != "":
                            power_ups_group.add(power_up)
            if len(wall.bricks) == 0:
                running = False


            power_up_hits = pygame.sprite.spritecollide(paddle, power_ups_group, True)
            for power_up_hit in power_up_hits:
                print(f"PowerUp Collected: {power_up_hit.powerMsg}")
                if power_up_hit.powerMsg == "Faster Paddle":
                    paddle.speed = 18
                elif power_up_hit.powerMsg == "Stronger Ball":
                    ball.strength = 3
                elif power_up_hit.powerMsg == "Slower Ball":
                    ball.speed[0] = 3
                    ball.speed[1] = 3
                    
            if pygame.sprite.collide_rect(ball, paddle):
 
                ball.speed[1] = -ball.speed[1]
            if ball.rect.bottom >= screen_height:
                running = False

            
            
            screen.fill((0, 0, 0))
            
                        
            font = pygame.font.Font(None, 36)
            tiempo_texto = font.render(f"Tiempo: {int(tiempo_transcurrido)-1} segundos", True, (255, 255, 255))

            #Se imprime el tiempo restante en pantalla, y se dibujan los sprites nuevamente
            screen.blit(tiempo_texto, (500, 500))
            all_sprites.draw(screen)
            power_ups_group.draw(screen)
            
            pygame.display.flip()

            clock.tick(fps)
            tiempo_transcurrido += 0.04
            if(tiempo_transcurrido > 22):
                break
            
        
    #se imprime el texto de Game Over en pantalla, luego de 5 segundos elimina todos los objetos dentro de all sprites y limpia la pantalla, para luego ir al menu principal.   
    screen.blit(text,textRect)
    pygame.display.flip()
    time.sleep(5)
    all_sprites.empty()
    screen.fill((0, 0, 0))
    MainMenu(screen)

    #Revisa si el usuario toca la tecla X de la ventana. 
    if salir:
        pygame.quit()
        sys.exit()

#Comandos necesarios para iniciar el juego
screen = Screen(780, 600, 1, 0)
screen.run_game()
        
