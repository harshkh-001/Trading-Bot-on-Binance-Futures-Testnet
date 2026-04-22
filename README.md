# Binance Demo Futures Trading Bot

## Overview
A CLI-based Python trading bot that places MARKET and LIMIT orders using Binance Demo Futures API.

## Setup

1. Clone repo
2. Install dependencies:
   pip install -r requirements.txt

3. Create .env file:
   cp .env.example .env

4. Add your API keys from Binance Demo

## Usage

### Market Order
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

### Limit Order
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 60000

## Features
- MARKET & LIMIT orders
- BUY/SELL support
- CLI interface
- Logging to file
- Input validation
- Error handling

## Logs
Check logs/trading.log

## Note
Using Binance Demo Futures API: (Getting 403 Forbidden error)
https://demo-fapi.binance.com

using testnet giving None in all fields 
As on testnet.binancefuture.com it redirects to binancefuture.com So cannot create api on testnet

On binancefuture.com need addhar verification to create api
