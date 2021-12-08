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

df= pd.read_csv(sys.argv[1],header=None)
sras = df[0].tolist()

def trim(sra):
    print("Trimming " + sra + " Currently, please do not exit...")
    y = "/home/ubuntu/project/rnaseq/student_tools/TrimGalore-0.6.6/trim_galore --fastqc --illumina --gzip --output_dir /home/ubuntu/project/rnaseq/data/fasta/trimmed --paired /home/ubuntu/project/rnaseq/data/fasta/" + sra + "_1.fastq.gz /home/ubuntu/project/rnaseq/data/fasta/" + sra + "_2.fastq.gz"
    os.system(y)
    print("Successfully trimmed " + sra)
    
Parallel(n_jobs=7)(delayed(trim)(sra) for sra in sras)

