import pygame
import random
pygame.init()

clock=pygame.time.Clock()

def movement(randomMoves,direction,states,moves):
    match = []
    upScore = 0
    rightScore = 0
    downScore = 0
    leftScore =0
    growing = False
    choices = []
    if randomMoves <100:

        clear =False
        while clear == False:
            generateDirection = random.randrange(1,5)
            if generateDirection == 1 and direction == "down":
                pass
            elif generateDirection == 2 and direction == "left":
                pass
            elif generateDirection == 3 and direction =="up":
                pass
            elif generateDirection == 4 and direction =="right":
                pass
            else:
                clear = True            

        if generateDirection == 1:
            direction = "up"
        elif generateDirection ==2:
            direction ="right"
        elif generateDirection == 3:
            direction ="down"
        elif generateDirection ==4:
            direction ="left"

    else:
        # states = [danger],[apple],[direction],[action],[score]
        # states = [up,right,down,left],[up,right,down,left],[direction],[nextdirection],[int]
        #for x in range(0,moves-1):                    
         #   if states[x][2][0] == direction:
          #      if states[x][0][0] == states[moves][0][0] and  states[x][0][1] == states[moves][0][1] and states[x][0][2] == states[moves][0][2] and  states[x][0][3] == states[moves][0][3]:
           #         if states[x][1][0] == states[moves][1][0] and states[x][1][1] == states[moves][1][1] and states[x][1][2] == states[moves][1][2] and states[x][1][3] == states[moves][1][3]:
            #                match.extend([x])
        currentState = states[moves][:3]
        for x in range(0,moves-1):
            tempState = states[x][:3]
            if tempState == currentState:
                match.extend([x])


        if len(match) ==0:
            clear =False
            while clear == False:
                generateDirection = random.randrange(1,5)
                if generateDirection == 1 and direction == "down":
                    pass
                elif generateDirection == 2 and direction == "left":
                    pass
                elif generateDirection == 3 and direction =="up":
                    pass
                elif generateDirection == 4 and direction =="right":
                    pass
                else:
                    clear = True            

            if generateDirection == 1:
                direction = "up"
            elif generateDirection ==2:
                direction ="right"
            elif generateDirection == 3:
                direction ="down"
            elif generateDirection ==4:
                direction ="left"
        else:
            upCount, downCount, leftCount, rightCount = 0,0,0,0
            for x in match:
                if states[x][3][0] == "up":
                    upScore = (upScore + states[x][4][0])
                    upCount += 1

                elif states[x][3][0] == "right":
                    rightScore = (rightScore+states[x][4][0])
                    rightCount += 1
                elif states[x][3][0] == "down":
                    downScore = (downScore+states[x][4][0])
                    downCount += 1

                elif states[x][3][0] == "left":
                    leftScore = (leftScore+states[x][4][0])
                    leftCount += 1
                upScore, downScore, leftScore, rightScore = upScore/max(1,upCount), downScore/max(1,downCount), leftScore/max(1,leftCount), rightScore/max(1,rightCount)


            if direction == "up":
                downScore = -8
            elif direction == "right":
                leftScore = -8
            if direction == "down":
                upScore = -8
            if direction == "left":
                rightScore = -8

            if upScore > max(rightScore,downScore,leftScore):
                direction = "up"

            elif rightScore > max(upScore,downScore,leftScore):
                direction = "right"

            elif downScore > max(upScore, rightScore, leftScore):
                direction ="down"

            elif leftScore > max(upScore, rightScore, downScore):
                direction ="left"

            elif upScore == max(rightScore,downScore,leftScore):
                choices.append("up")
                if upScore == rightScore:
                    choices.append("right")
                if upScore == downScore:
                    choices.append("down")
                if upScore == leftScore:
                    choices.append("left")      
                    
                direction = random.choice(choices)

            elif rightScore == max(downScore,leftScore):
                choices.append("right")
                if rightScore == downScore:
                    choices.append("down")
                if rightScore == leftScore:
                    choices.append("left")
                direction = random.choice(choices)
            
            elif downScore == leftScore:
                choices.append("down")
                choices.append("left")
                direction = random.choice(choices)
    return direction

