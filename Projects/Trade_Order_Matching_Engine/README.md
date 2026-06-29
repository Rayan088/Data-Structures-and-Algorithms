### Overview

A full stack simulated cryptocurrency trading platform build with a Python Flask backend and React frontend. The system simulates a live BTC/USD exchange with a real time order book, matching engine, market maker bot, and trading dashboard.

---

### Preview

![Dashboard](./frontend/vite-project/src/assets/UI%20-%20SS.png)

---

### Features

- **Real-time Order Book** — Live bids and asks, sorted by price, with depth visualisation bars
- **Matching Engine** — Price-time priority matching with support for partial fills
- **Market Maker Bot** — Automated bot that continuously places buy and sell orders to simulate a live market
- **Time & Sales** — Live feed of executed trades with buy/sell colour coding
- **Order Form** — Place limit orders with percentage-based quantity shortcuts and live total calculation
- **Wallet** — Track available USD and BTC balances, updated on every trade
- **Open Orders** — View all your submitted orders with fill status in real time
- **Live Stats Bar** — Current price, 24h change, high/low, and volume updated every 500 milliseconds

---

### How it Works

1. Orders are added to a heap-based order book — bids as a max-heap (negated price), asks as a min-heap
2. On every new order, `match_orders` runs and compares the best bid and best ask
3. If `best_bid.price >= best_ask.price`, a trade executes at the ask price
4. Quantity matched is `min(buy.remaining, sell.remaining)` — supporting partial fills
5. Filled orders are marked `CLOSED` and removed from the heap
6. The wallet updates in real time on every matched trade

---

## API Endpoints

| Method | Endpoint      | Description                                |
| ------ | ------------- | ------------------------------------------ |
| GET    | `/orderbook`  | Current bids and asks                      |
| GET    | `/trades`     | All executed trades                        |
| GET    | `/market`     | Market summary (price, volume, 24h change) |
| GET    | `/stats`      | Spread and mid price                       |
| GET    | `/wallet`     | User wallet balances                       |
| GET    | `/userorders` | User's submitted orders                    |
| POST   | `/order`      | Place a new order                          |

---

### Tech Stack

**Backend**

- Python 3
- Flask + Flask-CORS
- Custom heap-based order book (`heapq`)
- Multithreaded market maker bot

**Frontend**

- React (Vite)
- CSS Grid layout
- Polling-based live data (2s intervals)

---
