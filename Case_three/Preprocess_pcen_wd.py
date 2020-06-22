import pandas as pd
from ketos.data_handling import selection_table as sl
import ketos.data_handling.database_interface as dbi
from ketos.data_handling.parsing import load_audio_representation
from ketos.audio.spectrogram import MagSpectrogram
from ketos.data_handling.parsing import load_audio_representation
import numpy as np
from os import listdir
from os.path import isfile, join
from scipy import signal
import soundfile as sf
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from pydub import AudioSegment
import librosa
import os

#Generate mean and annot-train
def duration_mean(filename):
    annot_train = pd.read_csv(filename, sep='\t')
    mean=annot_train['duration_s'].mean()
    return annot_train,mean
  
#Function to add the end time
def add_end(filename):
    filename["end"]=filename["start"]+filename["duration_s"]

#Function to find extract filename and start time
def fname_stime(filename):
    file_name=filename.iloc[:,0].values
    start_time=filename.iloc[:,1].values
    return file_name,start_time

#Function to extract audio from the .wav files to generate complete positive and negative calls
def extract_audio(label,filename,path,position):
    file_name=filename.iloc[:,0].values
    start_time=filename.iloc[:,position].values
    i=0
    o=0
    for x in file_name:
  
        AUDIO_FILE=x
        sound = AudioSegment.from_file(AUDIO_FILE)
        p=start_time[i]
        p=p*1000
        print(p)
        i=i+1
        o=p+2000
        call=sound[p:o]
        call.export(path+label+ "MMMcalls{0}.wav".format(i),format="wav")


def apply_per_channel_energy_norm(data, sampling_rate):
    '''Compute Per-Channel Energy Normalization (PCEN)'''
    S = librosa.feature.melspectrogram(
        data, sr=sampling_rate, power=1)  # Compute mel-scaled spectrogram
    # Convert an amplitude spectrogram to dB-scaled spectrogram
    log_S = librosa.amplitude_to_db(S, ref=np.max)
    pcen_S = librosa.core.pcen(S)
    return pcen_S


def wavelet_denoising(data):
    '''
    Wavelet Denoising using scikit-image
    NOTE: Wavelet denoising is an effective method for SNR improvement in environments with
              wide range of noise types competing for the same subspace.
    '''
    sigma_est = estimate_sigma(data, multichannel=False, average_sigmas=True)
    im_bayes = denoise_wavelet(data, multichannel=False, convert2ycbcr=False, method='BayesShrink',
                               mode='soft')
    im_visushrink = denoise_wavelet(data, multichannel=False, convert2ycbcr=False, method='VisuShrink',
                                    mode='soft')

    # VisuShrink is designed to eliminate noise with high probability, but this
    # results in a visually over-smooth appearance. Here, we specify a reduction
    # in the threshold by factors of 2 and 4.
    im_visushrink2 = denoise_wavelet(data, multichannel=False, convert2ycbcr=False, method='VisuShrink',
                                     mode='soft', sigma=sigma_est / 2)
    im_visushrink4 = denoise_wavelet(data, multichannel=False, convert2ycbcr=False, method='VisuShrink',
                                     mode='soft', sigma=sigma_est / 4)
    return im_bayes


def plot_and_save(denoised_data, f_name):

    fig, ax = plt.subplots()

    i = 0
    # Add this line to show plots else ignore warnings
    # plt.ion()

    ax.imshow(denoised_data)
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    fig.set_size_inches(10, 10)
    fig.savefig(
        f"{f_name[:-4]}" + "_{:04d}.png".format(i),
        dpi=80,
        bbox_inches="tight",
        quality=95,
        pad_inches=0.0)

    fig.canvas.draw()
    fig.canvas.flush_events()
    i += 1
    plt.close(fig)



def final_plot(base_path,plot_path,folder_path):

    basePath = base_path
    plotPath = join(basePath,plot_path)
    folderpath = join(basePath, folder_path)
    onlyfiles = [f for f in listdir(folderpath) if isfile(join(join(folderpath, f)))]

    for idx,file in enumerate(onlyfiles):
        #data, samplerate = sf.read(join(folderpath, file))
   
        data, sr = librosa.core.load(
                    os.path.join(folderpath, file), res_type='kaiser_best')
        #print(data)
        #print(sf)
        f_name = os.path.basename(file)
        pcen_S = apply_per_channel_energy_norm(data, sr)

        denoised_data = wavelet_denoising(pcen_S)
        plot_and_save(denoised_data, f_name)



basePath = r"/home/kunal/Documents/Orcasound_gsoc/Round2_OS_07_05/wav"
plotPath = join(basePath,"train/calls")
folderpath = join(basePath, "wav/pod_calls")
onlyfiles = [f for f in listdir(folderpath) if isfile(join(join(folderpath, f)))]

for idx,file in enumerate(onlyfiles):
   
    data, sr = librosa.core.load(
                    os.path.join(folderpath, file), res_type='kaiser_best')
    
    f_name = os.path.basename(file)
    pcen_S = apply_per_channel_energy_norm(data, sr)

    denoised_data = wavelet_denoising(pcen_S)
    plot_and_save(denoised_data, f_name)


