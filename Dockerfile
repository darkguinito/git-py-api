FROM python:3


RUN adduser --disabled-password --gecos '' api
RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install -y libgit2-dev



WORKDIR /usr/src/app


COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
USER api

COPY --chown=api . .
EXPOSE 5000
CMD [ "python", "./main.py" ]
# RUN go get ./...
