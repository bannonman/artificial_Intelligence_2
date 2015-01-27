__author__ = 'coreyandrewbannon'


def genResults():
    import math
    from statistics import mode
    import sys

    list1 = list()
    cardList = list()
    sortedList = list()
    medList = list()
    modeList = list()
    secmodeList = list()


    dict = {0: 'symboling', 1:'normalized-losses',2:'make',3:'fuel-type',4:'aspiration',5:'num-of-doors',6:'body-style',
            7:'drive-wheels',8:'engine-location',9:'wheel-base',10:'length',11:'width',12:'height',13:'curb-weight',
            14:'engine-type',15:'num-of-cylinders',16:'engine-size',17:'fuel-system',18:'bore',19:'stroke',
            20:'compression-ratio',21:'horsepower',22:'peak-rpm',23:'city-mpg',24:'highway-mpg',25:'price'};


    fileName = input('Enter name of text file: ')+'.txt'
    newFile = open("reports/"+fileName, 'w')
    newFile.close()


    with open("data/DataSet.txt") as f:
        for line in f:
            car = list()
            information = line.strip().split(',')
            for line in information:
                car.append(line)
            list1.append(car)

    def categorical(i):
        total = 0
        mean = 0
        count = 0
        count1 = 0
        notin = 0
        miss = 0
        card = 0
        modecount = 0

        for list2 in list1:
            if(list2[i]!='?'):
                cardList.append(list2[i])
                count = count + 1
                count1 = count - notin
            else:
                notin = notin + 1
                count = count + 1

        ca = set(cardList)
        card = len(ca)
        miss = (notin / count)*100
        modes = mode(cardList)
        for list2 in list1:
            if(list2[i]!=modes):
                secmodeList.append(list2[i])

        modecount = cardList.count(modes)
        modeper = (modecount / count1)*100
        secondmode = mode(secmodeList)
        secmodecount = secmodeList.count(secondmode)
        secmodeper = (secmodecount / count1)*100

        # Open a file
        fo = open("reports/"+fileName, "a")
        fo.write(dict[i]);
        fo.write("|");
        fo.write(str(count1));
        fo.write("|");
        fo.write(str(round(miss,2)));
        fo.write("|");
        fo.write(str(round(card,2)));
        fo.write("|");
        fo.write(str(modes));
        fo.write("|");
        fo.write(str(round(modecount,2)));
        fo.write("|");
        fo.write(str(round(modeper,2)));
        fo.write("|");
        fo.write(str(secondmode));
        fo.write("|");
        fo.write(str(round(secmodecount,2)));
        fo.write("|");
        fo.write(str(round(secmodeper,2)));
        fo.write("|");
        fo.write("\n");

        # Close opend file
        fo.close()


    def continuous(i):
        total = 0
        mean = 0
        count = 0
        count1 = 0
        notin = 0
        miss = 0
        card = 0
        mini = 0
        maxi = 0
        median = 0
        onestquart = 0
        threerdquart = 0
        stand_dev = 0
        square = 0
        sq_tot = 0
        sd_mean = 0

        for list2 in list1:
            if(list2[i]!='?'):
                total = total + float(list2[i])
                cardList.append(float(list2[i]))
                medList.append(float(list2[i]))
                square = float(list2[i]) - mean
                square = square * square
                sq_tot = sq_tot + square
                count = count + 1
                count1 = count - notin
            else:
                notin = notin + 1
                count = count + 1

        ca = set(cardList)
        card = len(ca)
        miss = (notin / count)*100
        mean = total / count1
        medList.sort()
        mini = min(medList)
        maxi = max(medList)
        median = medList[int(count/2)]
        onestquart = medList[int((count/2)/2)]
        threerdquart = medList[int((count/2)+((count/2)/2))]
        sd_mean = sq_tot / count1
        stand_dev = math.sqrt(sd_mean)

        # Open a file
        fo = open("reports/"+fileName, "a")
        fo.write(dict[i]);
        fo.write("|");
        fo.write(str(count1));
        fo.write("|");
        fo.write(str(round(miss,2)));
        fo.write("|");
        fo.write(str(round(card,2)));
        fo.write("|");
        fo.write(str(round(mini,2)));
        fo.write("|");
        fo.write(str(round(onestquart,2)));
        fo.write("|");
        fo.write(str(round(mean,2)));
        fo.write("|");
        fo.write(str(round(median,2)));
        fo.write("|");
        fo.write(str(round(threerdquart,2)));
        fo.write("|");
        fo.write(str(round(maxi,2)));
        fo.write("|");
        fo.write(str(round(stand_dev,2)));
        fo.write("|");
        fo.write("\n");

        # Close opend file
        fo.close()

    newFile = open("reports/"+fileName, 'a')
    newFile.write("Feature");
    newFile.write("|");
    newFile.write("Count");
    newFile.write("|");
    newFile.write("Miss%");
    newFile.write("|");
    newFile.write("Card");
    newFile.write("|");
    newFile.write("Mode");
    newFile.write("|");
    newFile.write("Mode Count");
    newFile.write("|");
    newFile.write("Mode %");
    newFile.write("|");
    newFile.write("2nd Mode");
    newFile.write("|");
    newFile.write("2nd Mode Count");
    newFile.write("|");
    newFile.write("2nd Mode %");
    newFile.write("|");
    newFile.write("\n");
    newFile.close()

    categorical(0)
    categorical(2)
    categorical(3)
    categorical(4)
    categorical(5)
    categorical(6)
    categorical(7)
    categorical(8)
    categorical(14)
    categorical(15)
    categorical(16)
    categorical(17)

    newFile = open("reports/"+fileName, 'a')
    newFile.write("\nFeature");
    newFile.write("|");
    newFile.write("Count");
    newFile.write("|");
    newFile.write("Miss%");
    newFile.write("|");
    newFile.write("Card");
    newFile.write("|");
    newFile.write("Min");
    newFile.write("|");
    newFile.write("1st Quart");
    newFile.write("|");
    newFile.write("Mean");
    newFile.write("|");
    newFile.write("Median");
    newFile.write("|");
    newFile.write("3rd Quart");
    newFile.write("|");
    newFile.write("Max");
    newFile.write("|");
    newFile.write("Std Dev");
    newFile.write("|");
    newFile.write("\n");
    newFile.close()

    continuous(1)
    continuous(9)
    continuous(10)
    continuous(11)
    continuous(12)
    continuous(13)
    continuous(18)
    continuous(19)
    continuous(20)
    continuous(21)
    continuous(22)
    continuous(23)
    continuous(24)
    continuous(25)


genResults()