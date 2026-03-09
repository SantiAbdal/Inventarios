def test_create_category(client):
    response = client.post("/categories/", json={"name": "Electrónica"})
    assert response.status_code == 201
    assert response.json()["name"] == "Electrónica"


def test_create_duplicate_category(client):
    client.post("/categories/", json={"name": "Electrónica"})
    response = client.post("/categories/", json={"name": "Electrónica"})
    assert response.status_code == 400


def test_get_category_not_found(client):
    response = client.get("/categories/999")
    assert response.status_code == 404


def test_delete_category(client):
    response = client.post("/categories/", json={"name": "Electrónica"})
    category_id = response.json()["id"]

    response = client.delete(f"/categories/{category_id}")
    assert response.status_code == 200