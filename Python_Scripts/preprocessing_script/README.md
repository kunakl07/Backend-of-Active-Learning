
Command for running the script, you could use either of the combination with different cases to generate spectrograms

```

python3 preprocessing.py --tsv_path [Path to the tsv file] --files_dir [Path to the audio file] --call_time [Call duration in seconds] --output_dir [Path to the output directory] --power_spectral_density [type of spectrogram] --grayscale [preprocessing methods] 
```
```
python3 preprocessing.py --tsv_path [Path to the tsv file] --files_dir [Path to the audio file] --call_time [Call duration in seconds] --output_dir [Path to the output directory] --melspectrogram [type of spectrogram] --pcen --wavelets [preprocessing methods] 
```
`
