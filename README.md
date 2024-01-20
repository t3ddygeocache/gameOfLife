# gameOfLife
Based on Conway's Game Of Life

General:
For gameOfLife and gameOfLifeAnimation, I made the borders living cells as this created more interesting patterns and kept it going for longer than if the cells were dead. I left them dead for gameOfLifeInteractive so it is up to the user. 

gameOfLife:
Shows iteration on a random state in a pygame window. cellWidth is the number of cells wide and tall the board is. screenWidth is the size of the pygame window displaying the board. frameRate is the number of generations per second. Press Q to close the pygame window.

gameOfLifeAnimation:

Outputs an image of each generation for use in creating an animation, uses a random starting state. cellWidth is the number of cells wide and tall the board is. imgWidth is the width in pixels of the output images. If grid is true, lines will be drawn separating each cell. outputDir is where the images will be saved to, the directory must exist as the program can't create the folder if it isn't there. iterationNum is the number of generations to calculate and is how many images will be saved, however if the cells stop changing before that number of generations, it will stop early.

gameOfLifeInteractive:

Allows you to design the starting state of the cells. cellWidth is the number of cells wide and tall the board is. screenWidth is the size of the pygame window displaying the board. frameRate is the number of generations per second. Left click adds living cells, right click removes cells and pressing enter starts the iteration. Pressing Q closes the pygame window
