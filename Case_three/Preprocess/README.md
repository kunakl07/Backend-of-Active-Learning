### Preprocessing Stage Notebook
The jupyter notebook contains a step by step guide to create spectrograms from their audio files.

### There are three python script 

- preprocess_pcen_waved: This is the python script where in you could insert the path to your audio files and directories and generate the spectrograms.
  Note: The above script is not command line scripts but the user has to manually update the paths
 
- preprocess_pcen_waved: This is the commandline script where in the user just has to give the path to generate the spectrograms. The command would be like

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

 And an example is 

 ```

 python preprocess_pcen_wavd.py --tsvpath /home/podcast2.tsv 
 --audiospath /home/R2/ --calltime 3 
 --outputpathpositive /home/pos_calls/ 
 --outputpathnegative /home/neg_calls  
 --outputplotpathpos /home/plot_pos/ 
 --outputplotpathneg /home/plot_neg 
```

