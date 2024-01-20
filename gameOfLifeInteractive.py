import random, time
import pygame as py

cellWidth = 25
screenWidth = 1000
frameRate = 10

running = False
cellPix = screenWidth // cellWidth
cells = []

for i in range(cellWidth ** 2):
    cells.append(0)
    
py.init()
screen = py.display.set_mode((screenWidth,screenWidth))
screen.fill((255,255,255))
clock = py.time.Clock()

while not running:
    
    for i in range(len(cells)):
        if cells[i]:
            col = (0,0,0)
        else:
            col = (255, 255, 255)
        screen.fill(col, rect=((i % cellWidth) * cellPix, (i // cellWidth) * cellPix, cellPix, cellPix)) #Draw the cells as they are being updated
        
    for i in range(0, screenWidth+1, screenWidth // cellWidth): #Drawing the grid
        py.draw.line(screen, (0,0,0), (i, 0), (i, screenWidth), width = 1)
        py.draw.line(screen, (0,0,0), (0, i), (screenWidth, i), width = 1)
    
    events = py.event.get()
    for event in events:
        if py.mouse.get_pressed()[0] or py.mouse.get_pressed()[2]: #[0] is left click, [2] is for right click
            pos = py.mouse.get_pos()
            xIndex = pos[0] // cellPix #Finding the coordinates of the cell that was clicked on
            yIndex = pos[1] // cellPix
            index = yIndex * cellWidth + xIndex

            if py.mouse.get_pressed()[0]: #Left click adds cells, left click removes cells
                cells[index] = 1
            else:
                cells[index] = 0
                
        if event.type == py.KEYDOWN: #Press enter to begin the iteration
            if event.key == py.K_RETURN:
                running = True
                break
                    
    py.display.update()
    clock.tick(60) #60 FPS so it is responsive when editing cells
        

while running:
    newCells = []
    for i in range(len(cells)):
            
        x = i % cellWidth
        y = i // cellWidth
        
        if x == 0 or x == (cellWidth-1) or y == 0 or y == (cellWidth-1):
            newCells.append(0) #A border of living cells permanently around the edges
        else:
            neighbourCount = 0
            neighbourCount += cells[i-1]
            neighbourCount += cells[i+1]
            neighbourCount += cells[i-cellWidth]
            neighbourCount += cells[i+cellWidth]
            neighbourCount += cells[i-1-cellWidth]
            neighbourCount += cells[i+1-cellWidth]
            neighbourCount += cells[i-1+cellWidth]
            neighbourCount += cells[i+1+cellWidth]
            
            if cells[i]:
                if neighbourCount == 2 or neighbourCount == 3:
                    newCells.append(1)
                else:
                    newCells.append(0)
            else:
                if neighbourCount == 3:
                    newCells.append(1)
                else:
                    newCells.append(0)
        
        if cells[i] == 1:
            col = (0,0,0)
        else:
            col = (255, 255, 255)
        screen.fill(col, rect=((i % cellWidth) * cellPix, (i // cellWidth) * cellPix, cellPix, cellPix))
        
    if cells == newCells: #If the iteration is the same as the last, then it won't change again so stop iterating
        break
    
    cells = newCells.copy()
    
    for i in range(0, screenWidth+1, screenWidth // cellWidth): #Drawing the grid
        py.draw.line(screen, (0,0,0), (i, 0), (i, screenWidth), width = 1)
        py.draw.line(screen, (0,0,0), (0, i), (screenWidth, i), width = 1)
        
    py.display.update()
    clock.tick(frameRate)
    
time.sleep(3)
py.quit()