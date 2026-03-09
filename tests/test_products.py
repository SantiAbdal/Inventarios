def test_create_product(client):
    # Arrange — primero necesitamos una categoría
    category = client.post("/categories/", json={"name": "Electrónica"})
    category_id = category.json()["id"]

    product_data = {
        "name": "Laptop",
        "brand": "Dell",
        "description": "Laptop gamer",
        "price": "1500.00",
        "cost": "1000.00",
        "stock": 10,
        "stock_min": 2,
        "condition": "ACTIVO",
        "start_date": "2024-01-01",
        "sku": "LAP-001",
        "category_id": category_id
    }

    # Act
    response = client.post("/products", json=product_data)

    # Assert
    assert response.status_code == 201
    assert response.json()["name"] == "Laptop"
    assert response.json()["sku"] == "LAP-001"


def test_get_product_not_found(client):
    response = client.get("/products/999")
    assert response.status_code == 404


def test_create_duplicate_sku(client):
    category = client.post("/categories/", json={"name": "Electrónica"})
    category_id = category.json()["id"]

    product_data = {
        "name": "Laptop",
        "brand": "Dell",
        "description": "Laptop gamer",
        "price": "1500.00",
        "cost": "1000.00",
        "stock": 10,
        "stock_min": 2,
        "condition": "ACTIVO",
        "start_date": "2024-01-01",
        "sku": "LAP-001",
        "category_id": category_id
    }

    client.post("/products", json=product_data)
    response = client.post("/products", json=product_data)  # mismo SKU
    assert response.status_code == 400


def test_reduce_stock_insufficient(client):
    category = client.post("/categories/", json={"name": "Electrónica"})
    category_id = category.json()["id"]

    client.post("/products", json={
        "name": "Laptop",
        "brand": "Dell",
        "description": "Laptop gamer",
        "price": "1500.00",
        "cost": "1000.00",
        "stock": 2,
        "stock_min": 1,
        "condition": "ACTIVO",
        "start_date": "2024-01-01",
        "sku": "LAP-001",
        "category_id": category_id
    })

    response = client.post("/stock/out/LAP-001?quantity=10")
    assert response.status_code == 400