from scipy import stats
from numpy import log, exp, sqrt

def call_option_price(S, E, T, rf, sigma):
    # first we calculate d1 and d2 parameters
    d1 = (log(S/E)+(rf+sigma*sigma/2)*T)/(sigma*sqrt(T))
    d2 = d1 - sigma*sqrt(T)
    print ("the d1 and d2 parameters: %s, %s" % (d1, d2))
    # use the N(x) to calculate the price of the option
    return S*stats.norm.cdf(d1) - E*exp(-rf*T)*stats.norm.cdf(d2)


def put_option_price(S, E, T, rf, sigma):
    # first we calculate d1 and d2 parameters
    d1 = (log(S/E)+(rf+sigma*sigma/2)*T)/(sigma*sqrt(T))
    d2 = d1 - sigma*sqrt(T)
    print ("the d1 and d2 parameters: %s, %s" % (d1, d2))
    # use the N(x) to calculate the price of the option
    return -S*stats.norm.cdf(-d1) + E*exp(-rf*T)*stats.norm.cdf(-d2)

if __name__ == '__main__':
    # underlying stock price at t=0
    S0 = 100
    # strike price
    E = 100
    # expiry 1year=365 days
    T = 1
    # risk-free rate
    rf=0.05
    #volatility of the underlying stock
    sigma=0.2


    print ("Call option price according to the Black-Scholes model",
           call_option_price(S0, E, T, rf, sigma))

    print ("Put option price according to the Black-Scholes model",
           put_option_price(S0, E, T, rf, sigma))