#!/usr/bin/env python 

# add shebang at top of file
# shebang tells the shell how to interpret the file

# Set permission to run file
#    ls -la 
#    chmod ugo+x get_sra.py 
#
import subprocess
import pandas as pd
import sys
import os.path
import os
from joblib import Parallel, delayed
import math

if len(sys.argv) ==1:
  print("TOO FEW ARGUMENTS... PLEASE ADD SRR_ACC_LIST.TXT FILE")
  sys.exit(-1)
elif len(sys.argv) >2:
  print("TOO MANY ARGUMENTS... IGNORING EXTRA ARGUMENTS...")
  
if os.path.isfile(sys.argv[1]) == False:
  print("SRR FILE NOT FOUND... EXITING...")                   
  sys.exit(-2)

cwd = (str(os.getcwd()) + '/')
print(cwd)
print("PROGRAM RUNNING...")

# open SRR_Acc_list.txt

df= pd.read_csv(sys.argv[1],header=None)
sras = df[0].tolist()

def download(sra):
#skipping sra download for already downloaded .fastq file
    subprocess.call(['prefetch','-p 1' ,'--output-directory', cwd, sra])
    subprocess.call(['fastq-dump',"--split-files", "--gzip",sra + ".sra"])

Parallel(n_jobs=5)(delayed(download)(sra) for sra in sras)

    #subprocess.run(['fastq-dump',sra])
# open SRR_Acc_list.txt
# use pandas
# read.csv with pandas

# for every line
#   get the SRR number
#   download the SRA file


#Conda tips
#1) On osc enable python with ...
# module load python
# module load sratoolkit
#2) Create environment with
# conda create -n getsra
#3) Activate environment
# conda activate getsra
# source activate getsra
#4) Install pandas
# conda install pandas
#5) list environments on system