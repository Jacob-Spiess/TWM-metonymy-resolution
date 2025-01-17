# Target Word Masking for Location Metonymy Resolution

Code for the paper [Target Word Masking for Location Metonymy Resolution](metonymy_resolution_long.pdf) published in COLING 2020.

## Abstract
 Existing metonymy resolution approaches rely on features extracted
  from external resources like dictionaries and hand-crafted lexical
  resources.  In this paper, we propose an end-to-end word-level
  classification approach based only on BERT, without dependencies on
  taggers, parsers, curated dictionaries of place names, or other
  external resources. We show that our approach achieves the
  state-of-the-art on 5 datasets, surpassing conventional BERT models
  and benchmarks by a large margin. We also show that our approach
  generalises well to unseen data.

## Requirements

- python 3.6
- pytorch 1.6
- [transformers 3.4](https://github.com/huggingface/transformers)

## Overview

The code is based on [`transformers`](https://github.com/huggingface/transformers).

### Data

All data mentioned in the paper is in [`data`](https://github.com/haonan-li/TWM-metonymy-resolution/tree/main/data) directory. For metonymy resolution, datasets are transferred to the same format. 

Note that we use a subset of [`WiMCor`](https://kevinalexmathews.github.io/software/) and re-split it. 

### Metonymy Resolution

#### Prewin baselines 
We use the code in [this](https://github.com/nlpAThits/WiMCor) repo to generate the `Prewin` baselines, which is based on [Minimalist Location Metonymy Resolution](https://github.com/milangritta/Minimalist-Location-Metonymy-Resolution)

#### Our model
To run our metonymy resolution model, you just need to specify the arguments for `src/run_metonymy_resolution.py`.

For example: 
```bash
python run_metonymy_resolution.py \
--data_dir ../data \
--train_file conll_train.json \
--predict_file conll_test.json \
--output_dir ../output \
--do_train  \
--do_eval \
--do_mask
```

For single input test, you can see [single_example.ipynb](single_example.ipynb).


### Extrinsic Evaluation

#### Edinburgh Geoparser
First download [Edinburgh Geoparser](https://www.ltg.ed.ac.uk/software/geoparser/), use it to detect toponyms, then use `run_metonymy_resolution.py` to classify the readings.

#### NCRF++ 
First download [NCRF++](https://github.com/jiesutd/NCRFpp), modify config file, then train and test.

#### Bert tagger
Run `run_bert_tagger.py` on the data in `data/geoparsing/gold` directly.

#### Our model
Run `run_bert_tagger.py` on the data in `data/geoparsing/gold_entity` to first detect the toponyms. Then convert predictions to json file. Finally, use `run_metonymy_resolution.py` to classify the readings.

Run bert tagger by running

`python run_bert_tagger.py --data_dir ../data/geoparsing/gold_toponym --output_dir ../output/geoparsing/ --labels ../data/geoparsing/gold_toponym/labels_bmes.txt --train_file train0_bmes.txt --test_file test0_bmes.txt --do_predict --overwrite_output_dir --do_train --do_eval`
