from math import exp as e


def future_discrete_value(x, r, n):
    return x*(1+r)**n


def present_discrete_value(x, r, n):
    return x*(1+r)**-n

def future_continuous_value(x, r, t):
    return x*e(r*t)


def present_continuous_value(x, r, t):
    return x*e(-r*t)

if __name__=='__main__':
    #value of investment in dollars
    x=100
    #define interest rate (r)
    r=0.05
    #duration (years)
    n=5

    print("future value (discrete model) of x: %s" % future_discrete_value(x,r,n))
    print("present value (discrete model) of x: %s" % present_discrete_value(x,r,n))
    print("future value (continuous model) of x: %s" % future_continuous_value(x,r,n))
    print("present value (continuous model) of x: %s" % present_continuous_value(x,r,n))

