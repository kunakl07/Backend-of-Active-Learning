FROM python:3.6

WORKDIR /usr/src/app

COPY model_build_and_training.py .
COPY requirements.txt .
COPY content .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENTRYPOINT ["python3","./model_build_and_training.py"]





