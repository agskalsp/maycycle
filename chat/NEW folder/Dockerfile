FROM python:3.7-alpine

WORKDIR /app

COPY requirements.txt requirements.txt

RUN apk update && \
    apk add --no-cache gcc musl-dev && \
    pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

#RUN export FLASK_APP=app.py
#RUN python3 -m flask run
#RUN python3 -m pytest test.py

#CMD ["python", "app.py"]

EXPOSE 5005
ENV FLASK_APP=app.py
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]

#RUN pip install --no-cache-dir -r requirements.txt
#CMD ["flask","run","--host=0.0.0.0"]
