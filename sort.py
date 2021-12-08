import os
from joblib import Parallel, delayed
import math

sras = ['SRR13833625','SRR13833626','SRR13833627','SRR13833628','SRR13833629','SRR13221631','SRR13221632','SRR13221633','SRR13221634','SRR13221635','SRR13833630','SRR13833631','SRR13221630']

def trim(sra):
    print("Sorting " + sra + " Currently, please do not exit...")
    y = "/home/ubuntu/project/rnaseq/student_tools/samtools-1.11/samtools sort -o /home/ubuntu/project/rnaseq/STAR_ALIGNMENT/"+sra+"Aligned_sam_sorted.bam /home/ubuntu/project/rnaseq/STAR_ALIGNMENT/"+sra+"Aligned.sortedByCoord.out.bam"
    os.system(y)
    print("Successfully Sorted " + sra)
    
Parallel(n_jobs=7)(delayed(trim)(sra) for sra in sras)

#FeatureCounts
os.system("python3 featureCounts -a /home/ubuntu/project/rnaseq/refs/ref_index/GCF_017639785.1_BCM_Maur_2.0_genomic.gtf  -o featurecounts.txt /home/ubuntu/project/rnaseq/STAR_ALIGNMENT/*.bam")


