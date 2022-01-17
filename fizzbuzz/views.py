from typing import List

import httpx

import settings

from .models import FizzBuzz as FizzBuzzModel


async def list_fizzbuzz(url: str) -> List[FizzBuzzModel]:
    # I choose httpx instead of aiohttp because with this library we can call both sync and async
    async with httpx.AsyncClient() as client:
        result = (await client.get(url)).json()
    return [FizzBuzzModel.query_result_to_fizzbuzz_model(item) for item in result[: settings.NUMBER_OF_ITEMS]]


async def get_fizzbuzz(url: str) -> FizzBuzzModel:
    async with httpx.AsyncClient() as client:
        result = (await client.get(url)).json()
    return FizzBuzzModel.query_result_to_fizzbuzz_model(result)
