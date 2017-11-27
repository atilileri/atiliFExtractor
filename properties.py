class Properties:
    PropIdNone, PropIdMax, PropIdMin, PropIdRange, PropIdMaxPos, PropIdMinPos, PropIdAmean, PropIdLinregc1, \
        PropIdLinregc2, PropIdLinregerrA, PropIdLinregerrQ, PropIdStddev, PropIdSkewness, PropIdKurtosis, \
        PropIdQuartile1, PropIdQuartile2, PropIdQuartile3, PropIdIqr1_2, PropIdIqr2_3, PropIdIqr1_3 = range(20)


fullPropList = (Properties.PropIdMax,
                Properties.PropIdMin,
                Properties.PropIdRange,
                Properties.PropIdMaxPos,
                Properties.PropIdMinPos,
                Properties.PropIdAmean,
                Properties.PropIdLinregc1,
                Properties.PropIdLinregc2,
                Properties.PropIdLinregerrA,
                Properties.PropIdLinregerrQ,
                Properties.PropIdStddev,
                Properties.PropIdSkewness,
                Properties.PropIdKurtosis,
                Properties.PropIdQuartile1,
                Properties.PropIdQuartile2,
                Properties.PropIdQuartile3,
                Properties.PropIdIqr1_2,
                Properties.PropIdIqr2_3,
                Properties.PropIdIqr1_3)


def getPropsById(inSig, propIdList=fullPropList):
    properties = {}
    for propId in propIdList:
        if Properties.PropIdNone == propId:
            return None
        elif Properties.PropIdMax == propId:
            properties['max'] = getMax(inSig)
        elif Properties.PropIdMin == propId:
            properties['min'] = getMin(inSig)
        elif Properties.PropIdRange == propId:
            properties['range'] = getRange(inSig)
        elif Properties.PropIdMaxPos == propId:
            properties['maxPos'] = getMaxPos(inSig)
        elif Properties.PropIdMinPos == propId:
            properties['minPos'] = getMinPos(inSig)
        elif Properties.PropIdAmean == propId:
            properties['aMean'] = getAmean(inSig)
        elif Properties.PropIdLinregc1 == propId:
            properties['linregc1'] = getLinregc1(inSig)
        elif Properties.PropIdLinregc2 == propId:
            properties['linregc2'] = getLinregc2(inSig)
        elif Properties.PropIdLinregerrA == propId:
            properties['linreggerrA'] = getLinregerrA(inSig)
        elif Properties.PropIdLinregerrQ == propId:
            properties['linreggerrQ'] = getLinregerrQ(inSig)
        elif Properties.PropIdStddev == propId:
            properties['stddev'] = getStddev(inSig)
        elif Properties.PropIdSkewness == propId:
            properties['skewness'] = getSkewness(inSig)
        elif Properties.PropIdKurtosis == propId:
            properties['kurtosis'] = getKurtosis(inSig)
        elif Properties.PropIdQuartile1 == propId:
            properties['quartile1'] = getQuartile1(inSig)
        elif Properties.PropIdQuartile2 == propId:
            properties['quartile2'] = getQuartile2(inSig)
        elif Properties.PropIdQuartile3 == propId:
            properties['quartile3'] = getQuartile3(inSig)
        elif Properties.PropIdIqr1_2 == propId:
            properties['iqr1_2'] = getIqr1_2(inSig)
        elif Properties.PropIdIqr2_3 == propId:
            properties['iqr2_3'] = getIqr2_3(inSig)
        elif Properties.PropIdIqr1_3 == propId:
            properties['iqr1_3'] = getIqr1_3(inSig)
    return properties


def getMax(inSig):
    # todo implement
    return 0


def getMin(inSig):
    # todo implement
    return 0


def getRange(inSig):
    # todo implement
    return 0


def getMaxPos(inSig):
    # todo implement
    return 0


def getMinPos(inSig):
    # todo implement
    return 0


def getAmean(inSig):
    # todo implement
    return 0


def getLinregc1(inSig):
    # todo implement
    return 0


def getLinregc2(inSig):
    # todo implement
    return 0


def getLinregerrA(inSig):
    # todo implement
    return 0


def getLinregerrQ(inSig):
    # todo implement
    return 0


def getStddev(inSig):
    # todo implement
    return 0


def getSkewness(inSig):
    # todo implement
    return 0


def getKurtosis(inSig):
    # todo implement
    return 0


def getQuartile1(inSig):
    # todo implement
    return 0


def getQuartile2(inSig):
    # todo implement
    return 0


def getQuartile3(inSig):
    # todo implement
    return 0


def getIqr1_2(inSig):
    # todo implement
    return 0


def getIqr2_3(inSig):
    # todo implement
    return 0


def getIqr1_3(inSig):
    # todo implement
    return 0

