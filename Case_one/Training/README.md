## The training section consists of Jupyter Notebook and three python scripts
- Jupyter Notebook contains sequence of steps that were taken to train the model

## The three python scripts are command line executable scripts 
###  case_one_cnn: This python script is used to train our model on the spectrogram images of the audio data. 

```
python case_one_cnn.py --classpath --noofepochs
```
1. classpath: The path to the spectrogram images
2. noofepochs: The number of epochs for which the model is to be trained

### case_one_vgg: This python script is used to train our fine-tuned vgg-16 model on the spectrogram images of the audio data. 

```
python case_one_vgg.py --classpath --noofepochs
```
1. classpath: The path to the spectrogram images
2. noofepochs: The number of epochs for which the model is to be trained

### results:This python plots the ROC graph, the precision recall graph and the accuracy matrix
```
python case_one_vgg.py --modelpath --testpath
```
1. modelpath: The path to the model.h5 file
2. testpath: The path to the test directory

