### Preprocessing Stage Notebook
The jupyter notebook contains a step by step guide to create spectrograms from their audio files.

### There are three python script 
- Extract_calls: This python script allows user to extract calls from the audio files, and the parameters such as start-time and 
                  the end time are taken from the .tsv file.
- Preprocess_case_one: This is the python script where in you could insert the path to your audio files and directories and generate the spectrograms.
  Note: The above two scripts are not command line scripts but the user has to manually update the paths
 
- simple_preprocess: This is the commandline script where in the user just has to give the path to generate the spectrograms. The command would be like

```
python simple_preprocess.py --tsvpath --audiopath --calltime
--outputpathpositive --outputpathnegative
--outputplotpathpos --outputplotpathneg

```
Here the parameters are:
- tsvpath: The path to the .tsv file
- audiopath: The path to the audio
- calltime: The call time of the SRKWs
- outputpathpositive: The output path of the positive extracted calls
- outputpathnegative: The output path of the negative extracted calls
- outplotpathpos: The output path where the spectrgrams are plotted from the extracted audio files containing calls
- outputplotpathneg:  The output path where the spectrgrams are plotted from the extracted audio files not containing calls
