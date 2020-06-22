import os
import matplotlib.pyplot as plt
import soundfile as sf
import pandas as pd
from pydub import AudioSegment
from os import listdir
from os.path import isfile, join
from scipy import signal

from ketos.data_handling import selection_table as sl


# Function to add the end time
def add_end(filename):
    filename["end"] = filename["start"] + filename["duration_s"]


# Generate mean and annot-train
def duration_mean(filename):
    annot_train = pd.read_csv(filename, sep='\t')
    mean = annot_train['duration_s'].mean()
    return annot_train, mean


# Function to find extract filename and start time
def fname_stime(filename):
    file_name = filename.iloc[:, 0].values
    start_time = filename.iloc[:, 1].values
    return file_name, start_time


# Function to extract audio from the .wav files to generate
# complete positive and negative calls
def extract_audio(label, filename, path, position, file_location):
    file_name = filename.iloc[:, 0].values
    start_time = filename.iloc[:, position].values
    i = 0
    o = 0
    os.chdir(file_location)

    for x in file_name:
        AUDIO_FILE = x
        sound = AudioSegment.from_file(AUDIO_FILE)
        p = start_time[i]
        p = p * 1000
        print(p)
        i = i + 1
        o = p + 3000
        call = sound[p:o]
        call.export(path + label + "MMMcalls{0}.wav".format(i), format="wav")


# Plotting the spectrogram
def plot_spectrogram(base, plot, calls):
    basePath = base
    plotPath = join(basePath, plot)
    folderpath = join(basePath, calls)
    onlyfiles = [f for f in listdir(folderpath)
                 if isfile(join(join(folderpath, f)))]
    for idx, file in enumerate(onlyfiles):
        data, samplerate = sf.read(join(folderpath, file))
        f, t, spec = signal.spectrogram(data, samplerate)
        filename = file.split(sep=".")[0]

        fig, ax = plt.subplots(1, 1)
        ax.specgram(data, Fs=samplerate, NFFT=1024)
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
        os.chdir(plotPath)

        plt.savefig(join(plotPath,
                filename + ".png"))
        plt.close(fig)


# Enter the path of the standardized tsv's
annot_train2, mean2 = duration_mean('/content/podcast2.tsv')
annot_train3, mean3 = duration_mean('/content/podcast3.tsv')
annot_test, mean_test = duration_mean('/content/v10_test.tsv')

add_end(annot_train2)
add_end(annot_train3)
add_end(annot_test)
annot_train2.head()

# Extract the audio of the calls
extract_audio(
    "round2_calls", annot_train2,
    "/content/pod_calls/", 1,
    "/content/Round2_OS_07_05/wav/")

extract_audio(
    'round3_calls', annot_train3,
    "/content/pod_calls/", 1,
    "/content/Round3_OS_09_27_2017/wav/")


# Standardizing the tsv files
map_to_ketos_annot_std = {'wav_filename': 'filename'}
std_annot_train2 = sl.standardize(
                       table=annot_train2,
                       signal_labels=["SRKWs"],
                       mapper=map_to_ketos_annot_std,
                       trim_table=True)

std_annot_train3 = sl.standardize(
                       table=annot_train3,
                       signal_labels=["SRKWs"],
                       mapper=map_to_ketos_annot_std,
                       trim_table=True)
std_annot_test = sl.standardize(
                      table=annot_test,
                      signal_labels=["SRKWs"],
                      mapper=map_to_ketos_annot_std,
                      trim_table=True)


'''
Since we also want the negative audio, we would generate
negative sound by extracting it from the background sound
what are not present in  the call duration. For that first
we create a tsv that generates time-interval from the tsv
files that are not within the start-time and end-time
'''
positives_train2 = sl.select(annotations=std_annot_train2, length=3.0)
file_durations_train2 = sl.file_duration_table(
                            '/content/Round2_OS_07_05/wav')
negatives_train2 = sl.create_rndm_backgr_selections(
                    annotations=std_annot_train2,
                    files=file_durations_train2,
                    length=3.0,
                    num=len(positives_train2),
                    trim_table=True)


# Same steps for podcast3 tsv file
positives_train3 = sl.select(annotations=std_annot_train3, length=3.0)
file_durations_train33 = sl.file_duration_table(
                              '/content/Round3_OS_09_27_2017/wav')
negatives_train33 = sl.create_rndm_backgr_selections(
                    annotations=std_annot_train3,
                    files=file_durations_train33,
                    length=3.0,
                    num=len(positives_train3),
                    trim_table=True)


# Saving these tsv files for future use
negatives_train2.to_csv(
                   '/content/negative2.tsv',
                   mode='a',
                   sep='\t',
                   header=False)

negatives_train33.to_csv(
                   '/content/negative3.tsv',
                   mode='a',
                   sep='\t',
                   header=False)
negatives_train2save = pd.read_csv('/content/negative2.tsv', sep='\t')
negatives_train33save = pd.read_csv('/content/negative3.tsv', sep='\t')


extract_audio(
    'round2_calls', negatives_train2save,
    "/content/neg_pod_calls/", 2,
    "/content/Round2_OS_07_05/wav/")


extract_audio(
    'round3_calls', negatives_train33save,
    "/content/neg_pod_calls/", 2,
    "/content/Round3_OS_09_27_2017/wav/")


plot_spectrogram(
    '/content/Round2_OS_07_05/',
    'train/calls',
    'wav/pod_calls')
plot_spectrogram(
    '/content/Round2_OS_07_05/',
    'train/nocalls',
    'wav/neg_pod_calls')
