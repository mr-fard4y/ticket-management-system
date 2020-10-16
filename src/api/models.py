

from mongoengine.document import Document, EmbeddedDocument
from mongoengine.fields import StringField, IntField, DateTimeField,\
    EmbeddedDocumentField, ListField, FloatField
from mongoengine.queryset import queryset_manager
from src.main.utils import humanize_date


PT_ADULT = 'A'
PT_CHILD = 'C'
PT_INFANT = 'I'

PRICE_TYPES = (
    (PT_ADULT, 'Adult'),
    (PT_CHILD, 'Child'),
    (PT_INFANT, 'Infant')
)


class Price(EmbeddedDocument):
    meta = {
        'strict': False,
        'auto_create_index': False
    }

    type = StringField(choices=PRICE_TYPES)
    amount = FloatField(default=0)
    base_fare = FloatField(default=0)
    taxes = FloatField(default=0)
    currency = StringField(required=True)

    def __str__(self):
        return '{}: {} {}'.format(self.type, self.amount, self.currency)

    @property
    def json_data(self):
        return {
            'type': self.type,
            'amount': self.amount,
            'base_fare': self.base_fare,
            'taxes': self.taxes
        }

    def to_json(self):
        return self.json_data


class Flight(EmbeddedDocument):
    meta = {
        'strict': False,
        'auto_create_index': False
    }

    carier = StringField()
    number = IntField()
    source = StringField()
    destination = StringField()
    departure_time = DateTimeField()
    arrival_time = DateTimeField()
    _class = StringField()
    ticket_type = StringField()

    def __str__(self):
        return '{}-{} {}-{}'.format(self.carier, self.number,
                                    self.source, self.destination)

    @property
    def json_data(self):
        return {
            'carier': self.carier,
            'number': self.number,
            'source': self.source,
            'destination': self.destination,
            'departure_time': self.departure_time,
            'arrival_time': self.arrival_time,
            'class': self._class,
            'ticket_type': self.ticket_type,
        }

    def to_json(self):
        return self.json_data


class Itinerarie(Document):
    meta = {
        'collection': 'flights.itinerarie',
        'strict': False,
        'auto_create_index': False,
        'indexes': [
            '_duration',
            'default_price',
            ('source', 'destination', 'departure_time')]
    }

    source = StringField(required=True)
    destination = StringField(required=True)
    departure_time = DateTimeField(required=True)
    arrival_time = DateTimeField(required=True)
    _duration = IntField()
    default_price = FloatField()
    flights = ListField(EmbeddedDocumentField(Flight))
    prices = ListField(EmbeddedDocumentField(Price))

    @queryset_manager
    def objects(cls, queryset):
        return queryset.order_by('default_price', '_duration')

    def __str__(self):
        return 'From {} to {} {} by {}'.format(
            self.source, self.destination, self.duration, self.default_price)

    def clean(self):
        self._duration = (self.arrival_time - self.departure_time).total_seconds()
        price_for_adult = next(filter(lambda x: x.type == PT_ADULT, self.prices))
        self.default_price = price_for_adult.amount if price_for_adult else 0

    @property
    def duration(self):
        return humanize_date(self._duration)

    @property
    def json_data(self):
        return {
            'source': self.source,
            'destination': self.destination,
            'departure_time': self.departure_time,
            'arrival_time': self.arrival_time,
            'duration': self.duration,
            'flights': [_.to_json() for _ in self.flights],
            'prices': [_.to_json() for _ in self.prices],
            'price': self.default_price
        }

    def to_json(self):
        return self.json_data
