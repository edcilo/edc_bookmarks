from fixture import app, client


def test_api_index(client):
    response = client.get("/api/v1/")
    assert response.status_code == 200
    assert response.content_type == "application/json"
    assert "app_name" in response.json
    assert "version" in response.json
