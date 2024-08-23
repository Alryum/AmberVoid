FROM python:3.12
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV APP_HOME=/code
WORKDIR $APP_HOME
COPY backend/requirements.txt $APP_HOME/

RUN pip install --upgrade pip && pip install -r requirements.txt
COPY . .
