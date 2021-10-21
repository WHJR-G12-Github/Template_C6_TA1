import pygame,math,random

pygame.init()
screen = pygame.display.set_mode((400,600))

pygame.display.set_caption("Shooting Spaceship")
background_image = pygame.image.load("bg2.jpg").convert()
player_image = pygame.image.load("s4.png").convert_alpha()
enemy_image = pygame.image.load("e3.png").convert_alpha()
player=pygame.Rect(200,200,30,30)

angle=0
change=0
distance=5
forward=False

xvel=[]
yvel=[]
enemies=[]
enemycount=10

# Create a 'bullet'
# Create a 'bullet' at [200,200] as x,y location
# 'width' and 'height' of 'bullet' is 5


# Create a variable 'bulletState' to denote whether it is "ready" or "fired"
# Initially, 'bullet' will be in "ready" state


# Create YELLOW color by mixing RED and GREEN and name it 'YELLOW'


for i in range(enemycount): 
  enemies.append(pygame.Rect(random.randint(0,400),random.randint(0,600),20,20))
  xvel.append(random.randint(-3,3))
  yvel.append(random.randint(-3,3))

def newxy(x,y,distance,angle):
  angle=math.radians(angle+90)
  xnew=x+(distance*math.cos(angle))
  ynew=y-(distance*math.sin(angle))
  return xnew,ynew

while True:
  screen.blit(background_image,[0,0])
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      
    if event.type == pygame.KEYDOWN:
       if event.key == pygame.K_LEFT:
          change = 6
       if event.key ==pygame.K_RIGHT:
        change = -6 
       if event.key == pygame.K_UP:
        forward = True
        
       # Check if SPACE key is pressed and 'bulletState' is "ready"
       
           # Assign "fired" to 'bulletState'
          
           # Assign 'angle' value to another variable 'bangle'
           bangle=angle
        
    if event.type == pygame.KEYUP:
      if event.key ==pygame.K_LEFT or event.key == pygame.K_RIGHT:
          change = 0
      if event.key == pygame.K_UP:
        forward = False 
  i=0    
  for enemy in enemies:
      enemy.x=enemy.x + xvel[i]
      enemy.y=enemy.y + yvel[i]
  
  
      if enemy.x < -250 or enemy.x > 650 :
        xvel[i] = -1*xvel[i]
      
      if enemy.y < -250 or enemy.y > 850:  
        yvel[i] = -1*yvel[i]
      
      screen.blit(enemy_image,enemy)  
      i=i+1
  
  # Check if 'bulletState' is "ready" and assign  x,y coordinates
  # x,y coordinates are assigned such that bullet is hidden in 'player' image
  
  
  
  # Draw 'bullet' on 'screen' in 'YELLOW' color    
  
  
  if forward:
      player.x,player.y=newxy(player.x, player.y, distance, angle)  
  if player.x<0:
      player.x=400
  if player.x>400:
      player.x=0
  if player.y<0:
      player.y=600
  if player.y>600:
      player.y=0
      
  
  angle = angle + change
  newimage=pygame.transform.rotate(player_image,angle) 
  screen.blit(newimage ,player)
  
  

  pygame.display.update()
  pygame.time.Clock().tick(30)
  
  
