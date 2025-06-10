import numpy as np
from plot import plot_payoff_curve
from strategies import long_call_payoff,long_put_payoff,bull_call_spread_payoff,bear_put_spread_payoff,long_straddle_payoff,long_strangle_payoff,iron_condor_payoff,protective_put_payoff

choice = int(input("choose an option strategy\n1. long call\n2. long put \n3. bull call spread\n4. bear put spread payoff\n5. Long straddle\n6. Long Strangle \n7.Iron condor \n8. Protective put \n : "))


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

elif choice == 7:
    
    lowest_put_strike = float(input("Enter the lowest put strike (long put): "))
    lowest_put_premium = float(input("Enter the premium for the long put: "))

    lower_put_strike = float(input("Enter the lower put strike (short put): "))
    lower_put_premium = float(input("Enter the premium for the short put: "))

    higher_call_strike = float(input("Enter the higher call strike (short call): "))
    higher_call_premium = float(input("Enter the premium for the short call: "))

    highest_call_strike = float(input("Enter the highest call strike (long call): "))
    highest_call_premium = float(input("Enter the premium for the long call: "))

    stock_prices = np.arange(lowest_put_strike - 20, highest_call_strike + 20, 1)
    payoff = iron_condor_payoff(
    stock_prices,
    lowest_put_strike, lowest_put_premium,
    lower_put_strike, lower_put_premium,
    higher_call_strike, higher_call_premium,
    highest_call_strike, highest_call_premium
    )

    title = "Iron condor payoff"

elif choice == 8:
    stock_purchase_price = float(input("Enter the stock purchase price : "))
    strike_price = float(input("Enter the strike price : "))
    premium = float(input("Enter the premium : "))

    payoff = protective_put_payoff(stock_prices,stock_purchase_price,strike_price,premium)
    title = "Protective put payoff"

else:
    print("Invalid choice")
    exit()


plot_payoff_curve(stock_prices,payoff,title)