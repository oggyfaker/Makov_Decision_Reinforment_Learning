import numpy as np 

def transition_model(row , col ,action ,tot_row , tot_col):
    if (row > tot_row - 1 or col > tot_col-1):
        print("ERROR: the index is out of range...")
        return None
    
    extend_world = np.zeros((tot_row+2, tot_col+2))

    #Obstackle 1
    if (row == 1 and col == 1): return extend_world[1:9, 1:10]
    #Obstackle 2
    if (row == 1 and col == 2): return extend_world[1:9, 1:10] 
    #Obstackle 3
    if (row == 1 and col == 3): return extend_world[1:9, 1:10]
    #Obstackle 4
    if (row == 1 and col == 4): return extend_world[1:9, 1:10]
    #Obstackle 24
    if (row == 1 and col == 5): return extend_world[1:9, 1:10]
    #Obstackle 5
    if (row == 1 and col == 6): return extend_world[1:9, 1:10]
    #Obstackle 6
    if (row == 1 and col == 7): return extend_world[1:9, 1:10]  
    
    #Obstackle 7
    if (row == 2 and col == 1): return extend_world[1:9, 1:10]
    #Obstackle 8
    if (row == 2 and col == 7): return extend_world[1:9, 1:10]
    
    #Obstackle 9
    if (row == 3 and col == 1): return extend_world[1:9, 1:10]
    #Obstackle 10
    if (row == 3 and col == 7): return extend_world[1:9, 1:10]
    
    #Obstackle 11
    if (row == 4 and col == 1): return extend_world[1:9, 1:10]
    #Obstackle 12
    if (row == 4 and col == 2): return extend_world[1:9, 1:10]
    #Obstackle 13
    if (row == 4 and col == 3): return extend_world[1:9, 1:10]
    #Obstackle 14
    if (row == 4 and col == 7): return extend_world[1:9, 1:10]
    
    #Obstackle 15
    if (row == 5 and col == 7): return extend_world[1:9, 1:10]
    #Obstackle 16
    if (row == 6 and col == 2): return extend_world[1:9, 1:10]
    #Obstackle 17
    if (row == 6 and col == 3): return extend_world[1:9, 1:10]
    #Obstackle 18
    if (row == 6 and col == 4): return extend_world[1:9, 1:10]
    #Obstackle 19
    if (row == 6 and col == 5): return extend_world[1:9, 1:10]
    #Obstackle 20
    if (row == 6 and col == 6): return extend_world[1:9, 1:10]
    #Obstackle 21
    if (row == 6 and col == 7): return extend_world[1:9, 1:10]

    #terninal state    
    if (row == 0 and col == 2): return extend_world[1:9, 1:10]
    #punish state
    if (row == 0 and col == 3): return extend_world[1:9, 1:10]
