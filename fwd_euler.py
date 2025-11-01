import numpy as np
import matplotlib.pyplot as plt



def f_dynamics(tk, xk, xdotk):
    """SMD dynamics"""
    m = 1
    
    k = 1
    b = 0.1
    
    F = 0
    
    return (1/m) * ( -k*xk - b*xdotk + F )


def forward_euler():
    
    # initial conditions
    xk = 1
    xdotk = 0
    
    # time
    dt = 0.001
    tf = 10
    t_data = np.arange(0, tf, dt)
    
    # data
    k = 0
    x_data = np.zeros_like(t_data)
    xdot_data = np.zeros_like(t_data)
    
    for tk in t_data:
        
        xddotk = f_dynamics(tk, xk, xdotk)
        
        xdotk1 = xdotk + dt * xddotk

        xk1 = xk + dt * xdotk
        
        xk = xk1
        xdotk = xdotk1
        

        # add data for plotting
        x_data[k] = xk
        xdot_data[k] = xdotk
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
    
        
        






if _kame__ == "__main__":
    forward_euler()


