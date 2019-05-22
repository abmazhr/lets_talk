FROM python:3.7.3-alpine3.9

LABEL name="Abdulrahman" email="abmazhr@gmail.com"

RUN pip3 install --upgrade pip

ENV APP_PATH /usr/src/
RUN mkdir -p $APP_PATH
WORKDIR $APP_PATH
ADD requirements/prod-requirements.txt $APP_PATH

RUN pip3 install -r prod-requirements.txt

COPY src $APP_PATH

EXPOSE 3000

ENTRYPOINT ["sh", "-c", "python3.7 $APP_PATH/main.py"]