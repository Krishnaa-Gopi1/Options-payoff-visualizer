import matplotlib.pyplot as plt


def plot_payoff_curve(stock_prices,payoffs,title):
    plt.plot(stock_prices,payoffs,label="payoff")
    plt.xlabel('Stock Price at Expiry')
    plt.ylabel('Profit / Loss')
    plt.title(title)
    plt.grid(True)
    plt.legend()
    plt.show()

