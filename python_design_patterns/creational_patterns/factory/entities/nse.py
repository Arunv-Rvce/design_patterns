from creational_patterns.factory.entities.stock_exchange import StockExchange
from creational_patterns.factory.enums.exchange import Exchange
from creational_patterns.factory.responses.buy_order_response import BuyOrderResponse


class NSE(StockExchange):
    def get_exchange() -> Exchange:
        return Exchange.NSE

    def place_buy_order() -> BuyOrderResponse:
        """
        """
