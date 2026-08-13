import uuid

def test_create_user(
    client,
):
    email = f"{uuid.uuid4()}@test.com"

    response = client.post(
        "/api/v1/users",
        json={
            "name": "John",
            "email": email,
            "age": 25,
            "password": "password123",
        },
    )

    assert response.status_code == 201

    data = response.json()

    assert data["name"] == "John"
    assert data["email"] == email