import numpy as np 

def return_state_utility(v, T, u, reward, gamma):
    action_array = np.zeros(4)
    for action in range(0,4):
       action_array[action] = np.sum(np.multiply(u, np.dot(v, T[:,:,action])))  
    return reward + gamma*np.max(action_array)    

u = np.zeros(72)
u1 = np.zeros(72)
T = np.load("T_bug01.npy")
r =np.array([-0.04, -0.04, +1.00, -1.00, -0.04, -0.04, -0.04, -0.04, -0.04,   
             -0.04,  0.00,  0.00,  0.00,  0.00,  0.00,  0.00,  0.00, -0.04, 
             -0.04,  0.00, -0.04, -0.04, -0.04, -0.04, -0.04,  0.00, -0.04, 
             -0.04,  0.00, -0.04, -0.04, -0.04, -0.04, -0.04,  0.00, -0.04, 
             -0.04,  0.00,  0.00,  0.00, -0.04, -0.04, -0.04,  0.00, -0.04, 
             -0.04, -0.04, -0.04, -0.04, -0.04, -0.04, -0.04,  0.00, -0.04, 
             -0.04, -0.04,  0.00,  0.00,  0.00,  0.00,  0.00,  0.00, -0.04,
             -0.04, -0.04, -0.04, -0.04, -0.04, -0.04, -0.04, -0.04, -0.04])

tot_states = 72
gamma = 0.999 #Discount factor
iteration = 0 #Iteration counter
epsilon = 0.01 #Stopping criteria small value

#List containing the data for each iteation
graph_list = list()

while iteration < 100:
        delta = 0
        u = u1.copy()
        
        graph_list.append(u)
        for s in range(72):
            reward = r[s]
            v = np.zeros((1,tot_states))
            v[0,s] = 1.0
            u1[s] = return_state_utility(v, T, u, reward, gamma)
            delta = max(delta, np.abs(u1[s] - u[s])) #Stopping criteria       
        #if delta < epsilon * (1 - gamma) / gamma:
        print("=================== FINAL RESULT ==================")
        print("Iterations: " + str(iteration))
        print("Delta: " + str(delta))
        print("Gamma: " + str(gamma))
        print("Epsilon: " + str(epsilon))
        print("===================================================")
        print(u[0:9])
        print(u[9:18])
        print(u[18:27])
        print(u[27:36])
        print(u[36:45])
        print(u[45:54])
        print(u[54:63])
        print(u[63:72])

        print(u)
        print("===================================================")
                #break
        iteration += 1