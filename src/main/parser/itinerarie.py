
from src.main.parser.base import XMLParser
from src.main.parser.price import PriceParser
from src.main.parser.flight import FlightParser
from src.api.models import Itinerarie


class ItinerarieParser:

    FLIGHTS_NODES = [
        'OnwardPricedItinerary',
        'ReturnPricedItinerary'
    ]

    @staticmethod
    def get_settings(flights):
        source_flight = flights[0]
        dest_flight = flights[-1]

        return dict(
            source=source_flight.source,
            destination=dest_flight.destination,
            departure_time=source_flight.departure_time,
            arrival_time=dest_flight.arrival_time
        )

    @staticmethod
    def parse(xml_node):
        result = []

        for itinerarie in XMLParser.get_node(xml_node, 'PricedItineraries'):
            prices = XMLParser.get_node(itinerarie, 'Pricing')
            prices = PriceParser.parse(prices)

            for node_key in ItinerarieParser.FLIGHTS_NODES:
                flights = XMLParser.get_node(itinerarie, node_key)
                flights = FlightParser.parse(flights)

                if not flights:
                    continue

                settings = ItinerarieParser.get_settings(flights)
                result += [Itinerarie(prices=prices, flights=flights, **settings)]
        return result
