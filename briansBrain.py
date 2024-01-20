import random
import pygame as py

cellWidth = 100
screenWidth = 1000
frameRate = 10

cellPix = screenWidth // cellWidth
cells = []

for i in range(cellWidth ** 2):
    cells.append(random.randint(0,1))
    
py.init()
screen = py.display.set_mode((screenWidth,screenWidth))
screen.fill((255,255,255))
clock = py.time.Clock()

def calcNeighbourVal(neighbourCount, cell):
    if cell == 1:
        return (neighbourCount + 1)
    else:
        return neighbourCount

#0 - off, 1 - on, 2 - dying
while True:
    
    newCells = []
    
    for i in range(len(cells)):
        
        x = i % cellWidth
        y = i // cellWidth
        
        if x == 0 or x == (cellWidth-1) or y == 0 or y == (cellWidth-1):
            newCells.append(1)
        else:
            neighbourCount = 0
            neighbourCount = calcNeighbourVal(neighbourCount,cells[i-1])
            neighbourCount = calcNeighbourVal(neighbourCount,cells[i+1])
            neighbourCount = calcNeighbourVal(neighbourCount,cells[i-cellWidth])
            neighbourCount = calcNeighbourVal(neighbourCount,cells[i+cellWidth])
            neighbourCount = calcNeighbourVal(neighbourCount,cells[i-1-cellWidth])
            neighbourCount = calcNeighbourVal(neighbourCount,cells[i+1-cellWidth])
            neighbourCount = calcNeighbourVal(neighbourCount,cells[i-1+cellWidth])
            neighbourCount = calcNeighbourVal(neighbourCount,cells[i+1+cellWidth])
            
            if cells[i] == 0:
                if neighbourCount == 2:
                    newCells.append(1)
                else:
                    newCells.append(0)
            elif cells[i] == 1:
                newCells.append(2)
            else:
                newCells.append(0)
        
        if cells[i] == 1:
            col = (0,0,0)
        elif cells[i] == 2:
            col = (128, 128, 128)
        else:
            col = (255, 255, 255)
            
        screen.fill(col, rect=((i % cellWidth) * cellPix, (i // cellWidth) * cellPix, cellPix, cellPix))
        
    cells = newCells.copy()
    
    for i in range(0, screenWidth+1, screenWidth // cellWidth):
        py.draw.line(screen, (0,0,0), (i, 0), (i, screenWidth), width = 1)
        py.draw.line(screen, (0,0,0), (0, i), (screenWidth, i), width = 1)
        
    py.display.update()
    clock.tick(frameRate)
    
    events = py.event.get()
    for event in events:                
        if event.type == py.KEYDOWN:
            if event.key == py.K_q:
                py.quit()