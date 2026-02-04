import ccxt
import time

class ArbScanner:
    def __init__(self):
        # We initialize two different exchanges
        self.binance = ccxt.binance()
        self.kraken = ccxt.kraken()
        self.symbol = 'BTC/USDT'

    def fetch_prices(self):
        # Fetch tickers simultaneously
        b_ticker = self.binance.fetch_ticker(self.symbol)
        k_ticker = self.kraken.fetch_ticker(self.symbol)
        
        # We use 'ask' for buying and 'bid' for selling
        prices = {
            'binance_buy': b_ticker['ask'],
            'binance_sell': b_ticker['bid'],
            'kraken_buy': k_ticker['ask'],
            'kraken_sell': k_ticker['bid']
        }
        return prices

    def scan(self):
        print(f"--- Scanning for {self.symbol} Arbitrage ---")
        while True:
            try:
                p = self.fetch_prices()
                
                # Opportunity 1: Buy Binance -> Sell Kraken
                diff1 = p['kraken_sell'] - p['binance_buy']
                # Opportunity 2: Buy Kraken -> Sell Binance
                diff2 = p['binance_sell'] - p['kraken_buy']
                
                if diff1 > 0:
                    profit_pct = (diff1 / p['binance_buy']) * 100
                    print(f"💰 [OPPORTUNITY] Buy Binance (${p['binance_buy']}) -> Sell Kraken (${p['kraken_sell']}) | Spread: {profit_pct:.4f}%")
                
                elif diff2 > 0:
                    profit_pct = (diff2 / p['kraken_buy']) * 100
                    print(f"💰 [OPPORTUNITY] Buy Kraken (${p['kraken_buy']}) -> Sell Binance (${p['binance_sell']}) | Spread: {profit_pct:.4f}%")
                
                else:
                    print("... No spread found (Markets are efficient)")

                time.sleep(2) # Don't spam the APIs
            except Exception as e:
                print(f"Error: {e}")
                break

if __name__ == "__main__":
    scanner = ArbScanner()
    scanner.scan()