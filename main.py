import os

import uvicorn
from fastapi import FastAPI

from fizzbuzz import fizzbuzz_api

app = FastAPI()

app.include_router(fizzbuzz_api.router)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
