
from src.api import bp_api
from flask import jsonify, current_app


@bp_api.route('/', methods=['GET'])
@bp_api.route('/echo', methods=['GET'])
def index():
    return jsonify(
        {'version': current_app.config['VERSION']}
    )
