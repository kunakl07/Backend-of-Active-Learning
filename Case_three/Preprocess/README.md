### The directions for running the python script of preprocessing using PCEN and Wavelet-Denoising, simply run
 ```
 python preprocess_pcen_wavd.py --tsvpath 
 --audiospath --calltime --outputpathpositive --outputpathnegative 
 --outputplotpathpos --outputplotpathneg 

 ```
 And an example is 


```
 python preprocess_pcen_wavd.py --tsvpath /home/podcast2.tsv 
 --audiospath /home/R2/ --calltime 3 
 --outputpathpositive /home/pos_calls/ 
 --outputpathnegative /home/neg_calls  
 --outputplotpathpos /home/plot_pos/ 
 --outputplotpathneg /home/plot_neg 
```

