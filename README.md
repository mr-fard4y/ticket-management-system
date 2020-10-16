
Simple Web API

=========

Local installation
------------
Install project from git repository, by running:

```bash
    git clone https://github.com/Fe-Nik-S/ticket-management-system
    cd ticket-management-system
    make init_all || pipenv install
```
  Pipenv must be installed or just follow the on-screen instructions


Usage
-----
For running service:

```bash
    make run_docker
```
OR
```bash
    docker-compose build && docker-compose up
```

and open [http://localhost:8000](http://localhost:8000/api/search/dxb180518bkk)


ToDo
----------

Several improvements and fixes for the future:

- Linters and code analyzing, static validation
- Cover by functional and unit tests
- Dockerization. Separate configs (nginx, unicorn, etc) to files
- etc


Support
-------

If you find some issues, please let me know.
* Fe-Nik-S <mikifeynman@gmail.com>