import numpy as np
import matplotlib.pyplot as plt



def f_dynamics(t, x_n, xdot_n):
    """SMD dynamics"""
    m = 1
    
    k = 1
    b = 0.1
    
    F = 0
    
    return (1/m) * ( -k*x_n - b*xdot_n + F )


def forward_euler():
    
    # initial conditions
    x_n = 1
    xdot_n = 0
    
    # time
    dt = 0.001
    tf = 10
    t_data = np.arange(0, tf, dt)
    
    # data
    k = 0
    x_data = np.zeros_like(t_data)
    xdot_data = np.zeros_like(t_data)
    
    for t in t_data:
        
        xddot_n = f_dynamics(t, x_n, xdot_n)
        
        xdot_n1 = xdot_n + dt * xddot_n

        x_n1 = x_n + dt * xdot_n
        
        x_n = x_n1
        xdot_n = xdot_n1
        

        # add data for plotting
        x_data[k] = x_n
        xdot_data[k] = xdot_n
        k += 1
        

    plot(t_data, x_data, xdot_data)
        

def plot(t_data, x_data, xdot_data):
    
    plt.figure(figsize=(10, 9))
    
    plt.subplot(2, 1, 1)
    plt.plot(t_data, x_data)
    plt.xlabel("t")
    plt.ylabel("x")
    plt.grid()
    
    plt.subplot(2, 1, 2)
    plt.plot(t_data, xdot_data)
    plt.xlabel("t")
    plt.ylabel("xdot")
    plt.grid()
    
    plt.suptitle("fwd euler integration")
    plt.savefig("plots/fwd_euler.pdf")
    plt.close()
    
        
        






if __name__ == "__main__":
    forward_euler()


