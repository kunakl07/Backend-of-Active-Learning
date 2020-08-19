# Backend-of-Active-Learning
These Repository contains the necessary code for the Backend of Active Learning


# Backend-of-Active-Learning
These Repository contains the necessary code for the Backend of Active Learning

The directory structure of our project looks like this: 

```
├── experiments
│   ├── experiments/Grayscale_magspectrogram_scipy.ipynb
│   ├── experiments/Grayscale_specs_mag.ipynb
│   ├── experiments/Preprocess_grayscale.ipynb
│   ├── experiments/README.md
│   ├── experiments/Sir_Val's_method_color.ipynb
│   └── experiments/Spectrograms.ipynb
├── images
│   ├── images/active_final.png
│   ├── images/activelearning_general_stage.png
│   ├── images/CNN_final_vs_random.png
│   ├── images/General_flow.png
│   ├── images/grayscale_psd.png
│   ├── images/greyscale(2).png
│   ├── images/melscale.png
│   ├── images/noPre.png
│   ├── images/onlyPCEN.png
│   ├── images/pcen_melspectrogram.png
│   ├── images/preprocess2.png
│   ├── images/pre_train.png
│   ├── images/psd_color_scipy.png
│   ├── images/ROC_correct.png
│   └── images/wavelet_denoising_mel.png
├── notebooks
│   ├── notebooks/active_learning
│   │   └── notebooks/active_learning/active_learning_pipeline.ipynb
│   ├── notebooks/case_one
│   │   ├── notebooks/case_one/Preprocessing
│   │   │   └── notebooks/case_one/Preprocessing/preprocess_case_one.ipynb
│   │   ├── notebooks/case_one/README.md
│   │   └── notebooks/case_one/Training
│   │       ├── notebooks/case_one/Training/case_one_cnn.py
│   │       ├── notebooks/case_one/Training/case_one_vgg.py
│   │       ├── notebooks/case_one/Training/README.md
│   │       ├── notebooks/case_one/Training/results.py
│   │       └── notebooks/case_one/Training/training_on_case_one_on_model_VGG_and_CNN.ipynb
│   ├── notebooks/case_three
│   │   ├── notebooks/case_three/Preprocess
│   │   │   ├── notebooks/case_three/Preprocess/preprocessing_PCEN_and_Wavlet_denoising.ipynb
│   │   │   └── notebooks/case_three/Preprocess/README.md
│   │   ├── notebooks/case_three/README.md
│   │   └── notebooks/case_three/Training
│   │       ├── notebooks/case_three/Training/cnn_case_three_no_valid.py
│   │       ├── notebooks/case_three/Training/CNN_for_SRKW.ipynb
│   │       ├── notebooks/case_three/Training/README.md
│   │       ├── notebooks/case_three/Training/Resnet152_pre_pcen_wd_train.ipynb
│   │       ├── notebooks/case_three/Training/results.py
│   │       └── notebooks/case_three/Training/Training.ipynb
│   ├── notebooks/case_two
│   │   ├── notebooks/case_two/Preprocess
│   │   │   └── notebooks/case_two/Preprocess/preprocessing_using_PCEN.ipynb
│   │   └── notebooks/case_two/Training
│   │       └── notebooks/case_two/Training/training_on_PCEN_spectrograms.ipynb
│   ├── notebooks/preprocessing_and_training_using_Ketos
│   │   ├── notebooks/preprocessing_and_training_using_Ketos/Preprocessing
│   │   │   ├── notebooks/preprocessing_and_training_using_Ketos/Preprocessing/preprocessing_using_Ketos.ipynb
│   │   │   └── notebooks/preprocessing_and_training_using_Ketos/Preprocessing/README.md
│   │   └── notebooks/preprocessing_and_training_using_Ketos/Training
│   │       ├── notebooks/preprocessing_and_training_using_Ketos/Training/training_on_RNN_using_Ketos.ipynb
│   │       ├── notebooks/preprocessing_and_training_using_Ketos/Training/Training_SRKWs_Ketos.ipynb
│   │       └── notebooks/preprocessing_and_training_using_Ketos/Training/Train_K.py
│   └── notebooks/README.md
├── requirements.txt
├── src
│   ├── src/preprocessing_script
│   │   ├── src/preprocessing_script/Dockerfile
│   │   ├── src/preprocessing_script/preprocess.py
│   │   ├── src/preprocessing_script/README.md
│   │   ├── src/preprocessing_script/requirements.txt
│   │   └── src/preprocessing_script/selection_table.py
│   └── src/training_script
│       ├── src/training_script/Dockerfile
│       ├── src/training_script/model_build_and_training.py
│       ├── src/training_script/README.md
│       └── src/training_script/requirements.txt
├── trained_models
│   └── trained_models/README.md
└── unpolished_colab_notebooks
    ├── unpolished_colab_notebooks/Grayscale_magspectrogram_scipy.ipynb
    ├── unpolished_colab_notebooks/Grayscale_specs_mag.ipynb
    ├── unpolished_colab_notebooks/Preprocess_grayscale.ipynb
    ├── unpolished_colab_notebooks/README.md
    └── unpolished_colab_notebooks/Sir_Val's_method_color.ipynb


```
