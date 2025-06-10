import numpy as np

def long_call_payoff(stock_prices,strike_price,premium):
    return np.maximum(0,np.array(stock_prices)-strike_price)-premium

def long_put_payoff(stock_prices,strike_price,premium):
    return np.maximum(0,strike_price-np.array(stock_prices))-premium

def bull_call_spread_payoff(stock_prices,lower_strike,lower_premium,upper_strike,upper_premium):
    long_call = np.maximum(0,stock_prices-lower_strike)
    short_call = np.maximum(0,stock_prices-upper_strike)

    return((long_call-short_call) - (lower_premium-upper_premium))

def bear_put_spread_payoff(stock_prices,lower_strike,lower_premium,upper_strike,upper_premium):
    long_put = np.maximum(0,upper_strike-stock_prices)
    short_put = np.maximum(0,lower_strike-stock_prices)

    return((long_put-short_put)-(upper_premium-lower_premium))
    

def long_straddle_payoff(stock_prices,strike_price,call_premium,put_premium):
    call = np.maximum(0,stock_prices-strike_price)
    put = np.maximum(0,strike_price-stock_prices)

    return call+put - (call_premium+put_premium)

def long_strangle_payoff(stock_prices,lower_strike,lower_premium,upper_strike,upper_premium):
    call = np.maximum(0,stock_prices-upper_strike)
    put = np.maximum(0,lower_strike-stock_prices)
    
    return call+put -(upper_premium+lower_premium)

def iron_condor_payoff(
    stock_prices,
    lowest_put_strike, lowest_put_premium,
    lower_put_strike, lower_put_premium,
    higher_call_strike, higher_call_premium,
    highest_call_strike, highest_call_premium
):
    # Bull Put Spread 
    long_put = np.maximum(0, lowest_put_strike - stock_prices)
    short_put = np.maximum(0, lower_put_strike - stock_prices)
    bull_put = short_put - long_put - (lower_put_premium - lowest_put_premium)

    # Bear Call Spread 
    short_call = np.maximum(0, stock_prices - higher_call_strike)
    long_call = np.maximum(0, stock_prices - highest_call_strike)
    bear_call = short_call - long_call - (higher_call_premium - highest_call_premium)

   
    return bull_put + bear_call

def protective_put_payoff(stock_prices,stock_purchase_price,strike_price,premium):
    return stock_prices - stock_purchase_price + np.maximum(strike_price-stock_prices,0) - premium

    