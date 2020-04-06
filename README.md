# Python implementation of Conway's Game of Life
The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970.
The game is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input. One interacts with the Game of Life by creating an initial configuration and observing how it evolves.

The universe of the Game of Life is an infinite, two-dimensional orthogonal grid of square cells, each of which is in one of two possible states, alive or dead. Every cell interacts with its eight neighbours, which are the cells that are horizontally, vertically, or diagonally adjacent. At each step in time, the following transitions occur :
- Any live cell with fewer than two live neighbours dies, as if by underpopulation.
- Any live cell with two or three live neighbours lives on to the next generation.
- Any live cell with more than three live neighbours dies, as if by overpopulation.
- Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

## Prerequisites
- Python 3.6 or greater
- numpy
- scipy
- matplotlib

## Getting started
Start by choosing all settings l9-l12 :
```python
shape = (300, 300) # Shape of the grid (width x height)
density = 0.30 # ~Living cells density at t0
n_steps = 250 # Number of steps
delay =  0.1 # Delay between each frame in s
```
Then initialize your grid l34 (default):
```python
space = gen(shape, density) # Create a random grid
```
Or import a predefined pattern l35-l36 (simply uncomment):
```python
#with open('patterns/pentadecathlon.pickle', 'rb') as handle: # Import a pattern
    #space = pickle.load(handle)
```
You can run *file.py*.
Matplotlib will run an animation and save it.
![Example animation (200,200)](https://github.com/gildas-ev/Game-of-Life/blob/master/Example.png)

## Author
Hi ! My name is Gildas, I'm 15 and I have been learning programming since 2019. I am French. I love sciences and I want to become an engineer.


## License
This project is licensed under the MIT License - see the LICENSE.md file for details
