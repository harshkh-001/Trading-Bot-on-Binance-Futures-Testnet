import argparse
from bot.orders import place_order
from bot.validators import validate_order
from bot.logging_config import setup_logger

def main():
    setup_logger()

    parser = argparse.ArgumentParser(description="Binance Demo Futures Trading Bot")

    parser.add_argument("--symbol", required=True, help="e.g., BTCUSDT")
    parser.add_argument("--side", required=True, help="BUY or SELL")
    parser.add_argument("--type", required=True, help="MARKET or LIMIT")
    parser.add_argument("--quantity", required=True, help="Order quantity")
    parser.add_argument("--price", help="Required for LIMIT orders")

    args = parser.parse_args()

    try:
        validate_order(
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price
        )

        print("\n📌 Order Summary")
        print(f"Symbol   : {args.symbol}")
        print(f"Side     : {args.side}")
        print(f"Type     : {args.type}")
        print(f"Quantity : {args.quantity}")
        print(f"Price    : {args.price}\n")

        order = place_order(
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price
        )

        print("✅ SUCCESS")
        print(f"Order ID     : {order.get('orderId', 'N/A')}")
        print(f"Status       : {order.get('status', 'N/A')}")
        print(f"Executed Qty : {order.get('executedQty', 'N/A')}")

        avg_price = order.get('avgPrice') or order.get('price') or "N/A"
        print(f"Avg Price    : {avg_price}")

    except Exception as e:
        print("\n❌ ERROR:", str(e))


if __name__ == "__main__":
    main()