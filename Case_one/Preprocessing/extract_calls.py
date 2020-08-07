import pandas as pd
from pydub import AudioSegment
import os


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


# Enter the path of the standardized tsv's
annot_train2, mean2 = duration_mean('/content/podcast2.tsv')
annot_train3, mean3 = duration_mean('/content/podcast3.tsv')
annot_test, mean_test = duration_mean('/content/v10_test.tsv')


# Extract the audio of the calls
extract_audio(
    "round2_calls", annot_train2,
    "/content/pod_calls/", 1,
    "/content/Round2_OS_07_05/wav/")
extract_audio(
    'round3_calls', annot_train2,
    "/content/pod_calls/", 1,
    "/content/Round2_OS_07_05/wav/")
