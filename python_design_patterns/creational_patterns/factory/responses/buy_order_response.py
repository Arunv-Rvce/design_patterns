from creational_patterns.factory.enums.exchange import Exchange
from creational_patterns.factory.enums.order_status import OrderStatus


class BuyOrderResponse:
    def __init__(self, exchange: Exchange, status: OrderStatus, remarks: str) -> None:
        self.exchange: Exchange = exchange
        self.status: OrderStatus = status
        self.remarks: str = remarks
    
    @property
    def exchange(self):
        return self.exchange

    @property
    def _status(self):
        return self.status
    
    @property
    def remarks(self):
        return self.remarks