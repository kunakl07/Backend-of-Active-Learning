FROM python:3.6

WORKDIR /usr/src/app

COPY J_corrected_preprocess.py .
COPY requirements.txt .
COPY test_extract_audio.tsv .
COPY input_file .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN apt-get update &&  apt-get install -y \
libsndfile1-dev
RUN pip install pysndfile
ENTRYPOINT ["python3","./J_corrected_preprocess.py"]





