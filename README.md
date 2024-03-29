# SNP2Vec: Scalable Self-Supervised Pre-Training for Genome-Wide Association Study
![Pull Requests Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat) [![GitHub license](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/HLTCHKUST/snp2vec/blob/main/LICENSE) [![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-v2.0%20adopted-ff69b4.svg)](CODE_OF_CONDUCT.md)

<b>SNP2Vec</b> is a scalable self-supervised  pre-training approach for understanding SNP patterns of genomic sequences. The effectiveness of SNP2Vec has been evaluated for Alzheimer's disease risk in a Chinese cohort and is found to significantly outperforms existing polygenic risk score methods and all other deep learning baselines which are trained on haploid sequences.

## Research Paper
SNP2Vec has been accepted by BioNLP 2022 and you can find the details in our paper <TODO>.
If you are using any component on SNP2Vec including the token mapping resources, the cached chromosome matrix, or the Alzheimer's disease risk dataset in your work, please cite the following paper:
```
@inproceedings{cahyawijaya-etal-2022-snp2vec,
    title = "{SNP}2{V}ec: Scalable Self-Supervised Pre-Training for Genome-Wide Association Study",
    author = "Cahyawijaya, Samuel  and
      Yu, Tiezheng  and
      Liu, Zihan  and
      Zhou, Xiaopu  and
      Mak, Tze Wing Tiffany  and
      Ip, Yuk Yu Nancy  and
      Fung, Pascale",
    booktitle = "Proceedings of the 21st Workshop on Biomedical Language Processing",
    month = may,
    year = "2022",
    address = "Dublin, Ireland",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2022.bionlp-1.14",
    doi = "10.18653/v1/2022.bionlp-1.14",
    pages = "140--154",
    abstract = "Self-supervised pre-training methods have brought remarkable breakthroughs in the understanding of text, image, and speech. Recent developments in genomics has also adopted these pre-training methods for genome understanding. However, they focus only on understanding haploid sequences, which hinders their applicability towards understanding genetic variations, also known as single nucleotide polymorphisms (SNPs), which is crucial for genome-wide association study. In this paper, we introduce SNP2Vec, a scalable self-supervised pre-training approach for understanding SNP. We apply SNP2Vec to perform long-sequence genomics modeling, and we evaluate the effectiveness of our approach on predicting Alzheimer{'}s disease risk in a Chinese cohort. Our approach significantly outperforms existing polygenic risk score methods and all other baselines, including the model that is trained entirely with haploid sequences.",
}
```

## Repository Structure 
We provide code and resources to generate the SNP pre-training dataset which we use to build the Dipformer model in our paper.
- [resources/nucleotide_to_index.json](https://github.com/HLTCHKUST/snp2vec/blob/main/resources/nucleotide_to_index.json) | Mapping of the nucleotide and indel tokens to index on the chromosome matrix
- [resources/snp_vocab.json](https://github.com/HLTCHKUST/snp2vec/blob/main/resources/snp_vocab.json) | Mapping of the multi-characters SNP tokens code into the single-character SNP tokens code
- [gen_chromosome_matrix.ipynb](https://github.com/HLTCHKUST/snp2vec/blob/main/gen_chromosome_matrix.ipynb) | Python script to generate chromosome matrix from the reference genome Fasta file and dbSNP Tabix file
- [sample_chromosome_matrix.py](https://github.com/HLTCHKUST/snp2vec/blob/main/sample_chromosome_matrix.py) | Python script to perform sampling from a given chromosome matrix and generate a SNP-encoded chromosome sequence
- [sample_chromosome_matrix.sh](https://github.com/HLTCHKUST/snp2vec/blob/main/sample_chromosome_matrix.sh) | Example shell script to run `sample_chromosome_matrix.py`
- [gen_dataset_tokenizer.ipynb](https://github.com/HLTCHKUST/snp2vec/blob/main/gen_dataset_tokenizer.ipynb) | Python script to generate the pre-training dataset and tokenizer from the SNP-encoded chromosome sampled from `sample_chromosome_matrix.py`
  
## Chromosome Matrix
We provide two pre-processed chromosome matrix for Chromosome-19 and Chromosome-21 which build from GRCh37 and dbSNP 153
- [Chromosome-19](https://storage.googleapis.com/samcah-bucket/alzheimer-split/NC_000019.9.npy) (4.8GB)
- [Chromosome-21](https://storage.googleapis.com/samcah-bucket/alzheimer-split/NC_000021.8.npy) (3.9GB)
  
For generating other chromosome matrices, you can check the [`gen_chromosome_matrix.ipynb`](https://github.com/HLTCHKUST/snp2vec/blob/main/gen_chromosome_matrix.ipynb) provided on this repo.
  
## Alzheimer's Disease Risk Dataset
To access the Alzheimer's disease risk dataset used for evaluating the model in our paper, you need to request and sign a Data Use Agreement (DUA) by contacting Tiffany T.W MAK (tiffanytze@ust.hk) or Xiaopu Zhou (xpzhou@ust.hk).
