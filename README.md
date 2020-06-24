# Backend-of-Active-Learning
These Repository contains the necessary code for the Backend of Active Learning

The three cases contains three different ways in which data is preprocessed and passed to different models for performing predictions.
Below is the flowchart that explains each of the case and the models used for training in each cases

# General flow 


<p align = "center">
<img src = Images/General_flow.png>
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
  
