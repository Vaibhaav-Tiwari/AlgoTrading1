import matplotlib.pyplot as plt
import numpy as np


def vasicek_model(r0, kappa, theta, sigma, T=1, N=1000):
    dt = T/float(N)
    t = np.linspace(0, T, N+1)
    rates = [r0]
    for _ in range(N):
        dr = kappa*(theta-rates[-1])*dt + sigma*np.sqrt(dt)*np.random.normal()
        rates.append(rates[-1]+dr)


    return t, rates

def plot_model(t, r):
    plt.plot(t, r)
    plt.xlabel('Time(t)')
    plt.ylabel('Interest rate r(t)')
    plt.title('Vasicek Model')
    plt.show()


if __name__=='__main__':
    time, data = vasicek_model(1.3, 0.9, 1.5, 0.5)
    plot_model(time, data)
