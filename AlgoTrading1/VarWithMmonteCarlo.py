import numpy as np
import yfinance as yf
import datetime
import pandas as pd


def download_data(stock, start, end):
    data = {}
    ticker = yf.download(stock, start, end)
    data['Adj Close'] = ticker['Adj Close']
    return pd.DataFrame(data)

class ValueAtRiskMonteCarlo:

    def __init__(self, S, mu, sigma, c, n, iterations):
        # this is the value of our investment at t=0 (1000 dollars)
        self.S=S
        self.mu=mu
        self.sigma=sigma
        self.c=c
        self.n=n
        self.iterations=iterations

    def simulation(self):
        rand = np.random.normal(0, 1, [1, self.iterations])

        # equation for the S(t) stock price
        # the random walk of our intial investment
        stock_price=self.S * np.exp(self.n * (self.mu - 0.5*self.sigma**2) +
        self.sigma*np.sqrt(self.n)*rand)

        #we have to sort the stock prices to determine the percentile
        stock_price=np.sort(stock_price)



        # it depends on the stock prices to determine the percentile
        percentile = np.percentile(stock_price, (1 - self.c)*100)

        return self.S - percentile


if __name__=='__main__':

    S = 1e6 #investment
    c=0.95
    n=1
    iterations=100000

    #historical data to approximate the mean and standard deviation
    start_date = datetime.datetime(2014, 1, 1)
    end_date = datetime.datetime(2017, 10, 15)

    #download stock related data from yahoo fin
    citi=download_data('C', start_date, end_date)

    # we can use the pct_change() to calculate daily returns
    citi['returns'] = citi['Adj Close'].pct_change()

    mu = np.mean(citi['returns'])
    sigma=np.std(citi['returns'])

    model = ValueAtRiskMonteCarlo(S, mu, sigma, c,n ,iterations)
    print ('value at risk with monte carlo simulation: $%.2f' % model.simulation())
