
from src.main.parser.base import XMLParser
from src.api.models import Price


class PriceParser:

    @staticmethod
    def parse(xml_node):
        currency = XMLParser.get_attr(xml_node, 'currency')
        prices = {}
        for price in xml_node:
            type = XMLParser.get_attr(price, 'type')
            charge_type = XMLParser.get_attr(price, 'ChargeType')
            value = XMLParser.get_text(price)
            prices[type] = prices.get(type, {})
            prices[type][charge_type] = prices[type].get(charge_type, value)

        prices = PriceParser.clean(prices)
        result = []
        for _ in prices:
            result += [Price(currency=currency, **_)]
        return result

    @staticmethod
    def clean(prices):
        from src.api.models import PT_ADULT, PT_CHILD, PT_INFANT
        PRICE_TYPES = {
            'SingleAdult': PT_ADULT,
            'SingleChild': PT_CHILD,
            'SingleInfant': PT_INFANT
        }
        BASE_FIRE_KEY = 'BaseFare'
        TAXES_KEY = 'AirlineTaxes'
        AMOUNT_KEY = 'TotalAmount'

        result = []
        for type, attrs in prices.items():
            settings = dict(
                type=PRICE_TYPES.get(type),
                base_fare=attrs.get(BASE_FIRE_KEY, 0),
                taxes=attrs.get(TAXES_KEY, 0),
                amount=attrs.get(AMOUNT_KEY, 0)
            )
            result += [settings]
        return result
