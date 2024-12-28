FROM python:3.13-alpine

# Disable pip cache and poetry venvs
ENV PIP_NO_CACHE_DIR=false

WORKDIR /iotd-bot

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY ./secrets ./bot.py ./main.py ./

CMD [ "python3", "main.py" ]
