import pygame
import random
import math
from pygame import mixer

# Initialize the pygame
pygame.init()

# Create screen
screen=pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("Space Invader")
icon=pygame.image.load("D:\Projects\C# Projects\C-Project\Space Invader\spaceship.png")
pygame.display.set_icon(icon)

# Background
backgroundImg=pygame.image.load("D:\Projects\C# Projects\C-Project\Space Invader\\background.png")

# Background Sound
mixer.music.load("D:\Projects\C# Projects\C-Project\Space Invader\\background.wav")
mixer.music.play(-1)

# Player
playerImg=pygame.image.load("D:\Projects\C# Projects\C-Project\Space Invader\space_invaders.png")
playerX=370
playerY=500
playerX_change=0
playerY_change=0

# Enemy
enemyImg=[]
enemyX=[]
enemyY=[]
enemyY=[]
enemyX_change=[]
enemyY_change=[]
num_of_enemies=8

#enemyImg="D:\Projects\C# Projects\C-Project\Space Invader\enemy1.png"

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('D:\Projects\C# Projects\C-Project\Space Invader\enemy1.png'))
    enemyX.append(random.randint(0,735))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(2)
    enemyY_change.append(20)

# Bullet
bulletImg=pygame.image.load("D:\Projects\C# Projects\C-Project\Space Invader\\bullet.png")
bulletX=0
bulletY=500
bulletX_change=0
bulletY_change=5
bullet_state="ready"  #ready-You can't see the bullet, fire-You can see the bullet


# Score
score_value=0
font=pygame.font.Font('D:\Projects\C# Projects\C-Project\Space Invader\BabyBoomer.ttf',32)
textX=10
textY=10


def show_score(x,y):
    score=font.render("Score :" +str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))
# Game over Text
font1=pygame.font.Font('D:\Projects\C# Projects\C-Project\Space Invader\BabyBoomer.ttf',128)
def game_over_text():
    game_over=font1.render("GAME OVER",True,(255,255,255))
    screen.blit(game_over,(150,250))


def player(x,y):
    screen.blit(playerImg, (x,y))

def enemy(x,y,i):
    screen.blit(enemyImg[i],(x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bulletImg,(x+16, y+10))

# Collision of Bullet and Enemy
def isCollision(enemyX,bulletX,enemyY,bulletY):
    distance=math.sqrt((math.pow(enemyX-bulletX,2))+(math.pow(enemyY-bulletY,2)))
    if distance<15:
        return True
    else:
        return False    
# Game Loop
running=True
while running:

    # screen.fill((R,G,B))
    screen.fill((0,0,0))

    # Background Image
    screen.blit(backgroundImg,(0,0))

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

        # If keystroke is pressed check whether its left or right
        if event.type==pygame.KEYDOWN: #or event.type==pygame.MOUSEBUTTONDOWN:
            print("A Key has been pressed or mouse button is pressed")
            if event.key==pygame.K_LEFT:
                print("Left arrow key is pressed")
                playerX_change=-5

            if event.key==pygame.K_RIGHT:
                print("Right arrow key is pressed")
                playerX_change=5
            if event.key==pygame.K_SPACE : #or event.type==pygame.MOUSEBUTTONDOWN:
                if bullet_state is "ready":
                    bullet_sound=mixer.Sound('D:\Projects\C# Projects\C-Project\Space Invader\laser.wav')
                    bullet_sound.play()
                    bulletX=playerX
                    print("Spacebar key is pressed")
                    fire_bullet(playerX,bulletY)

        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT  or event.key==pygame.K_RIGHT:
                print("Key has been released") 
                playerX_change=0           

    playerX+=playerX_change
    
    # Defining the boundary for spaceship
    if playerX<=0:
        playerX=0
    if playerX>=736:
        playerX=736

    #Defining the boundary for enemy and Enemy movement
    for i in range(num_of_enemies):

        # Game Over
        if enemyY[i]>460:
            for j in range(num_of_enemies):
                enemyY[j]=2000
            game_over_text() 
            break   
        enemyX[i]+=enemyX_change[i]
        
        if enemyX[i]<=0:
            enemyX_change[i]=3
            enemyY[i]+=enemyY_change[i]
        elif enemyX[i]>=736:
            enemyX_change[i]=-3
            enemyY[i]+=enemyY_change[i]

        # Collision
        collision=isCollision(enemyX[i],enemyY[i],bulletX,bulletY)
        if collision:
            explosion_sound=mixer.Sound('D:\Projects\C# Projects\C-Project\Space Invader\explosion.wav')
            explosion_sound.play()
            bulletY=500
            bullet_state="ready"
            score_value+=1
            #print(score)
            enemyX[i]=random.randint(0,735)
            enemyY[i]=random.randint(50,150)   
        enemy(enemyX[i],enemyY[i],i)
        
    # Bullet movement
    if bulletY<=0:
        bulletY=500
        bullet_state="ready"

    if bullet_state is "fire":
        fire_bullet(bulletX,bulletY)
        bulletY-=bulletY_change

    

    player(playerX,playerY)
    show_score(textX,textY)
    pygame.display.update()        