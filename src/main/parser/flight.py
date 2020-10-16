
from src.main.parser.base import XMLParser
from src.main.utils import str2date
from src.api.models import Flight


class FlightParser:

    DATE_FORMAT = "%Y-%m-%dT%H%M"

    @staticmethod
    def parse(xml_node):
        if xml_node is None:
            return []

        result = []
        for flight in XMLParser.get_node(xml_node, 'Flights'):
            carier_node = XMLParser.get_node(flight, 'Carrier')
            carier_name = XMLParser.get_text(carier_node)
            carier_id = XMLParser.get_attr(carier_node, 'id')

            flight_number = XMLParser.get_text(XMLParser.get_node(flight, 'FlightNumber'))
            source = XMLParser.get_text(XMLParser.get_node(flight, 'Source'))
            destination = XMLParser.get_text(XMLParser.get_node(flight, 'Destination'))
            departure_time = XMLParser.get_text(XMLParser.get_node(flight, 'DepartureTimeStamp'))
            arrival_time = XMLParser.get_text(XMLParser.get_node(flight, 'ArrivalTimeStamp'))
            _class = XMLParser.get_text(XMLParser.get_node(flight, 'ArrivalTimeStamp'))
            ticket_type = XMLParser.get_text(XMLParser.get_node(flight, 'TicketType'))

            result += [Flight(
                carier=carier_name,
                number=flight_number,
                source=source,
                destination=destination,
                departure_time=str2date(departure_time, FlightParser.DATE_FORMAT),
                arrival_time=str2date(arrival_time, FlightParser.DATE_FORMAT),
                _class=_class,
                ticket_type=ticket_type
            )]
        return result
