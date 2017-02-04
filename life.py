import os
import time
import random
import pygame

pygame.init()

fps = 10

scale = 5

n = 150

clock = pygame.time.Clock()
gameDisplay = pygame.display.set_mode([n*scale, n*scale])

cell = chr(219)

f = [[" " for i in range(n)] for j in range(n)]
for i in range(int((n/2)**2)):
    f[random.randint(0, n-1)][random.randint(0, n-1)] = cell

def step(board):
    nBoard = [[" " for i in range(n)] for j in range(n)]

    for x in range(n):
        for y in range(n):
            count = 0
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    a = dx
                    b = dy
                    if a == 0 == b:
                        continue
                    if x+a < 0:
                        a+=n
                    elif x+a >= n:
                        a-=n
                    if y+b < 0:
                        b+=n
                    elif y+b >= n:
                        b-=n

                    #print("At", x, y, ": '",board[x+a][y+b],"' at", x+a, y+b)
                    
                    if board[x+a][y+b] != " ":
                        count+=1
            
            #print(x, y, count)
            if board[x][y] == cell:
                if count in [0, 1]:
                    nBoard[x][y] = " "
                    #print("removing at", x, y)
                elif count in [4, 5, 6, 7, 8]:
                    nBoard[x][y] = " "
                    #print("removing at", x, y)
                elif count in [2, 3]:
                    nBoard[x][y] = cell
                else:
                    nBoard[x][y] = " " 
            else:
                if count in [3]:
                    nBoard[x][y] = cell
                    #print ("Adding at", x, y)
                else:
                    nBoard[x][y] = " "

    return nBoard

gameExit = False

ts = time.time()

while not gameExit:
    for event in pygame.event.get(): ##Event Handler
        if event.type == pygame.QUIT:
            gameExit = True
        elif event.type == 5:
            print("Mouse!")

    gameDisplay.fill((0, 0, 0))

    for i in range(len(f)):
        for j in range(len(f[i])):
            if f[i][j] == cell:
                pygame.draw.rect(gameDisplay, (255, 255, 255), [i*scale, j*scale, scale, scale])
    
    f = step(f[:])[:]

    pygame.display.update()
    clock.tick(fps)

pygame.quit()

