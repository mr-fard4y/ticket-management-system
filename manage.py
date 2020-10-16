
import os
from flask_script import Manager, Shell, Server
from src.server import create_app


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
    pass


@manager.command
def init_state():
    pass



manager.add_command('runserver', Server())
manager.add_command('shell', Shell(make_context=make_shell_context))


if __name__ == '__main__':
    manager.run()
