import numpy as np

def long_call_payoff(stock_prices,strike_price,premium):
    return np.maximum(0,np.array(stock_prices)-strike_price)-premium
