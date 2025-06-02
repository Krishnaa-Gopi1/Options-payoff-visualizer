import numpy as np
from plot import plot_payoff_curve
from payoff import long_call_payoff,long_put_payoff,bull_call_spread_payoff

choice = int(input("choose an option strategy\n1. long call\n2. long put \n3. bull call spread\n : "))


stock_prices = np.arange(50,151,1)


if choice == 1:
    strike_price = float(input("Enter the strike price: "))
    premium = float(input("Enter the premium: "))
    payoff = long_call_payoff(stock_prices, strike_price, premium)
    title = "Long Call Option Payoff"

elif choice == 2:
    strike_price = float(input("Enter the strike price: "))
    premium = float(input("Enter the premium: "))
    payoff = long_put_payoff(stock_prices, strike_price, premium)
    title = "Long Put Option Payoff"

elif choice == 3:
    lower_strike = float(input("Enter the LOWER strike price: "))
    lower_premium = float(input("Enter the premium PAID for the LOWER strike call: "))
    upper_strike = float(input("Enter the UPPER strike price: "))
    upper_premium = float(input("Enter the premium RECEIVED for the UPPER strike call: "))

    payoff = bull_call_spread_payoff(stock_prices, lower_strike, lower_premium, upper_strike, upper_premium)
    title = "Bull Call Spread Payoff"

else:
    print("Invalid choice")
    exit()


plot_payoff_curve(stock_prices,payoff,title)