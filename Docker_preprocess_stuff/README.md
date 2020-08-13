### Docker command to build, here preprocess is the name, I have given 
```
sudo docker build -t 'preprocess' .
```
### Docker command to run the process(you could run any of the tsv file, call time, preprocessing command)

```
 sudo docker run -ti preprocess_three --tsv_path test_extract_audio.tsv --files_dir .  --call_time 3 --output_dir output --power_spectral_density 
```
### If you want to explore the container

```
 sudo docker ps -a
```

### After finding the name of the container run the following command, here stupefied_dirac is my container name, replace it with your container name

```
sudo docker start stupefied_dirac
```

### Copy those commands to the output directory and replace the 'output_path' by your output directory name where you want your output

```
 sudo docker cp stupefied_dirac:/usr/src/app/output_dir/ output_path/
```
