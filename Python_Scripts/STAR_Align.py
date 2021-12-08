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

#build index (hash out if previously done)
os.system("/home/ubuntu/project/rnaseq/student_tools/STAR-2.5.2a/bin/Linux_x86_64/STAR --runThreadN 8 --runMode genomeGenerate \
    --genomeDir ./STAR_index --genomeFastaFiles /home/ubuntu/project/rnaseq/refs/ref_index/GCA_000349665_1.fasta \
    --sjdbGTFfile /home/ubuntu/project/rnaseq/refs/Mesocricetus_auratus.MesAur1.0.104.gtf--sjdbOverhang 99")

for sra in sras:
    print("Aligning " + sra)
    y ="STAR --runThreadN 31 --genomeDir /home/ubuntu/project/rnaseq/STAR_INDEX  --limitGenomeGenerateRAM 120000000000 --readFilesIn /home/ubuntu/project/rnaseq/data/fasta/trimmed/"+ sra +"_1_val_1.fq.gz /home/ubuntu/project/rnaseq/data/fasta/trimmed/" + sra +"_2_val_2.fq.gz --readFilesCommand zcat --outSAMtype BAM SortedByCoordinate --quantMode GeneCounts --outFileNamePrefix /home/ubuntu/project/rnaseq/STAR_ALIGNMENT/"+ sra
    os.system(y)
    print("Successfully aligned " + sra)
    continue
