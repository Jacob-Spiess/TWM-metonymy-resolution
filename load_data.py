import numpy as np
import json
import os

def extract(results):
    ret = {}
    for key, val in results.items():
        steps = []
        accs = []
        for line in val:
            if not line:
                continue
            steps.append(int(line.split(':')[1].split('-')[0].strip()))
            accs.append(float(line.split('=')[1].strip()))
        ret[key] = (steps, accs)
    return ret



def load():
    # load data for original model
    with open(os.path.join('output_wimcor', 'eval_results_wimcor_test.json'), encoding='utf-8') as f:
        wimcor_in = f.readlines()
    with open(os.path.join('output_conll', 'eval_results_conll_test.json'), encoding='utf-8') as f:
        conll_in = f.readlines()
    with open(os.path.join('output_semeval', 'eval_results_semeval_test.json'), encoding='utf-8') as f:
        semeval_in = f.readlines()
    with open(os.path.join('output_relocar', 'eval_results_relocar_test.json'), encoding='utf-8') as f:
        relocar_in = f.readlines()
    with open(os.path.join('output_gwn', 'eval_results_gwn_test.json'), encoding='utf-8') as f:
        gwn_in = f.readlines()

    with open(os.path.join('output_gwn_no_mask', 'eval_results_gwn_test.json'), encoding='utf-8') as f:
        gwn_nm = f.readlines()
    with open(os.path.join('output_semeval_no_mask', 'eval_results_semeval_test.json'), encoding='utf-8') as f:
        semeval_nm = f.readlines()
    with open(os.path.join('output_relocar_no_mask', 'eval_results_relocar_test.json'), encoding='utf-8') as f:
        relocar_nm = f.readlines()
    with open(os.path.join('output_conll_no_mask', 'eval_results_conll_test.json'), encoding='utf-8') as f:
        conll_nm = f.readlines()
    with open(os.path.join('output_wimcor_no_mask', 'eval_results_wimcor_test.json'), encoding='utf-8') as f:
        wimcor_nm = f.readlines()

    with open(os.path.join('output_relocar', 'eval_results_semeval_test.json'), encoding='utf-8') as f:
        relocar_semeval = f.readlines()
    with open(os.path.join('output_semeval', 'eval_results_relocar_test.json'), encoding='utf-8') as f:
        semeval_relocar = f.readlines()
    with open(os.path.join('output_conll', 'eval_results_relocar_test.json'), encoding='utf-8') as f:
        conll_relocar = f.readlines()
    with open(os.path.join('output_conll', 'eval_results_semeval_test.json'), encoding='utf-8') as f:
        conll_semveval = f.readlines()
    with open(os.path.join('output_wimcor', 'eval_results_relocar_test.json'), encoding='utf-8') as f:
        wimcor_relocar = f.readlines()
    with open(os.path.join('output_wimcor', 'eval_results_semeval_test.json'), encoding='utf-8') as f:
        wimcor_semeval = f.readlines()

    with open(os.path.join('output_relocar_no_mask', 'eval_results_semeval_test.json'), encoding='utf-8') as f:
        relocar_semeval_nm = f.readlines()
    with open(os.path.join('output_semeval_no_mask', 'eval_results_relocar_test.json'), encoding='utf-8') as f:
        semeval_relocar_nm = f.readlines()
    with open(os.path.join('output_conll_no_mask', 'eval_results_relocar_test.json'), encoding='utf-8') as f:
        conll_relocar_nm = f.readlines()
    with open(os.path.join('output_conll_no_mask', 'eval_results_semeval_test.json'), encoding='utf-8') as f:
        conll_semveval_nm = f.readlines()
    with open(os.path.join('output_wimcor_no_mask', 'eval_results_relocar_test.json'), encoding='utf-8') as f:
        wimcor_relocar_nm = f.readlines()
    with open(os.path.join('output_wimcor_no_mask', 'eval_results_semeval_test.json'), encoding='utf-8') as f:
        wimcor_semeval_nm = f.readlines()

    data = {
        'in-domain':{
            'semeval' : semeval_in,
            'relocar' : relocar_in,
            'conll'   : conll_in,
            'gwn'     : gwn_in,
            'wimcor'  : wimcor_in
        },
        'cross-domain':{
            'semeval-relocar' : semeval_relocar,
            'relocar-semeval' : relocar_semeval,
            'conll-relocar'   : conll_relocar,
            'conll-semeval'   : conll_semveval,
            'wimcor-relocar'  : wimcor_relocar,
            'wimcor-semeval'  : wimcor_semeval
        },
        'in-domain-nm': {
            'semeval' : semeval_nm,
            'relocar' : relocar_nm,
            'conll'   : conll_nm,
            'gwn'     : gwn_nm,
            'wimcor' : wimcor_nm
        },
        'cross-domain-nm':{
            'semeval-relocar' : semeval_relocar_nm,
            'relocar-semeval' : relocar_semeval_nm,
            'conll-relocar' : conll_relocar_nm,
            'conll-semeval' : conll_semveval_nm,
            'wimcor-relocar' : wimcor_relocar_nm,
            'wimcor-semeval' : wimcor_semeval_nm
        },
    }

    with open(os.path.join('output_wimcor_test', 'eval_results_wimcor_test.json'), encoding='utf-8') as f:
        wimcor_in = f.readlines()
    with open(os.path.join('output_wimcor_test', 'eval_results_relocar_test.json'), encoding='utf-8') as f:
        wimcor_relocar = f.readlines()
    with open(os.path.join('output_wimcor_test', 'eval_results_semeval_test.json'), encoding='utf-8') as f:
        wimcor_semeval = f.readlines()
    with open(os.path.join('output_conll_test', 'eval_results_conll_test.json'), encoding='utf-8') as f:
        conll_in = f.readlines()
    with open(os.path.join('output_conll_test', 'eval_results_relocar_test.json'), encoding='utf-8') as f:
        conll_relocar = f.readlines()
    with open(os.path.join('output_conll_test', 'eval_results_semeval_test.json'), encoding='utf-8') as f:
        conll_semveval = f.readlines()
    with open(os.path.join('output_semeval_test', 'eval_results_semeval_test.json'), encoding='utf-8') as f:
        semeval_in = f.readlines()
    with open(os.path.join('output_semeval_test', 'eval_results_relocar_test.json'), encoding='utf-8') as f:
        semeval_relocar = f.readlines()
    with open(os.path.join('output_relocar_test', 'eval_results_relocar_test.json'), encoding='utf-8') as f:
        relocar_in = f.readlines()
    with open(os.path.join('output_relocar_test', 'eval_results_semeval_test.json'), encoding='utf-8') as f:
        relocar_semeval = f.readlines()
    with open(os.path.join('output_gwn_test', 'eval_results_gwn_test.json'), encoding='utf-8') as f:
        gwn_in = f.readlines()

    data_new = {
        'in-domain':{
            'semeval' : semeval_in,
            'relocar' : relocar_in,
            'conll' : conll_in,
            'gwn' : gwn_in,
            'wimcor' : wimcor_in
        },
        'cross-domain':{
            'semeval-relocar' : semeval_relocar,
            'relocar-semeval' : relocar_semeval,
            'conll-relocar' : conll_relocar,
            'conll-semeval' : conll_semveval,
            'wimcor-relocar' : wimcor_relocar,
            'wimcor-semeval' : wimcor_semeval
        }
    }


    in_domain_new = extract(data_new['in-domain'])
    cross_domain_new = extract(data_new['cross-domain'])
    in_domain = extract(data['in-domain'])
    cross_domain = extract(data['cross-domain'])
    in_domain_nm = extract(data['in-domain-nm'])
    cross_domain_nm = extract(data['cross-domain-nm'])

    return in_domain_new, cross_domain_new, in_domain, cross_domain, in_domain_nm, cross_domain_nm