import os
import time
import random
import pygame

pygame.init()

fps = 20

scale = 5

n = 100

clock = pygame.time.Clock()
gameDisplay = pygame.display.set_mode([n*scale, n*scale])

cell = chr(219)

f = [[" " for i in range(n)] for j in range(n)]
for i in range(int(n/2)**2):
    f[random.randint(0, n-1)][random.randint(0, n-1)] = cell

def step(board):
    nBoard = [[" " for i in range(n)] for j in range(n)]

    for x in range(n):
        for y in range(n):
            count = 0
            shouldKill = False
            rng = [-1, 0, 1]
            for dx in rng:
                for dy in rng:
                    a = dx
                    b = dy
                    
                    if a == 0 == b:
                        continue

                    if x+a < 0:
                        a+=n
                        shouldKill = True
                    elif x+a >= n:
                        a-=n
                        shouldKill = True
                    if y+b < 0:
                        b+=n
                        shouldKill = True
                    elif y+b >= n:
                        b-=n
                        shouldKill = True

                    #print("At", x, y, ": '",board[x+a][y+b],"' at", x+a, y+b)
                    
                    if board[x+a][y+b] != " ":
                        count+=1

            #if shouldKill:
            #    board[x][y] = " "
            
            #print(x, y, count)
            if board[x][y] == cell:
                if count < 2:
                    nBoard[x][y] = " "
                    #print("removing at", x, y)
                elif count < 4:
                    nBoard[x][y] = cell
                    #print("removing at", x, y)
                else:
                    nBoard[x][y] = " "
            else:
                if count == 3:
                    nBoard[x][y] = cell
                    #print ("Adding at", x, y)
                else:
                    nBoard[x][y] = " "

    return nBoard

gameExit = False

ts = time.time()

shouldTick = False

while not gameExit:
    for event in pygame.event.get(): ##Event Handler
        if event.type == pygame.QUIT:
            gameExit = True
        elif event.type == 5:
            print("Mouse!")
            p = event.pos
            f[int(p[0]/scale)][int(p[1]/scale)] = cell
        elif event.type == 2:
            if event.key == 112:
                shouldTick = not shouldTick

    gameDisplay.fill((0, 0, 0))

    for i in range(len(f)):
        for j in range(len(f[i])):
            if f[i][j] == cell:
                pygame.draw.rect(gameDisplay, (255, 255, 255), [i*scale, j*scale, scale, scale])

    if shouldTick:
        f = step(f[:])[:]

    pygame.display.update()
    clock.tick(fps)

pygame.quit()

