# ⚖️ Cross-Exchange Arbitrage Scanner (Crypto)

A Python-based **real-time crypto arbitrage scanner** that monitors price differences between multiple exchanges and detects **potential arbitrage opportunities**.

This project compares **bid–ask spreads** across exchanges to identify moments when buying on one exchange and selling on another could be profitable.

---

## 🚀 What This Project Does

- Connects to multiple crypto exchanges using **CCXT**
- Fetches **live bid and ask prices**
- Compares prices across exchanges
- Identifies **cross-exchange arbitrage spreads**
- Calculates potential **profit percentage**
- Runs continuously with rate-limit safety

---

## 🔍 Exchanges Supported

- **Binance**
- **Kraken**

*(Easily extendable to any CCXT-supported exchange)*

---

## 🧠 Arbitrage Logic

Two arbitrage paths are evaluated:

### 🔹 Opportunity 1
Buy on Binance (ask)
Sell on Kraken (bid)

### 🔹 Opportunity 2
Buy on Kraken (ask)
Sell on Binance (bid)

If the sell price is higher than the buy price, an arbitrage opportunity is flagged.

---

## 🧮 Spread Calculation

Profit % = (Sell Price - Buy Price) / Buy Price × 100


Only **positive spreads** are reported.

---

## 🛠️ Tech Stack

- **Python 3.8+**
- **CCXT**
- **Time-based polling**

---

## 📦 Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/PranavVetkar/Arbitrage-Opportunity-Scanner.git
cd Arbitrage-Opportunity-Scanner
