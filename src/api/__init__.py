

from flask import Blueprint


bp_api = Blueprint('api', __name__)

from src.api import routes
