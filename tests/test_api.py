from settings import NUMBER_OF_ITEMS
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_list_output():
    response = client.get("/fizzbuzz/list")
    assert response.status_code == 200
    result = response.json()
    assert len(result) == NUMBER_OF_ITEMS
    assert all(key in ("number", "fizzbuzz_api", "placeholder_post") for key in result[0].keys())

def test_get_output():
    response = client.get("/fizzbuzz/1")
    assert response.status_code == 200
    result = response.json()
    assert result["number"] == 1
    assert not result["fizzbuzz_api"]


    response = client.get("/fizzbuzz/3")
    assert response.status_code == 200
    result = response.json()
    assert result["number"] == 3
    assert result["fizzbuzz_api"] == "Fizz"

    response = client.get("/fizzbuzz/5")
    assert response.status_code == 200
    result = response.json()
    assert result["number"] == 5
    assert result["fizzbuzz_api"] == "Buzz"

    response = client.get("/fizzbuzz/15")
    assert response.status_code == 200
    result = response.json()
    assert result["number"] == 15
    assert result["fizzbuzz_api"] == "FizzBuzz"




    
