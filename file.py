# Imports
import numpy as np
from scipy.ndimage import convolve
from matplotlib import pyplot as plt
from matplotlib import animation
import pickle
import time

shape = (300, 300) # Shape of the grid (width x height)
density = 0.30 # ~Living cells density at t0
n_steps = 250 # Number of steps
delay =  0.1 # Delay between each frame in s

def gen(shape, density): # Generate the grid
    space = np.random.uniform(size=(shape)) # Random float array (between 0 and 1)
    space = np.where(space < density, 1, 0) # Where space < density cells are living
    return space

def step(space): # Compute the next step of space
    initial_shape = space.shape # Save initial shape
    pattern = np.array([[1,1,1], [1,0,1], [1,1,1]])
    neighbours = convolve(space, pattern, mode='constant') # Convolve sum the neighbours of each cells, according to the pattern
    space, neighbours = space.flatten(), neighbours.flatten() # From 2d to 1d array
    def new_value(space, neighbours): # Return the new cell state
        if neighbours == 3: # If there are 3 neighbours, the cell will be alive
            return 1
        elif neighbours == 2: # If there are 2 neighbours, the state of the cell will not change
            return space
        return 0 # In all other cases, the cell will die
    new = np.array(list(map(new_value, space, neighbours))) # Compute next step array by mapping with new_value function
    return new.reshape(initial_shape) # Return the reshaped new array

# Initialize space (create a random grid or import a pattern)
space = gen(shape, density) # Create a random grid
#with open('patterns/pentadecathlon.pickle', 'rb') as handle: # Import a pattern
    #space = pickle.load(handle)

# Compute all steps
snapshots = [space]
for loop in range(n_steps-1):
    snapshots.append(step(snapshots[-1]))

# Create figure
fig = plt.figure()
im = plt.imshow(space, interpolation='none', aspect='auto', vmin=0, vmax=1)

def animate_func(i): # Return each step
    im.set_array(snapshots[i])
    return [im]

anim = animation.FuncAnimation(fig,
                               animate_func,
                               frames = n_steps,
                               interval = (delay*1000)) # Animation

anim.save(f'{int(time.time())}.html') # Save the animation in dir
plt.show()
