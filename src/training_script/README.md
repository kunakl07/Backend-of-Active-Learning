The directory contains necessary commands for model building and training, predicting and plotting the ROC curve.
model_build_and_training.py: Code for building the model and training
The directory structure should be as follows:
```
CLASSPATH
├── train_srkw
│   ├── calls
│   └── no_calls
└── val_srkw
    ├── calls
    └── no_calls
```
The command to run the training and model building script.
```
python model_build_and_training.py --classpath Path to the training directory --noofepochs No of epochs
```

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

The command runs fine and thanks [Diego](https://github.com/jd-rs) for testing it out on your computer!


model_predict.py: Would predict the call if present
```
CLASSPATH
├── test_srkw
│   ├── calls
│   └── no_calls
```
The command to run the predict script is:
```
python model_predict.py --modelpath Path to the model --testpath Path to the test directory
```

statistics.py : Would plot the ROC curve

The command to plot the ROC curve is:
```
python statistics.py --modelpath Path to the model --testpath Path to the test directory
```
