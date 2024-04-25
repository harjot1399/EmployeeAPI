FROM python:3.11-slim-buster

RUN apt-get update && apt-get upgrade -y

COPY apiAssignment/requirements.txt .

RUN pip install -r requirements.txt

COPY ./apiAssignment /app

WORKDIR /app

COPY entrypoint.sh /entrypoint.sh

# Give execute permission to the entrypoint script and run it
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]


