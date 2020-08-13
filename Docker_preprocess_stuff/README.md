### Docker command to build, here preprocess is the name of the container

```
sudo docker build -t 'preprocess' .
```
### Docker command to run the process 

```
 sudo docker run -ti preprocess_three --tsv_path test_extract_audio.tsv --files_dir .  --call_time 3 --output_dir output_dir/ --power_spectral_density 
```
