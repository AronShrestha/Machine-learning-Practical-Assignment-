from re import L
import numpy as np

def load_data(dataset_name):
    features=[]
    target = []
    target_names=set()
    with open('{0}.tsv'.format(dataset_name) )as ifile:
        for line in ifile:
            tokens = line.strip().split('\t')
            features.append([float(values) for values in tokens[:-1]])
            target.append(tokens[-1])
            target_names.add(tokens[-1])
    target_names=list(target_names)
    target_names.sort()
    target = [target_names.index(i) for i in target]
    target=np.array(target)
    features=np.array(features)
    return {
        'features':features,
        'target_names':target_names,
        'target':target,
    }

