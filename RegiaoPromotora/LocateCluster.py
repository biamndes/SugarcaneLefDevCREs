#!/usr/bin/env python3

import argparse
import pandas as pd
import re

parser = argparse.ArgumentParser(description='Organize gene ID according to co-expression data')
parser.add_argument('tsv_data', type=str, 
                                    help='gene and cluster in tsv format')
parser.add_argument('outfile_prefix', type=str, help='It is prefix for the output files.')

args = parser.parse_args()

tsv_data=args.tsv_data

genecluster=pd.read_csv(tsv_data, sep="\t")


dictgenecluster={}
for i,r in genecluster.iterrows():
    if r['cluster'] not in dictgenecluster.keys():
        dictgenecluster[r['cluster']]=[]
    dictgenecluster[r['cluster']].append(r['transcript'])

for cluster in dictgenecluster.keys():
    fastaoutput = args.outfile_prefix + '_' + str(cluster) + "_coexpression.txt"
    with open (fastaoutput, "w") as clusterfile:
        for ID in dictgenecluster[cluster]:
            clusterfile.write(ID+"\n")



