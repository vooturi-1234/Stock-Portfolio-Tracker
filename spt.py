import yfinance as yf
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

# Portfolio dictionary
portfolio = {}

# Function to add stock
def add_stock(ticker, shares):
    if ticker in portfolio:
        portfolio[ticker] += shares
    else:
        portfolio[ticker] = shares
    print(f"Added {shares} shares of {ticker}.")

# Function to remove stock
def remove_stock(ticker):
    if ticker in portfolio:
        del portfolio[ticker]
        print(f"Removed {ticker} from portfolio.")
    else:
        print(f"{ticker} not in portfolio.")

# Function to fetch real-time stock data
def get_stock_price(ticker):
    stock = yf.Ticker(ticker)
    data = stock.history(period="1d")
    if not data.empty:
        return data['Close'][0]
    else:
        return None

# Function to display portfolio
def view_portfolio():
    if not portfolio:
        print("Portfolio is empty.")
        return

    print("\nYour Portfolio:")
    total_value = 0
    df = pd.DataFrame(columns=["Ticker", "Shares", "Price", "Total Value"])
    
    for ticker, shares in portfolio.items():
        price = get_stock_price(ticker)
        if price is not None:
            value = shares * price
            total_value += value
            df = pd.concat([df, pd.DataFrame([[ticker, shares, round(price, 2), round(value, 2)]], 
                                             columns=df.columns)], ignore_index=True)
        else:
            print(f"Failed to fetch price for {ticker}")
    
    print(df.to_string(index=False))
    print(f"\nTotal Portfolio Value: ${round(total_value, 2)}")

# Sample usage
add_stock("AAPL", 10)
add_stock("MSFT", 5)
view_portfolio()
remove_stock("AAPL")
view_portfolio()