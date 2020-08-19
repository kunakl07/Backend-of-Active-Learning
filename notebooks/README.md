
The three cases are explained below in brief:

The three cases contains three different ways in which data is preprocessed and passed to different models for performing predictions.
Below is the flowchart that explains each of the case and the models used for training in each cases

# General flow 


<p align = "center">
<img src = 
     /images/General_flow.png>
</p>

## The three cases are:
 - Preprocessing without applying PCEN and Wavelet-Denoising
 - Preprocessing using PCEN
 - Preprocessing using PCEN and Wavelet-Denoising

### The different models that are used in the above cases are:
1. Preprocessing without PCEN and Wavelet Denosing  
    1. Basic Convolution Neural Network
    2. VGG-16
  
2. Preprocessing with PCEN 
    1. VGG-16
  
3. Preprocessing with PCEN and Wavelet Denoising
    1. Resnet-512
    2. VGG-16
    3. Basic CNN 
    4. InceptionResnet-V2

#### Note: Although, in the directory structure we have preprocessing and training using Ketos we are not going to use this phase for active learning, but we are going to use the three cases for the active learning.
# Active Learning Phase
This is the active learning phase that would be used to evaluate the outcome of the active learning on the model where a small subset would be extracted and the model would perform probability predictions on these subset, which depending on the probability would be passed to the labeler or directly to the model.


# Active Learning flow 


<p align = "center">
<img src = /images/active_final.png>
</p>

I have worked on this active learning pipeline where I have taken the following steps:

1. Preprocess the spectrograms.
2. Create a CNN model and train the training data(Podcast Round 2 and Round 3) on the CNN model.
3. Calculate the Probability predictions for each of the samples present in the test data.
4. If the model predicts the probability of the sample (being either call or no-call) in the range of 0.4 to 0.6, the model is uncertain and pass
    these calls to the labeler to label them.
5. But, if the value of the predicted sample is greater than 0.6 assign it no call, and if the value is less then 0.4 assign the sample call.
6. Retrain the model on the combined data(samples labeled by the model as well as the user).

## The ROC curve

<p align = "center">
<img src = /images/CNN_final_vs_random.png>
</p>

The CNN model of the case three generates the following ROC curve.
