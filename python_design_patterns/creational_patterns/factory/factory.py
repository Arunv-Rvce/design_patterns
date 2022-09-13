
from creational_patterns.factory.entities.bse import BSE
from creational_patterns.factory.entities.nse import NSE
from creational_patterns.factory.enums.exchange import Exchange


def stock_exchange_factory(exchange: Exchange):
    if Exchange.BSE.__eq___(exchange):
        return BSE()
    elif Exchange.NSE.__eq__(exchange):
        return NSE()
    raise ValueError(f"Invalid Exchange Type {exchange}")