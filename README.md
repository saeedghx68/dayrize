Dayrize test
=============
A simple app with python3.9 to run fizzbuzz algorithm with fastapi.

I hope that understood the challenge correctly. please reveiw the code.
About the test coverage , I just wrote *A FEW of them*. it is not fully covered, *THAT IT SHOULD BE*.
If you think that I should do that, please let me know and I will do so as well.

Due deliver you the task soon, I didn't separate the test packages and development packages from the requirements.txt and also seperate docker file, but I'm aware of that, if you think I should separate it please let me know

install python3.9
------------
```
make install
```

install requirements
-----------
```
make req
```

------------

## Test and Build

to run the app
```
make run
```

Run unit tests and integration tests
```
make test
```

run the app via docker
```
make docker-build
make docker-run
```

run tests via docker
```
make docker-test
```

-----------
## black and sort

to run black:
```
make black
```

run isort
```
make isort
```

-----------

# To run tests:
`pytest`

# Documantation
please see the docs [here](http://127.0.0.1:8000/docs) and [here](http://127.0.0.1:8000/redoc)

# Endpoints
* An endpoint that responds with a list of the first 10 fizzbuzz entities (i.e. number 1-10): `http://127.0.0.1:8000/fizzbuzz/list`
* An endpoint that includes a number parameter in the url path, e.g. fizzbuzz/15 and responds with the relevant fizzbuzz entity: `http://127.0.0.1:8000/fizzbuzz/15`


