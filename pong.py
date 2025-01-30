import time
import pygame
import random

pygame.init()

font = pygame.font.SysFont("arial",24)
screen = pygame.display.set_mode((1600, 1000))

player_one_wins = 0
player_two_wins = 0

wins = font.render(str(player_one_wins)+" "+str(player_two_wins),100,"white")

clock = pygame.time.Clock()
running = True


paddle_width = screen.get_width()/3
paddle_height = screen.get_height()/25
player_one_pos = pygame.Vector2(screen.get_width()/2,screen.get_height())
player_two_pos = pygame.Vector2(screen.get_width()/2,0)
ball_pos = pygame.Vector2(screen.get_width()/2, screen.get_height()/2)
mvelocity = screen.get_height()/2.5
vert_velocity = random.choice([-1,1]) * mvelocity
horiz_velocity = random.choice([-mvelocity/2, mvelocity/2])


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fps = 60
    dt = clock.tick(60) / 1000
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE
    player_one = pygame.Rect(player_one_pos.x-paddle_width/2,player_one_pos.y-paddle_height,paddle_width,paddle_height)
    player_two = pygame.Rect(player_two_pos.x-paddle_width/2,player_two_pos.y,paddle_width,paddle_height)
    
    pygame.draw.rect(screen,"blue",player_one)
    pygame.draw.rect(screen,"red",player_two)
    circleRect = pygame.draw.circle(screen, "white", ball_pos, min(screen.get_height(),screen.get_width())/50)
    
    keys = pygame.key.get_pressed()
    if (keys[pygame.K_a]):
        player_one_pos.x -= 1000 * dt
    if (keys[pygame.K_d]):
        player_one_pos.x += 1000 * dt
    if (keys[pygame.K_LEFT]):
        player_two_pos.x -= 1000 * dt
    if (keys[pygame.K_RIGHT]):
        player_two_pos.x += 1000 * dt
            
    if (circleRect.colliderect(player_one)): 
        horiz_velocity =  (ball_pos.x - player_one_pos.x)*3
        vert_velocity *= -1
        
    if (circleRect.colliderect(player_two)):
        horiz_velocity = (ball_pos.x - player_two_pos.x)*3
        vert_velocity *= -1
        
    if (circleRect.left <= 0 or circleRect.right >= screen.get_width()):
        horiz_velocity *= -1
    
    if (circleRect.top <= 0):
        ball_pos = pygame.Vector2(screen.get_width()/2, screen.get_height()/2)
        vert_velocity = random.choice([-1,1]) * mvelocity
        horiz_velocity = random.choice([-mvelocity/2, mvelocity/2])
        player_one_wins += 1

        
    if (circleRect.bottom >= screen.get_height()):
        ball_pos = pygame.Vector2(screen.get_width()/2, screen.get_height()/2)
        vert_velocity = random.choice([-1,1]) * mvelocity
        horiz_velocity = random.choice([-mvelocity/2, mvelocity/2])
        player_two_wins += 1
    
    ball_pos.y += vert_velocity * dt
    ball_pos.x += horiz_velocity * dt
    
    wins = font.render(f"{player_one_wins} - {player_two_wins}", True, "white")
    screen.blit(wins, (screen.get_width()/2 - 50, screen.get_height()/2 - 50))
    # flip() the display to put your work on screen
    pygame.display.flip()
    
pygame.quit()


