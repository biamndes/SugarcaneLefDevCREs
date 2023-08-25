#!/usr/bin/env python3

import argparse
from Bio import SeqIO
import re

parser= argparse.ArgumentParser(description='Sequence extractor based on a list')
parser.add_argument('listfile', type=str,
                                    help='file.txt with the name of each id in a line')

parser.add_argument('fastafile', type=str,
                                    help='fasta file')

parser.add_argument('outputfile', type=str,
                                            help='output file')
parser.add_argument('--index', action='store_true',
                                    help='store true if there is a fasta index')
parser.add_argument('--fastaindex', type=str,
                                            help='file with all the ids in fasta file')
args = parser.parse_args()

fasta = args.fastafile
ids = args.listfile
index = args.fastaindex
output = args.outputfile
count = 0
totalids = 0

with open(ids) as f:
    wanted_ids = [l[:-1] for l in f]
#    print("wanted ids", wanted_ids)
    totalids=len(wanted_ids)
#    print(totalids)

with open(output,'w') as out:
    for record in SeqIO.parse(fasta, "fasta"):
        if record.id in wanted_ids:
            count += 1
            SeqIO.write(record, out, "fasta")
    if args.index:
        records=index
        with open (index, "r") as records:
            for line in records:
                for id in wanted_ids:
                    search=str((rf"='{id}',"))                    
                    if search not in line:
                        print("ID", id, "not found in fasta file")

print(str(count) + " records selected out of " + str(totalids) , "in", ids)
