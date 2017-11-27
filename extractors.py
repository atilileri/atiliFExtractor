import math


def pcm(inSig):
    # todo implement main operation
    outSig = []

    return outSig

# minimum value of melspectra when computing mfcc
melFloor = 0.00000001
# parameter for cepstral 'liftering', set to 0.0 to disable cepstral liftering
cepLifter = 22.0
cosTable = []
sinTable = []


# compute sin/cos tables
def initTables(lenInSig, firstMFCC, lastMFCC):
    global cosTable
    global sinTable
    cosTable = [None] * lenInSig * (lastMFCC - firstMFCC + 1)
    sinTable = [None] * (lastMFCC - firstMFCC + 1)

    for i in range(firstMFCC, lastMFCC+1):
        for m in range(lenInSig):
            cosTable[m + (i - firstMFCC) * lenInSig] = math.cos(math.pi * ( i / lenInSig) * (m + 0.5))
    if cepLifter > 0:
        for i in range(firstMFCC, lastMFCC+1):
            sinTable[i - firstMFCC] = 1.0 + cepLifter / 2.0 * math.sin(math.pi * i / cepLifter)
    else:
        for i in range(firstMFCC, lastMFCC + 1):
            sinTable[i - firstMFCC] = 1.0


# todo hocayla konus max min isini
def mfcc(inSig, firstMFCC=1, lastMFCC=12):
    # todo implement main operation
    lenInSig = len(inSig)
    tempInSig = [None] * lenInSig
    outSig = [None] * (lastMFCC - firstMFCC + 1)
    initTables(lenInSig, firstMFCC, lastMFCC)

    # compute log mel spectrum
    for i in range(lenInSig):
        if inSig[i] < melFloor:
            tempInSig[i] = math.log(melFloor)
        else:
            tempInSig[i] = math.log(inSig[i])

    # compute dct of mel data & do cepstral liftering
    factor = math.sqrt(2.0/lenInSig)
    for i2 in range(firstMFCC, lastMFCC+1):
        j = i2 - firstMFCC
        k = j
        if 0 == firstMFCC:
            if i2 == lastMFCC:
                k = 0
            else:
                k = j + 1
        outSig[j] = 0.0
        for m in range(lenInSig):
            outSig[j] += tempInSig[m] * cosTable[m + k * lenInSig]
        # outSig[j] *= factor # use this line, if you want unliftered mfcc
        # do cepstral liftering
        outSig[j] *= sinTable[k] * factor

    return outSig


def lspFreq(inSig):
    # todo implement main operation
    return inSig
