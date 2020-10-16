

from flask import Blueprint


bp_main = Blueprint('main', __name__)


from src.main import handlers
