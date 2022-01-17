from typing import Dict, List, Optional

from pydantic import BaseModel, create_model


class FizzBuzz(BaseModel):
    number: int
    fizzbuzz_api: Optional[str] = None
    placeholder_post: create_model("Placeholer", title=(str, ...), body=(str, ...))

    # TODO:this function can go to logic.py file
    @classmethod
    def get_fizzbuzz(cls, value: int) -> Optional[str]:
        """
        run fizzbuzz algorithm
        if number is a multiple of three, it returns “Fizz”, for multiples of five it returns “Buzz”.
        For numbers which are multiples of both three and five it returns “FizzBuzz”.
        For numbers which satisfy neither of these, it returns None
        """
        if not value:
            return None

        multiple_of_three = bool(not (value % 3))
        multiple_of_five = bool(not (value % 5))

        if multiple_of_three and multiple_of_five:
            return "FizzBuzz"
        elif multiple_of_three:
            return "Fizz"
        elif multiple_of_five:
            return "Buzz"

    @classmethod
    def query_result_to_fizzbuzz_model(cls, item: dict) -> List["FizzBuzz"]:
        return FizzBuzz(
            number=item["id"],
            fizzbuzz_api=cls.get_fizzbuzz(item["id"]),
            placeholder_post=dict(
                title=item.get("title", ""),
                body=item.get("body", ""),
            ),
        )
