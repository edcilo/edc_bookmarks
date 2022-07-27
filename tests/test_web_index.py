from fixture import app, client


def test_index(client):
    response = client.get("/")
    assert response.status_code == 200
    assert 'text/html' in response.content_type
    assert response.data.decode('ascii') == "hello from flask"
