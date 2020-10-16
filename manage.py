
import os
from flask_script import Manager, Shell, Server
from src.server import create_app
from termcolor import colored


app = create_app(os.getenv('APP_STAGE') or 'dev')
manager = Manager(app)


def make_shell_context():
    return dict(app=app)


@manager.command
def run_tests():
    """Run the unit tests."""
    import unittest

    path_to_tests = os.path.join(
        os.getcwd(), "tests"
    )
    tests = unittest.TestLoader().discover(path_to_tests)
    unittest.TextTestRunner(verbosity=2).run(tests)


@manager.command
def clear_db():
    from src.api.models import Itinerarie
    Itinerarie.objects.delete()
    print(colored('DB was successfully cleared.', 'green'))


@manager.command
def init_state():
    current_dir = os.getcwd()
    FLIGHTS_DATA = [
        os.path.join(current_dir, "src", "data", file_name) for file_name in [
            'RS_ViaOW.xml', 'RS_Via-3.xml']
    ]
    clear_db()
    for path_to_data in FLIGHTS_DATA:
        import_data(path_to_data)


@manager.command
def import_data(path_to_file):
    from src.main.parser.base import XMLParser
    from src.main.parser.itinerarie import ItinerarieParser

    with open(path_to_file) as f:
        xml_root = XMLParser.get_root(f)
        items = ItinerarieParser.parse(xml_root)
        for _ in items:
            _.save()

    print(colored('The file {} was successfully parsed.'.format(path_to_file), 'green'))


manager.add_command('runserver', Server())
manager.add_command('shell', Shell(make_context=make_shell_context))


if __name__ == '__main__':
    manager.run()
