'''
The Tower of Hanoi problem involves 3 towers. A number of rings decreasing in size are placed on one tower. 
All rings must then be moved to another tower, but at no point can a larger ring be placed on a smaller ring.

Your task: Given a number of rings, return the MINIMUM number of moves needed to move all the rings from 
one tower to another.

'''

def tower_of_hanoi(rings):
    #your code here
    return 2 ** rings - 1