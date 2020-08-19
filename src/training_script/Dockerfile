FROM python:3.8.5

WORKDIR /usr/src/app

COPY model_build_and_training.py .
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENTRYPOINT ["python3","./model_build_and_training.py"]





