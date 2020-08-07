# Importing the necessary libraries
import pandas as pd
from ketos.data_handling import selection_table as sl
import ketos.data_handling.database_interface as dbi
from ketos.data_handling.parsing import load_audio_representation
from ketos.audio.spectrogram import MagSpectrogram
from ketos.data_handling.parsing import load_audio_representation


# Reading data_from the files


# Function to add the end time
def add_end(filename):
    filename["end"] = filename["start"] + filename["duration_s"]


# Generate mean and annot-train
def duration_mean(filename):
    annot_train = pd.read_csv(filename, sep='\t')
    mean = annot_train['duration_s'].mean()
    return annot_train, mean

annot_train2, mean2 = duration_mean('/home/kunal/Documents/Orcasound_gsoc/Round2_OS_07_05/podcast2.tsv')
annot_train3, mean3 = duration_mean('/home/kunal/Documents/Orcasound_gsoc/Round2_OS_07_05/podcast3.tsv')
annot_test, mean_test = duration_mean('/home/kunal/Documents/Orcasound_gsoc/Round2_OS_07_05/v10_test.tsv')
annot_val,mean_val = duration_mean('/home/kunal/Documents/Orcasound_gsoc/val2/val_pod3.tsv')

add_end(annot_train2)
add_end(annot_train3)
add_end(annot_test)
annot_train2.head()


# Standardizing the tsv files to generate negative audio
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


std_annot_val = sl.standardize(
                    table=annot_val,
                    signal_labels=["SRKWs"],
                    mapper=map_to_ketos_annot_std,
                    trim_table=True)

# Loading the .json file that contains the necessary parameters for plotting the spectrograms
spec_cfg = load_audio_representation('/home/kunal/Documents/spec_config.json', name="spectrogram")

positives_train2 = sl.select(annotations=std_annot_train2, length=3.0)
file_durations_train2 = sl.file_duration_table(
                              '/home/kunal/Documents/Orcasound_gsoc/Round2_OS_07_05/wav')
dftest.to_csv('test_pod3.tsv', mode='a', header=False)
negatives_train2 = sl.create_rndm_backgr_selections(
                    annotations=std_annot_train2,
                    files=file_durations_train2,
                    length=3.0,
                    num=len(positives_train2),
                    trim_table=True)
selections_train2 = positives_train2.append(negatives_train2)


# Creating the database and storing these spectrogram data in the form of hdf5 files 
dbi.create_database(
      output_file='val3_train_database.h5',
      data_dir='/home/kunal/Documents/Orcasound_gsoc/Round2_OS_07_05/wav',
      dataset_name='wav',
      selections=selections_train2,
      audio_repres=spec_cfg)


# Same steps for Round 3 as well
positives_train3 = sl.select(annotations=std_annot_train3, length=3.0)
file_durations_train3 = sl.file_duration_table('/home/kunal/Documents/Orcasound_gsoc/Round3_OS_09_27_2017/wav')
negatives_train3 = sl.create_rndm_backgr_selections(
                    annotations=std_annot_train3,
                    files=file_durations_train3,
                    length=3.0,
                    num=len(positives_train3),
                    trim_table=True)
selections_train3 = positives_train3.append(negatives_train3)


dbi.create_database(
      output_file='val3_train_database.h5',
      data_dir='/home/kunal/Documents/Orcasound_gsoc/Round3_OS_09_27_2017/wav',
      dataset_name='wav',
      selections=selections_train3,
      audio_repres=spec_cfg)
                                                            

# Same steps for validation data as well


positives_val = sl.select(annotations=std_annot_val, length=3.0)
#positives_train2
file_durations_val = sl.file_duration_table(
                          '/home/kunal/Documents/Orcasound_gsoc/val2/val')
negatives_val=sl.create_rndm_backgr_selections(
                  annotations=std_annot_val,
                  files=file_durations_val,
                  length=3.0,
                  num=len(positives_val),
                  trim_table=True)
selections_val = positives_val.append(negatives_val)


dbi.create_database(
      output_file='val3_train_database.h5',
      data_dir='/home/kunal/Documents/Orcasound_gsoc/val2/val',
      dataset_name='val3',selections=selections_val,
      audio_repres=spec_cfg)

db = dbi.open_file("train_database.h5", 'r')

train_data = dbi.open_table(db, "/wav/data")
val_data = dbi.open_table(db, "/val3/data")


# Performing the same for test data aswell

positives_test = sl.select(annotations=std_annot_test, length=3.0)
file_durations_test = sl.file_duration_table(
                            '/home/kunal/Documents/Orcasound_gsoc/OrcasoundLab09272017_Test/wav')
negatives_test=sl.create_rndm_backgr_selections(
                   annotations=std_annot_test,
                   files=file_durations_test,
                   length=3.0,
                   num=len(positives_test),
                   trim_table=True)

selections_test = positives_test.append(negatives_test, sort=False)

dbi.create_database(
      output_file='test_database.h5',
      data_dir='/home/kunal/Documents/Orcasound_gsoc/OrcasoundLab09272017_Test/wav',
      dataset_name='wav',
      selections=selections_test,
      audio_repres=spec_cfg)


#Checking the values
print(train_data)
print(val_data)


# Closing the database
db.close()

