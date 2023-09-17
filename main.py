import pygame, sys, random

# pygame setup
pygame.init()
clock = pygame.time.Clock()

# Screen setup:
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
running = True
dt = 0

pong_ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30, 30)
player1 = pygame.Rect(screen_width - 20, screen_height/2 - 70, 10, 140)
player2 = pygame.Rect(10, screen_height/2 - 70, 10, 140)

dark_grey = pygame.Color("grey12")
light_grey = (200,200,200)

ball_speed_x = 10 * random.choice((1, -1))
ball_speed_y = 10 * random.choice((1, -1))
player1_speed = 750
player2_speed = 750

while running:
    # User inputs:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    pong_ball.x += ball_speed_x
    pong_ball.y += ball_speed_y

    if pong_ball.top <= 0 or pong_ball.bottom >= screen_height:
        ball_speed_y *= -1
    if pong_ball.left <= 0 or pong_ball.right >= screen_width:
        pong_ball.center = (screen_width/2 , screen_height/2)
        ball_speed_y *= random.choice((1, -1))
        ball_speed_x *= random.choice((1, -1))

    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player1.y -= player1_speed * dt
    if keys[pygame.K_s]:
        player1.y += player1_speed * dt

    for player in player1, player2:
            if player.top <= 0:
                player.top = 0
            if player.bottom >= screen_height:
                player.bottom = screen_height
            if pong_ball.colliderect(player):
                ball_speed_x *= -1
                
            if player2.top < pong_ball.y:
                player2.y += player2_speed * dt
            if player2.bottom > pong_ball.y:
                player2.y -= player2_speed * dt

    # Drawing the elements on screen
    screen.fill(dark_grey)
    pygame.draw.rect(screen, light_grey, player1)
    pygame.draw.rect(screen, light_grey, player2)
    pygame.draw.ellipse(screen, light_grey, pong_ball)
    pygame.draw.aaline(screen, light_grey, (screen_width/2,0), (screen_width/2, screen_height))
            
    pygame.display.flip() # Draw smt from the previous loop
    dt = clock.tick(60) / 1000
  
    