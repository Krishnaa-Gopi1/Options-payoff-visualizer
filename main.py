import numpy as np
from plot import plot_payoff_curve
from payoff import long_call_payoff,long_put_payoff,bull_call_spread_payoff,bear_put_spread_payoff,long_straddle_payoff,long_strangle_payoff

choice = int(input("choose an option strategy\n1. long call\n2. long put \n3. bull call spread\n4. bear put spread payoff\n5. Long straddle\n6. Long Strangle \n: "))


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

elif choice == 4:
    lower_strike = float(input("Enter the LOWER strike price: "))
    lower_premium = float(input("Enter the premium PAID for the LOWER strike call: "))
    upper_strike = float(input("Enter the UPPER strike price: "))
    upper_premium = float(input("Enter the premium RECEIVED for the UPPER strike call: "))

    payoff = bear_put_spread_payoff(stock_prices, lower_strike, lower_premium, upper_strike, upper_premium)
    title = "Bear put Spread Payoff"

elif choice == 5:
    strike_price = float(input("Enter the strike price: "))
    call_premium = float(input("Enter the call premium: "))
    put_premium = float(input("Enter the put premium: "))
    

    payoff = long_straddle_payoff(stock_prices,strike_price,call_premium,put_premium)
    title = "Long straddle payoff"

elif choice == 6:
   
    lower_strike = float(input("Enter the LOWER strike price: "))
    lower_premium = float(input("Enter the premium PAID for the LOWER strike call: "))
    upper_strike = float(input("Enter the UPPER strike price: "))
    upper_premium = float(input("Enter the premium RECEIVED for the UPPER strike call: "))

    payoff = long_strangle_payoff(stock_prices,lower_strike,lower_premium,upper_strike,upper_premium)
    title = "Long strangle payoff"

else:
    print("Invalid choice")
    exit()


plot_payoff_curve(stock_prices,payoff,title)