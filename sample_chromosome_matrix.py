import os, sys
import numpy as np
import pandas as pd
import pickle
from collections import Counter
import pysam
import time
import tqdm
import glob
import torch
import json
import argparse

parser = argparse.ArgumentParser(description='Generate tokens from profile matrix')
parser.add_argument('--in_path', default='./pretraining_data/NC_000022.10.npy', type=str)
parser.add_argument('--out_path', default='./pretraining_data/token_NC_000022.10.txt', type=str)
parser.add_argument('--vocab_path', default='./resource/snp_vocab.json', type=str)
parser.add_argument('--nt_to_idx_path', default='./resource/nucleotide_to_index.json', type=str)
parser.add_argument('--batch_len', default=100000, type=int)
args = vars(parser.parse_args())

torch.set_grad_enabled(False)

# Load Vocab
nt_biallele_code = json.load(open(args['vocab_path'], 'r'))
nt_to_index = json.load(open(args['nt_to_idx_path'], 'r'))
index_to_nt = {v:k for k,v in nt_to_index.items()}

# Prepare input & output
out_file = open(args['out_path'], 'wb')
data = torch.from_numpy(np.load(args['in_path']))

# Loop over chromosome
num_batch = (data.shape[0] // args['batch_len']) + 1
for nb in tqdm.tqdm(range(num_batch)):
    # Build biallelic sequence
    s_idx, e_idx = nb * args['batch_len'], (nb + 1) * args['batch_len']
    values, indices = data[s_idx:e_idx,:].topk(2, dim=-1)
torch.multinomial(input, num_samples, replacement=False, *, generator=None, out=None)
    tokens = []
    for i, (vals, idxs) in enumerate(zip(values, indices)):
        token = []
        for val, idx in zip(vals, idxs):
            if val > 0:
                token.append(index_to_nt[int(idx)])        
        tokens.append(nt_biallele_code['_'.join(sorted(token))])
        
    # Dump string to file
    str_tokens = ''.join(tokens)
    out_file.write(str_tokens.encode('utf8'))
    out_file.flush()
    
# Close file
out_file.close()