The directory structure of your new project looks like this: 

```
├── LICENSE
├── Dockerfile
|    ├── preprocessing <- The preprocessing script. 
|    ├── training      <- The model building and training script.
|    └── README.md 
|
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── tsv_files      <- Data from third party sources.
│   └── README.md 
|
├── Case_one
│   ├── Preprocessing <-Jupyter notebook in colab performing preprocessing
│   ├── Training      <- Jupyter notebook in colab performing training
|   └── README.md 
|
├── Case_two
│   ├── Preprocessing <-Jupyter notebook in colab performing preprocessing process using case two
│   ├── Training      <- Jupyter notebook in colab performing training stage on stage two preprocessed spectrograms.
|   └── README.md
|
├── Case_three
│   ├── Preprocessing <-Jupyter notebook in colab performing preprocessing process using case three.
│   ├── Training      <- Jupyter notebook in colab performing training stage on case three preprocessed spectrograms.
|   └── README.md
│
├── Preprocessing and training using Ketos
│   ├── Preprocessing <-Jupyter notebook in colab performing preprocessing using Ketos library.
│   ├── Training      <- Jupyter notebook in colab performing training stage on preprocessed spectrograms.
|   └── README.md
|
├── active_learning
│   └── active_learning_pipeling <-Jupyter notebook in colab performing active learning.
|
├── trained_models   <- Trained and serialized models, model predictions, or model summaries for different preprocessing cases
│
├── references       <- Data dictionaries, manuals, and all other explanatory materials.
│
├── requirements.txt <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── scripts                 <- Source code for use in this project.
│   ├── preprocess_data     <- Scripts to preprocess audio data and generate spectrograms
|   |    ├── selection.py   <- Script to generate background noise
│   │    └── preprocess.py  <- Script to preprocess_data
│   |
│   ├── models              <- Scripts to train models and then use trained models to make
│   │   │                      predictions
│   │   └── train_model.py
│   │  
│   │
│   └── visualization  <- Scripts to create exploratory and results oriented visualizations
│       └── visualize.py
│
└── experiments        <- Different types of spectrograms used and the accuracy we get using each spectrogram

```
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
  
# Active Learning Phase
This is the active learning phase that would be used to evaluate the outcome of the active learning on the model where a small subset would be extracted and the model would perform probability predictions on these subset, which depending on the probability would be passed to the labeler or directly to the model.


# Active Learning flow 


<p align = "center">
<img src = Images/active_final.png>
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
<img src = Images/ROC_correct.png>
</p>

The CNN model of the case three generates the following ROC curve.
