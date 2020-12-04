FROM python
COPY requirements.txt .

RUN pip install -r requirements.txt

RUN mkdir /app
RUN mkdir /app/pipeline
RUN mkdir /app/docker


COPY docker /app/docker
COPY pipeline /app/pipeline
COPY app.py app/app.py


WORKDIR /app

#CMD ["python","pipeline/model/model.py"]
CMD ["python","app.py"]