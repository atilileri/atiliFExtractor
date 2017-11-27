import numpy as np
import extractors as extr
import properties as props

# create sample sound signal
orgSig = list(np.random.random_integers(100, size=100))
orgSigStatic = [51, 15, 31, 6, 38, 61, 17, 49, 80, 75, 28, 89, 72, 98, 100, 69, 30, 27, 38, 27, 99, 65, 70, 4, 21, 37,
                2, 72, 10, 48, 47, 49, 2, 34, 37, 66, 92, 84, 99, 67, 27, 38, 11, 16, 31, 34, 94, 28, 96, 3, 95, 13,
                11, 96, 62, 43, 23, 39, 20, 62, 43, 7, 99, 17, 5, 27, 17, 40, 100, 39, 89, 66, 66, 86, 52, 22, 28, 45,
                67, 52, 22, 31, 86, 47, 68, 64, 94, 62, 25, 91, 44, 8, 91, 44, 3, 51, 46, 63, 25, 25]
# create dictionary resulting vectors
results = dict()

results['orig'] = orgSig
results['pcm'] = extr.pcm(orgSig)
results['pcm-props'] = props.getPropsById(orgSig)
results['pcm-selprops'] = props.getPropsById(orgSig, propIdList=(props.Properties.PropIdMin,
                                                                 props.Properties.PropIdMax,
                                                                 props.Properties.PropIdAmean))
results['lspFreq'] = extr.lspFreq(orgSig)
results['mfccStatic'] = extr.mfcc(orgSigStatic)
results['mfccStatic-selcoefs'] = extr.mfcc(orgSigStatic, firstMFCC=2, lastMFCC=3)
results['mfcc'] = extr.mfcc(orgSig)
results['mfcc-selcoefs'] = extr.mfcc(orgSig, firstMFCC=4, lastMFCC=6)


for k, v in results.items():
    print(k, '\t:', v)
