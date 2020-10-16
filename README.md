
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
    make run
```
OR
```bash
    docker-compose build && docker-compose up
```

and open [http://localhost:8000](http://localhost:8000/api/search/dxb180518bkk)


Support
-------

If you have found some issues, please let me know.
* Fe-Nik-S <mikifeynman@gmail.com>