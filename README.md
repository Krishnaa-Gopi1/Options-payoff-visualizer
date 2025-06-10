## 📈 Options Payoff Visualizer

A Python mini-project to visualize profit/loss (payoff) at expiry for common **options trading strategies**.\
Designed for beginners in finance and options, with clear code and interactive inputs.

---

### 🚀 Features

- Visualize 8 popular options strategies
- Interactive CLI interface
- Matplotlib-based plots
- Modular, beginner-friendly Python structure

---

### 🧐 What is an Options Payoff?

In options trading, a **payoff** shows your profit or loss at expiry depending on where the stock price ends up.\
This tool lets you experiment with strike prices, premiums, and see how each strategy behaves visually.

---

### 📊 Strategies Included

| # | Strategy             | Description                                                                              |
| - | -------------------- | ---------------------------------------------------------------------------------------- |
| 1 | **Long Call**        | Buy a call option to profit from rising prices. Loss is limited to premium paid.         |
| 2 | **Long Put**         | Buy a put option to profit from falling prices. Loss limited to premium.                 |
| 3 | **Bull Call Spread** | Buy a lower strike call, sell a higher one. Limited risk, limited reward.                |
| 4 | **Bear Put Spread**  | Buy a higher strike put, sell a lower one. Used when expecting a drop.                   |
| 5 | **Long Straddle**    | Buy both a call and put at the same strike. Profits from big moves either way.           |
| 6 | **Long Strangle**    | Similar to a straddle, but with out-of-the-money options. Cheaper but needs bigger move. |
| 7 | **Iron Condor**      | Sell a put spread and call spread. Profits if stock stays in a range.                    |
| 8 | **Protective Put**   | Own the stock + buy a put as insurance. Limits downside risk.                            |

---

### 🧰 Tech Stack

- Python 3.x
- [NumPy](https://numpy.org/)
- [Matplotlib](https://matplotlib.org/)

---

### 📦 Setup

```bash
git clone https://github.com/your-username/options-payoff-visualizer.git
cd options-payoff-visualizer
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

---

### ✅ To-Do / Future Ideas

- Add breakeven annotations on plots
- GUI using Tkinter or Streamlit
- Export results to PDF/image
- Include Greeks (Delta, Theta, etc.)

