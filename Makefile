REQ_FILE=requirements.txt

.PHONY: install
install:
	sudo apt install python3.9 python3.9-dev
	python3.9 -m venv venv
	./venv/bin/pip install -r $(REQ_FILE)

.PHONY: req
req:
	pip install -r $(REQ_FILE)

.PHONY: black
black:
	black src
	black tests

.PHONY: isort
isort:
	isort src
	isort tests

.PHONY: run
run:
	./venv/bin/python main.py

.PHONY: test
test:
	pytest tests

.PHONY: docker-build
docker-build:
	docker build . -t dayrize:latest

.PHONY: docker-run
docker-run:
	docker run -d -p 8000:8000 --name dayrize dayrize:latest python main.py

.PHONY: docker-test
docker-test:
	docker run -it --name dayrize dayrize:latest pytest
