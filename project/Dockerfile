FROM python:3.7.4

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN /usr/local/bin/python -m pip install --upgrade pip

#RUN pip3 install https://storage.googleapis.com/tensorflow/windows/cpu/tensorflow_cpu-2.4.0-cp37-cp37m-win_amd64.whl

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_APP=app.py

CMD flask run --host=0.0.0.0