score = 0
highScore = 0
length =1
speed=200

white = (255,255,225)
grey = (237, 237, 237)
darkGrey = (143, 143, 143)
snakeColour=(113, 49, 133)
foodColour=(230, 20, 16)
font = pygame.font.Font('freesansbold.ttf', 28)

screenSize = 600
windowWidth = 600
windowHeight = 700
screen = pygame.display.set_mode([windowWidth, windowHeight])

gridCount = 15
size = screenSize/gridCount
middle = size*int(gridCount/2)
print(middle)

snakeX=middle
snakeY=middle
foodX = random.randrange(0,screenSize,size)
foodY = random.randrange(0,screenSize,size)

direction = "stationary"
prevDirection="stationary"

path = [[middle,middle,direction]]

# states = [danger],[apple],[direction],[action],[score]
# states = [up,right,down,left],[up,right,down,left],[direction],[nextdirection],[int]
states =[[[False,False,False,False],[False,False,False,False],[direction],["undetermined"],[0]]]

moves = 0
randomMoves = 0
canTurn =True
running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.fill((255, 255, 255))
    pygame.draw.rect(screen,(143, 143, 143),(0,600,600,100))
    text = font.render('Score: '+ str(score) + '   HighScore: '+ str(highScore) + '   Time: '+ str(int(pygame.time.get_ticks()/1000)), True, snakeColour, darkGrey)    
    textRect = text.get_rect()
    textRect.center = (windowWidth/2,windowWidth+(windowHeight-windowWidth)/2)
    screen.blit(text,textRect)


    count = 0
    for y in range (0,screenSize,int(size)):
        count=count+1
        for x in range(0,screenSize,int(size*2)):
            if count%2 != 0:
                x=x+size
            pygame.draw.rect(screen,grey,(x,y,size,size))
            

    if direction == "up" and snakeX%size ==0:
        snakeY =snakeY - 5
    elif direction == "right" and snakeY%size==0:
        snakeX = snakeX +5
    elif direction == "down" and snakeX%size ==0:
        snakeY = snakeY+5
    elif direction == "left" and snakeY%size ==0:
        snakeX = snakeX-5
    elif direction == "stationary":
        snakeX = snakeX
        snakeY=snakeY
    else:
        if prevDirection == "up":
            snakeY =snakeY - 5
        elif prevDirection == "right":
            snakeX = snakeX +5
        elif prevDirection == "down":
            snakeY = snakeY+5
        elif prevDirection == "left":
            snakeX = snakeX-5
    
            
    growing = False
    if snakeX==foodX and snakeY==foodY:
        foodX = random.randrange(0,screenSize,size)
        foodY = random.randrange(0,screenSize,size)
        score=score+1
        growing = True
        #print(score)
        path.append([snakeX,snakeY,direction])
        length = length + 1
        #states[moves][4][0]=states[moves][4][0]+5


        for x in range(length):
            while foodX == path[x][0] and foodY==path[x][1]:
                foodX = random.randrange(0,screenSize,size)
                foodY = random.randrange(0,screenSize,size)


    if snakeX%size == 0 and snakeY%size ==0:

        moves = moves + 1
        states.append([[False,False,False,False],[False,False,False,False],[direction],["undetermined"],[0]])

        states[moves-1][3] =[direction]
        path.append([snakeX,snakeY, direction])
        path.pop(0)
        canTurn=True


        # states = [[danger],[apple],[direction],[action],[score]]
        # states = [[up,right,down,left],[up,right,down,left],[direction],[nextdirection],[int]]


        if (snakeX > 0 and snakeX < 5 and direction != "right"):
            states[moves][0][3] = True

        elif (snakeX == screenSize-size and direction != "left"):
            states[moves][0][1] = True

        elif(snakeY == 0 and direction != "down"):
            states[moves][0][0] = True

        elif (snakeY==screenSize-size and direction != "up"):
            states[moves][0][2] = True

        for x in range(length-3):
            if snakeX == path[x][0]+size and snakeY==path[x][1] and growing == False:
                states[moves][0][3]=True 

            if snakeX == path[x][0]-size and snakeY==path[x][1] and growing == False:
                states[moves][0][1]=True 

            if snakeX == path[x][0] and snakeY==path[x][1]+size and growing == False:
                states[moves][0][0]=True 

            if snakeX == path[x][0] and snakeY==path[x][1]-size and growing == False:
                states[moves][0][2]=True 


        if snakeX > foodX:
            states[moves][1][3]=True

        elif snakeX < foodX:
            states[moves][1][1] =True
            
        if snakeY >foodY:
            states[moves][1][0]=True

        elif snakeY < foodY:
            states[moves][1][2] = True

        if (states[moves-1][1][0] == True and direction == "up") or(states[moves-1][1][1] == True and direction == "right") or (states[moves-1][1][2] == True and direction == "down") or (states[moves-1][1][3] == True and direction == "left"):
            states[moves-1][4][0]=states[moves-1][4][0]+1
        else:
            states[moves-1][4][0]=states[moves-1][4][0]-1


        if canTurn == True:
            prevDirection =direction

            direction = movement(randomMoves,direction,states,moves)
            canTurn = False
            if randomMoves <= 100:
                randomMoves = randomMoves + 1
                print(randomMoves)
        if states[moves-1][4][0] != 1:
            print(states[moves-1][4][0])
    pygame.draw.rect(screen,foodColour,(foodX+2,foodY+2,size-4,size-4),0,10)

    for x in range(length):
  #      if path[x][2]== "up":
   #         path[x][1]=path[x][1] -5
    #    if path[x][2]== "right":
     #       path[x][0]=path[x][0] +5
      #  if path[x][2]== "down":
       #     path[x][1]=path[x][1] + 5        
        #if path[x][2]== "left":
         #   path[x][0]=path[x][0] -5

        pygame.draw.rect(screen,snakeColour,(path[x][0], path[x][1], size,size))        
        pygame.draw.rect(screen,(0,0,0),(path[x][0], path[x][1], size,size),5)


    if (snakeX <= 0 and direction=="left") or (snakeX >= screenSize-size and direction == "right") or (snakeY <= 0 and direction =="up") or (snakeY>=screenSize-size and direction =="down"):
        length =1
        highScore = max(highScore,score)
        score =0
        snakeX=middle
        snakeY=middle
        path.clear()
        path = [[middle,middle,direction]]
        foodX = random.randrange(0,screenSize,size)
        foodY = random.randrange(0,screenSize,size)
        states[moves][4][0]=states[moves][4][0]-5
        states[moves-1][4][0]=states[moves-1][4][0]-5

    hit = False
    for x in range(length-2):
        if hit == False:
            if (snakeX == path[x][0]+size and snakeY==path[x][1] and growing == False and direction == "left") or(snakeX == path[x][0]-size and snakeY==path[x][1] and growing == False and direction == "right") or (snakeX == path[x][0] and snakeY==path[x][1]+size and growing == False and direction == "up") or (snakeX == path[x][0] and snakeY==path[x][1]-size and growing == False and direction == "down"):
                length =1
                highScore = max(highScore,score)
                score =0
                snakeX=middle
                snakeY=middle
                path.clear()
                path = [[middle,middle,direction]]
                foodX = random.randrange(0,screenSize,size)
                foodY = random.randrange(0,screenSize,size)
                states[moves][4][0]=states[moves][4][0]-5
                states[moves-1][4][0]=states[moves-1][4][0]-5
                hit = True
            


    pygame.draw.rect(screen,snakeColour,(snakeX,snakeY, size,size) )    
    pygame.draw.rect(screen,(0,0,0),(snakeX,snakeY, size,size),5, 5)

    clock.tick(speed)

    pygame.display.flip()


