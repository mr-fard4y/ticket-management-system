
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


API
---

<details>
<summary> Get service version: </summary>

    GET /api/

</details>

<details>
<summary> Get list of itineraries from DXB to BKK on 18-05-18 - template: </summary>

    GET /api/search/DXB180518BKK?sort={price,duration}&order={asc,desc}

</details>

<details>
<summary>Get list of itineraries - optimal choice (sorted by price, duration in ascending order): </summary>

    GET /api/search/DXB180518BKK

</details>

<details>
<summary>Get list of itineraries - cheapest itinerarie (sorted by price in ascending order): </summary>

    GET /api/search/DXB180518BKK?sort=price

</details>

<details>
<summary>Get list of itineraries - the most expensive itinerarie (sorted by price in descending order): </summary>

    GET /api/search/DXB180518BKK?sort=price&order=desc

</details>

<details>
<summary> Get list of itineraries - the shortest itinerarie (sorted by duration in ascending order): </summary>

    GET /api/search/DXB180518BKK?sort=duration

</details>

<details>
<summary>Get list of itineraries - the longest itinerarie (sorted by duration in descending order): </summary>

    GET /api/search/DXB180518BKK?sort=duration&order=desc

</details>


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