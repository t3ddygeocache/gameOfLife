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

Brian's Brain:

https://en.wikipedia.org/wiki/Brian%27s_Brain

In each time step, a cell turns on if it was off but had exactly two neighbors that were on, just like the birth rule for Seeds. All cells that were "on" go into the "dying" state, which is not counted as an "on" cell in the neighbor count, and prevents any cell from being born there. Cells that were in the dying state go into the off state. 

briansBrain:

Same as gameOfLife but with an extra state for dying and with new rules as above

briansBrainAnimation:

Same as gameOfLifeAnimation but with an extra state for dying and with new rules as above

briansBrainInteractive:

Same as gameOfLife but with an extra state for dying and with new rules as above. Middle mouse click adds a dying cell
