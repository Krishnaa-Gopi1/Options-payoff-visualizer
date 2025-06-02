import numpy as np

def long_call_payoff(stock_prices,strike_price,premium):
    return np.maximum(0,np.array(stock_prices)-strike_price)-premium

def long_put_payoff(stock_prices,strike_price,premium):
    return np.maximum(0,strike_price-np.array(stock_prices))-premium

def bull_call_spread_payoff(stock_prices,lower_strike,lower_premium,upper_strike,upper_premium):
    long_call = np.maximum(0,stock_prices-lower_strike)
    short_call = np.maximum(0,stock_prices-upper_strike)

    return((long_call-short_call) - (lower_premium-upper_premium))

