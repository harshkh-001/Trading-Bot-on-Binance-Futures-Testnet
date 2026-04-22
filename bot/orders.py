import logging
from bot.client import get_client

def place_order(symbol, side, order_type, quantity, price=None):
    client = get_client()

    try:
        logging.info(f"REQUEST -> {symbol} {side} {order_type} qty={quantity} price={price}")

        if order_type == "MARKET":
            order = client.futures_create_order(
                symbol=symbol.upper(),
                side=side,
                type="MARKET",
                quantity=quantity
            )

        elif order_type == "LIMIT":
            order = client.futures_create_order(
                symbol=symbol.upper(),
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

        logging.info(f"RESPONSE -> {order}")
        return order

    except Exception as e:
        logging.error(f"ERROR -> {str(e)}")
        raise RuntimeError(f"Order failed: {str(e)}")