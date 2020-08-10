The command to build docker image
```
sudo docker build -t 'training_script' .
```
The command to run dockerfile
```
sudo docker run -ti training_script --classpath [PATH TO THE TRAINING DIRECTORY] --noofepochs [NO OF EPOCHS]
```

1. classpath: The path to the spectrogram images
2. noofepochs: The number of epochs for which the model is to be trained

[Here, is the link to the training dataset that could be used for training](https://drive.google.com/drive/folders/1tINM2C8d5c9dIOqNpMWZdobC2UZes-XZ?usp=sharing)
