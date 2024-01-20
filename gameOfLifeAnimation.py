import random
from PIL import Image

cellWidth = 50
imgWidth = 1000
grid = True
outputDir = './GoL/' #Where the images will be saved
iterationNum = 100

scaleFactor = imgWidth // cellWidth #How much to scale up the board for the image
cellPix = imgWidth // cellWidth #The width of each cell in the image

cells = []
for i in range(cellWidth ** 2):
    cells.append(random.randint(0,1)) #Fill the board with random noise

counter = 0

while counter < iterationNum:
    
    counter += 1
    newCells = []
    
    for i in range(len(cells)):
        x = i % cellWidth
        y = i // cellWidth
        
        if x == 0 or x == (cellWidth-1) or y == 0 or y == (cellWidth-1): #Border of living cells around the edges
            newCells.append(1)
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
            
            if cells[i]: #If a cell is living, anything other than 2 or 3 living neighbours will kill it 
                if neighbourCount == 2 or neighbourCount == 3: 
                    newCells.append(1) 
                else:
                    newCells.append(0)
            else: #If a cell is dead, 3 living neighbours revives it
                if neighbourCount == 3:
                    newCells.append(1)
                else:
                    newCells.append(0)
        
    if cells == newCells: #If the board stays the same, it won't change again so stop iterating
        break
    
    Img = Image.new('1', [imgWidth, imgWidth])
    data = Img.load()
    index = 0
    for x in range(imgWidth):
        for y in range(imgWidth):
            
            pixX = x // scaleFactor
            pixY = y // scaleFactor
            index = pixY * cellWidth + pixX #Scale the image coordinates down to the board coordinates
            
            if (x % cellPix == 0 or y % cellPix == 0) and grid: #If it is on the border between 2 cells and the
                #grid should be displayed, the pixel should be black
                data[x,y] = (0) #0 is black, 1 is white
            elif cells[index]: #Pixel is the same colour as the corresponding cell
                data[x,y] = (0)
            else:
                data[x,y] = (1)
            index += 1
    Img.save(f"{outputDir}img{counter}.png")
    cells = newCells.copy()
    