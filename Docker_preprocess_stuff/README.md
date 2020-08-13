### Docker command to build, here preprocess is the name of the container

```
sudo docker build -t 'preprocess' .
```
### Docker command to run the process 

```
 sudo docker run -ti preprocess_three --tsv_path test_extract_audio.tsv --files_dir .  --call_time 3 --output_dir . --power_spectral_density 
```
### If you want to explore the container

```
 sudo docker ps -a
```

### After finding the name of the container run the following command, here stupefied_dirac is my container name, replace it with your container name

```
sudo docker start stupefied_dirac
```

### Copy those commands to the output directory

```
 sudo docker cp stupefied_dirac:/usr/src/app/output_dir/ output_path/
```
