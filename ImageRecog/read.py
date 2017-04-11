from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

import time


def whatNumIsThis(filePath):

    matchedAr = []
    loadExamps = open("numArEx.txt", "r").read()
    loadExamps = loadExamps.split("\n")

    i = Image.open(filePath)
    iar = np.array(i)
    iarl = iar.tolist()

    inQuestion = str(iarl)

    for eachExample in loadExamps:
        try:
            splitEx = eachExample.split("::")
            currentNum = splitEx[0]
            currentAr = splitEx[1]

            eachPixEx = currentAr.split("],")
            eachPixInQ = inQuestion.split("],")

            for x in range(0, len(eachPixEx)):
                if eachPixEx[x] == eachPixInQ[x]:
                    matchedAr.append(int(currentNum))

        except Exception as e:
            print(str(e))

    x = Counter(matchedAr)

    print(x)
    graphX = []
    graphY = []

    ylimi = 0

    for each in x:
        graphX.append(each)
        graphY.append(x[each])
        ylimi = x[each]

    fig = plt.figure()
    ax1 = plt.subplot2grid((4,4),(0,0), rowspan=1, colspan=4)
    ax2 = plt.subplot2grid((4,4),(1,0), rowspan=3, colspan=4)

    ax1.imshow(iar)
    ax2.bar(graphX, graphY, align='center')
    plt.ylim(400)

    xloc = plt.MaxNLocator(12)
    ax2.xaxis.set_major_locator(xloc)

    plt.show()

whatNumIsThis("test.png")
