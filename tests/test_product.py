import pytest

from app.product.schemas import Product


def test_create_product(client):
    response = client.post("/products", json={
        "name": "iphone 12",
        "category": "phones",
        "quantity": 100
    })
    assert response.status_code == 201
    assert 'id' in response.json()
    pytest.product = Product(**response.json())


def test_get_all_products(client):
    response = client.get("/products")
    assert isinstance(response.json(), list)


def test_delete_product(client):
    response = client.delete(f"/products/{pytest.product.id}")
    assert response.json() == {"detail": "product deleted"}
