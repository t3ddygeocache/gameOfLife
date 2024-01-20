# gameOfLife
Based on Conway's Game Of Life

gameOfLifeAnimation:

cellWidth is the number of cells wide and tall the board is. imgWidth is the width in pixels of the output images. If grid is true, lines will be drawn separating each cell. 
outputDir is where the images will be saved to, the directory must exist as the program can't create the folder if it isn't there. iterationNum is the number of generations to 
calculate and is how many images will be saved, however if the cells stop changing before that number of generations, it will stop early.

gameOfLifeInteractive:

cellWidth is the number of cells wide and tall the board is. screenWidth is the size of the pygame window displaying the board. frameRate is the number of generations per second. Left click adds living cells, right click removes cells and pressing enter starts the iteration. Pressing Q closes the pygame window
