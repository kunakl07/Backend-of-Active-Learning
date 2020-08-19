FROM python:3.6

WORKDIR /usr/src/app

COPY preprocess.py .
COPY selection_table.py .
COPY requirements.txt .

RUN apt-get update && apt-get install -y \
ffmpeg libavcodec-extra
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN apt-get update &&  apt-get install -y \
libsndfile1-dev
RUN pip install pysndfile
ENTRYPOINT ["python3","./preprocess.py"]





