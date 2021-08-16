FROM python:3.7.5-slim
COPY ./requirements.txt /requirements.txt
WORKDIR /
EXPOSE 8888
COPY . /
RUN pip install -r requirements.txt
ENTRYPOINT [ "python" ]
CMD [ "main.py" ]
