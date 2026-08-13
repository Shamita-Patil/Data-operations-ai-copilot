
def test_root(
    client,
):
    response = client.get("/")

    assert response.status_code == 200


def test_get_users(
    client,
):
    response = client.get(
        "/api/v1/users"
    )

    assert response.status_code == 401


def test_login_invalid_credentials(
    client,
):
    response = client.post(
        "/api/v1/login",
        data={
            "username": "fake@email.com",
            "password": "wrongpassword",
        },
    )

    assert response.status_code == 401

def test_invalid_route(
    client,
):
    response = client.get(
        "/does-not-exist"
    )

    assert response.status_code == 404