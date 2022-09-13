from abc import ABC, ABCMeta, abstractmethod, abstractproperty

from creational_patterns.factory.enums.exchange import Exchange
from creational_patterns.factory.responses.buy_order_response import BuyOrderResponse


class StockExchange(ABC):
    @abstractproperty
    def get_exchange() -> Exchange:
        pass

    @abstractmethod
    def place_buy_order() -> BuyOrderResponse:
        pass