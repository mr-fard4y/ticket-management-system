# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------
#
# ---------------------------------------------------------------------
# Copyright (C) 2019-Present
# See LICENSE for details
# ---------------------------------------------------------------------

import os
from flask_script import Manager, Shell, Server
from src.server import create_app


app = create_app(os.getenv('APP_STAGE') or 'dev')
manager = Manager(app)


def make_shell_context():
    return dict(app=app)


manager.add_command('runserver', Server())
manager.add_command('shell', Shell(make_context=make_shell_context))


if __name__ == '__main__':
    manager.run()
