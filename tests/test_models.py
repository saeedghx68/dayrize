import pytest
from fizzbuzz.models import FizzBuzz


@pytest.mark.parametrize(
    ["item", "output"],
    [
        [
            {"id": 1, "title": "foo", "body": "bar"},
            {
                "number": 1,
                "fizzbuzz_api": None,
                "placeholder_post": {
                    "title": "foo",
                    "body": "bar",
                },
            },
        ],
        [
            {"id": 3, "title": "foo", "body": "bar"},
            {
                "number": 3,
                "fizzbuzz_api": "Fizz",
                "placeholder_post": {
                    "title": "foo",
                    "body": "bar",
                },
            },
        ],
        [
            {"id": 5, "title": "foo", "body": "bar"},
            {
                "number": 5,
                "fizzbuzz_api": "Buzz",
                "placeholder_post": {
                    "title": "foo",
                    "body": "bar",
                },
            },
        ],
        [
            {"id": 15, "title": "foo", "body": "bar"},
            {
                "number": 15,
                "fizzbuzz_api": "FizzBuzz",
                "placeholder_post": {
                    "title": "foo",
                    "body": "bar",
                },
            },
        ],
    ],
)
def test_query_result_to_fizzbuzz_model(item, output):
    assert FizzBuzz.query_result_to_fizzbuzz_model(item).dict() == output


@pytest.mark.parametrize(
    ["item", "output"],
    [
        [0, None],
        [1, None],
        [3, "Fizz"],
        [4, None],
        [5, "Buzz"],
        [15, "FizzBuzz"],
    ],
)
def test_get_fizzbuzz(item, output):
    assert FizzBuzz.get_fizzbuzz(item) == output
