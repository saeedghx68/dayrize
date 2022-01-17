from typing import List

import httpx
from fastapi import APIRouter, Depends, HTTPException

import settings

from .models import FizzBuzz as FizzBuzzModel
from .views import get_fizzbuzz as get_fizzbuzz_view, list_fizzbuzz as list_fizzbuzz_view

# APIRouter creates path operations for item module
router = APIRouter(
    prefix="/fizzbuzz",
    tags=["fizzbuzz"],
    responses={404: {"description": "Not found"}},
)


@router.get(
    "/list",
    status_code=200,
    response_model=List[FizzBuzzModel],
)
async def get_list():
    url = settings.LIST_EDNPOINT
    return await list_fizzbuzz_view(url)


@router.get(
    "/{fizzbuzz_id}",
    status_code=200,
    response_model=FizzBuzzModel,
)
async def get_fizzbuzz(fizzbuzz_id: int):
    url = settings.GET_EDNPOINT.format(fizzbuzz_id=fizzbuzz_id)
    return await get_fizzbuzz_view(url)

