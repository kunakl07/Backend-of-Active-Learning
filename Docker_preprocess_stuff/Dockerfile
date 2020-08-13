FROM python:3.6

WORKDIR /usr/src/app

COPY preprocess.py .
COPY selection_table.py .
COPY requirements.txt .
COPY test_extract_audio.tsv .
COPY 1562337136_0004.wav .
RUN apt-get update && apt-get install -y \
ffmpeg libavcodec-extra
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN apt-get update &&  apt-get install -y \
libsndfile1-dev
RUN pip install pysndfile
ENTRYPOINT ["python3","./preprocess.py"]





