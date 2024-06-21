import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# we will simulate 1000 r(t) interest rate processes
NUM_OF_SIMULATIONS=1000
# these are the number of points in a single r(t) proces
NUM_OF_POINTS=200

def monte_carlo_simulation(x, r0, kappa, theta, sigma, T=1):

    dt = T / float(NUM_OF_POINTS)
    result = []

    for _ in range(NUM_OF_SIMULATIONS):
        rates = [r0]
        for _ in range(NUM_OF_POINTS):
            dr = kappa * (theta - rates[-1])*dt + sigma * np.sqrt(dt) * np.random.normal()
            rates.append(rates[-1] + dr)

        result.append(rates)

    simulation_data = pd.DataFrame(result)
    simulation_data=simulation_data.T

    # calculate the integral of the r(t) based on the simulated paths
    integral_sum = simulation_data.sum() * dt
    # present value of a future cash flow
    present_integral_sum = np.exp(-integral_sum)
    # mean because the integral is the average
    bond_price = x * np.mean(present_integral_sum)

    print('bond price based on the monte carlo simulation $%.2f' % bond_price)

    #plt.plot(simulation_data.T)
    #plt.show()
    #print(simulation_data.T)



if __name__=='__main__':

    monte_carlo_simulation(1000, 0.1, 0.3, 0.3, 0.03)



