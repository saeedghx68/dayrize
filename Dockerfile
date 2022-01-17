FROM python:3.9

RUN mkdir /code

WORKDIR /code

# copy files
ADD ./fizzbuzz ./fizzbuzz
Add tests  ./tests
Add main.py .
Add requirements.txt .
Add settings.py .

# for using black and isort
Add pyproject.toml

# to install packages
COPY ./requirements.txt /code/requirements.txt
RUN pip install -r requirements.txt

# expose port
EXPOSE 8000

CMD []