#------------------------------------
    if action == "up":
        row += 1
        col += 1
        extend_world[row-1, col] = 0.8 
        extend_world[row, col-1] = 0.1
        extend_world[row, col+1] = 0.1
    
    elif action == "down":
        row += 1
        col += 1
        extend_world[row+1,  col] = 0.8
        extend_world[row , col-1] = 0.1
        extend_world[row , col+1] = 0.1
    
    elif action == "left":
        row += 1
        col += 1
        extend_world[row, col-1]  = 0.8
        extend_world[row-1, col]  = 0.1
        extend_world[row+1, col]  = 0.1
    
    elif action == "right":
        row += 1
        col += 1
        extend_world[row, col+1] = 0.8
        extend_world[row-1, col] = 0.1
        extend_world[row+1, col] = 0.1

    
    #reset the obstacle 
    if extend_world[2,2] != 0:
        extend_world[row,col] += extend_world[2,2]
    extend_world[2,2] = 0.0
    
    if extend_world[2,3] != 0:
        extend_world[row,col] += extend_world[2,3]
    extend_world[2,3] = 0.0

    if extend_world[2,4] != 0:
        extend_world[row,col] += extend_world[2,4]
    extend_world[2,4] = 0.0

    if extend_world[2,5] != 0:
        extend_world[row,col] += extend_world[2,5]
    extend_world[2,5] = 0.0

    if extend_world[2,6] != 0: 
        extend_world[row,col] += extend_world[2,6]
    extend_world[2,6] = 0.0
    
    if extend_world[2,7] != 0:
        extend_world[row,col] += extend_world[2,7]
    extend_world[2,7] = 0.0

    if extend_world[2,8] != 0:
        extend_world[row,col] += extend_world[2,8]
    extend_world[2,8] = 0.0

    if extend_world[3,2] != 0:
        extend_world[row,col] += extend_world[3,2]
    extend_world[3,2] = 0.0

    if extend_world[3,8] != 0:
        extend_world[row,col] += extend_world[3,8]
    extend_world[3,8] = 0.0

    if extend_world[4,2] != 0:
        extend_world[row,col] += extend_world[4,2]
    extend_world[4,2] = 0.0

    if extend_world[4,8] != 0:
        extend_world[row,col] += extend_world[4,8]
    extend_world[4,8] = 0.0

    if extend_world[5,2] != 0:
        extend_world[row,col] += extend_world[5,2]
    extend_world[5,2] = 0.0

    if extend_world[5,3] != 0:
        extend_world[row,col] += extend_world[5,3]
    extend_world[5,3] = 0.0

    if extend_world[5,4] != 0:
        extend_world[row,col] += extend_world[5,4]
    extend_world[5,4] = 0.0

    if extend_world[5,8] != 0:
        extend_world[row,col] += extend_world[5,8]
    extend_world[5,8] = 0.0

    if extend_world[6,8] != 0:
        extend_world[row,col] += extend_world[6,8]
    extend_world[6,8] = 0.0

    if extend_world[7,3] != 0:
        extend_world[row,col] += extend_world[7,3]
    extend_world[7,3] = 0.0

    if extend_world[7,4] != 0:
        extend_world[row,col] += extend_world[7,4]
    extend_world[7,4] = 0.0

    if extend_world[7,5] != 0:
        extend_world[row,col] += extend_world[7,5]
    extend_world[7,5] = 0.0

    if extend_world[7,6] != 0:
        extend_world[row,col] += extend_world[7,6]
    extend_world[7,6] = 0.0

    if extend_world[7,7] != 0:
        extend_world[row,col] += extend_world[7,7]
    extend_world[7,7] = 0.0

    if extend_world[7,8] != 0:
        extend_world[row,col] += extend_world[7,8]
    extend_world[7,8] = 0.0
   
    #Control bouncing
    for row in range(0, 10):   
        if(extend_world[row, 0] != 0): 
            extend_world[row, 1] += extend_world[row, 0]
        
        if(extend_world[row, 10] != 0): 
            extend_world[row, 9] += extend_world[row, 10]
    
    for col in range(0,11):
        if(extend_world[0, col] != 0): 
            extend_world[1, col] += extend_world[0, col]
        
        if(extend_world[9, col] != 0): 
            extend_world[8, col] += extend_world[9, col]
    
    return extend_world[1:9 , 1:10]
"""
def main():

    T = np.zeros((72,72,4))
    counter = 0
    for row in range(0,8):
        for col in range(0,9):
            line = transition_model(row, col, action=  "up", tot_row=8, tot_col=9)
            T[counter, : , 0] = line.flatten()
            line = transition_model(row, col, action="left", tot_row=8, tot_col=9)
            T[counter, : , 1] = line.flatten()
            line = transition_model(row, col, action="down", tot_row=8, tot_col=9)
            T[counter, : , 2] = line.flatten()
            line = transition_model(row, col, action="right",tot_row=8, tot_col=9)
            T[counter, : , 3] = line.flatten()

            counter += 1
    print("Saving T in 'T.npy' ...")
    np.save("T_bug01", T)
    print("Done!")
if __name__ == "__main__":
    main()

"""

"""
tot_row = 8
tot_col = 9 

extend_world = np.zeros((tot_row+2, tot_col+2))
print(extend_world[1:9,1:10])
"""
"""
for row in range(0,8):
    for col in range(0,9):
        line = transition_model(row = row , col = col , action = "up", tot_row = 8 , tot_col = 9)
        print(line)
"""
print(transition_model(row = 1 , col= 0 , action= "right", tot_row = 8 , tot_col = 9))
