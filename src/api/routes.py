
from src.api import bp_api
from flask import jsonify, current_app
from src.api.models import Itinerarie
from src.main.utils import str2date
from src.api.decorators import prettify_args


@bp_api.route('/', methods=['GET'])
@bp_api.route('/echo', methods=['GET'])
def index():
    return jsonify(
        {'version': current_app.config['VERSION']}
    )


@bp_api.route('/search/<regex("[a-zA-Z]{3}"):src><regex("[0-9]{6}"):date><regex("[a-zA-Z]{3}"):dst>', methods=['GET'])
@prettify_args([('src', str.upper), ('dst', str.upper), ('date', str2date)])
def search(src, dst, date, sort_key, sort_order, *args, **kwargs):
    query = Itinerarie.objects.filter(
        source=src, destination=dst, departure_time__gte=date)

    if sort_key:
        replacements = {
            'price': 'default_price',
            'duration': '_duration'
        }
        sort_key = replacements.get(sort_key, sort_key)
        if sort_order and sort_order.lower() == 'desc':
            sort_key = '-{}'.format(sort_key)
        query = query.order_by(sort_key)

    result = {
        'result': [_.to_json() for _ in query]
    }
    return jsonify(result)
