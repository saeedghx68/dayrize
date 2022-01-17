REQ_FILE=requirements.txt
VERSION=3.9.10


.PHONY: setup-pyenv
setup-pyenv:
	git clone https://github.com/pyenv/pyenv.git ~/.pyenv
	./.pyenv/bin/pyenv install $(VERSION)

.PHONY: install
install:
	~/.pyenv/versions/$(VERSION)/bin/python$(version) -m venv venv
	./venv/bin/pip install -r $(REQ_FILE)

.PHONY: black
black:
	./venv/bin/black src
	./venv/bin/black tests

.PHONY: isort
isort:
	./venv/bin/isort src
	./venv/bin/isort tests

.PHONY: run
run:
	./venv/bin/python main.py

.PHONY: test
test:
	./venv/bin/pytest tests

.PHONY: docker-build
docker-build:
	docker build . -t dayrize-api:latest

.PHONY: docker-run
docker-run:
	docker run -d -p 8000:8000 --name dayrize-api dayrize-api:latest python main.py

.PHONY: docker-test
docker-test:
	docker run -it --name dayrize-api dayrize-api:latest pytest
