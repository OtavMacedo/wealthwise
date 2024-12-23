from http import HTTPStatus


def test_hello_world(client):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Hello World'}


def test_create_user(client):
    response = client.post(
        '/users', json={'username': 'otavio', 'email': 'otavmacedo04@gmail.com', 'password': '1234'}
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {'username': 'otavio', 'email': 'otavmacedo04@gmail.com'}


def test_read_users(client):
    response = client.get('/users')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'users': [{'username': 'otavio', 'email': 'otavmacedo04@gmail.com'}]}
