
import pytest
from src.server import create_app


TEST_ROUTE_PARAMS = [
    ('/unknown_path', '', 404),

    ('/api/', '', 200),
    ('/api/echo', '', 200),

    ('/search/dxb180518bkk', '', 200),

    ('/search/dxb180518bkk', 'sort=price', 200),
    ('/search/dxb180518bkk', 'sort=price&order=ASC', 200),

    ('/search/dxb180518bkk', 'sort=duration', 200),
    ('/search/dxb180518bkk', 'sort=duration&order=DESC', 200)
]


@pytest.fixture
def client():
    app = create_app('test')
    app.testing = True
    return app.test_client()


@pytest.mark.parametrize("route, params, expected_status", TEST_ROUTE_PARAMS)
def test_api(client, route, params, expected_status):
    status_code = client.get(route +'?%s' % (params or '')).status_code
    assert expected_status == status_code
