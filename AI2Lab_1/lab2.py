__author__ = 'coreyandrewbannon'


def main():
    import math
    from statistics import mode
    import sys

    list1 = list()
    dict = list()

    #dict = {0: 'symboling', 1:'normalized-losses',2:'make',3:'fuel-type',4:'aspiration',5:'num-of-doors',6:'body-style',
     #       7:'drive-wheels',8:'engine-location',9:'wheel-base',10:'length',11:'width',12:'height',13:'curb-weight',
      #      14:'engine-type',15:'num-of-cylinders',16:'engine-size',17:'fuel-system',18:'bore',19:'stroke',
       #     20:'compression-ratio',21:'horsepower',22:'peak-rpm',23:'city-mpg',24:'highway-mpg',25:'price'};

    fileName = input('Enter name of text file: ')+'.txt'
    newFile = open("reports/"+fileName, 'w')
    newFile.close()


    with open("data/featureNames.txt") as g:
            for line in g:
                feat = line.replace('\n','')
                dict.append(feat)

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
        secondmode =0
        
        cardList = list()
        modeList = list()
        secmodeList = list()

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
        fo.write(dict[i].ljust(16))
        fo.write("\t")
        fo.write(str(count1).rjust(5))
        fo.write("\t")
        fo.write(str(round(miss,2)).rjust(5))
        fo.write("\t")
        fo.write(str(round(card,2)).rjust(5))
        fo.write("\t")
        fo.write(str(modes).rjust(5))
        fo.write("\t")
        fo.write(str(round(modecount,2)).rjust(10))
        fo.write("\t")
        fo.write(str(round(modeper,2)).rjust(8))
        fo.write("\t")
        fo.write(str(secondmode).rjust(8))
        fo.write("\t")
        fo.write(str(round(secmodecount,2)).rjust(12))
        fo.write("\t")
        fo.write(str(round(secmodeper,2)).rjust(10))
        fo.write("\t")
        fo.write("\n")

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

        sortedList = list()
        medList = list()
        cardList = list()
        
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
        fo.write(dict[i].ljust(16));
        fo.write("\t");
        fo.write(str(count1).rjust(5));
        fo.write("\t");
        fo.write(str(round(miss,2)).rjust(5));
        fo.write("\t");
        fo.write(str(round(card,2)).rjust(5));
        fo.write("\t");
        fo.write(str(round(mini,2)).rjust(5));
        fo.write("\t");
        fo.write(str(round(onestquart,2)).rjust(10));
        fo.write("\t");
        fo.write(str(round(mean,2)).rjust(8));
        fo.write("\t");
        fo.write(str(round(median,2)).rjust(8));
        fo.write("\t");
        fo.write(str(round(threerdquart,2)).rjust(10));
        fo.write("\t");
        fo.write(str(round(maxi,2)).rjust(10));
        fo.write("\t");
        fo.write(str(round(stand_dev,2)).rjust(10));
        fo.write("\t");
        fo.write("\n")

        # Close opend file
        fo.close()

    newFile = open("reports/"+fileName, 'a')
    newFile.write("Categorical Table:")
    newFile.write("\n")
    newFile.write("Feature".ljust(16));
    newFile.write("\t");
    newFile.write("Count".rjust(5));
    newFile.write("\t");
    newFile.write("Miss%".rjust(5));
    newFile.write("\t");
    newFile.write("Card".rjust(5));
    newFile.write("\t");
    newFile.write("Mode".rjust(5));
    newFile.write("\t");
    newFile.write("ModeCount".rjust(10));
    newFile.write("\t");
    newFile.write("Mode%".rjust(8));
    newFile.write("\t");
    newFile.write("2ndMode".rjust(8));
    newFile.write("\t");
    newFile.write("2ndModeCount".rjust(12));
    newFile.write("\t");
    newFile.write("2ndMode%".rjust(10));
    newFile.write("\t");
    newFile.write("\n");
    newFile.write("-------------------------------------------------------------------------------------------------------------------")
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
    categorical(17)

    newFile = open("reports/"+fileName, 'a')
    newFile.write("\nContinuous Table:")
    newFile.write("\n")
    newFile.write("---------------------------------------------------------------------------------------------------------------------------\n")
    newFile.write("Feature".ljust(16));
    newFile.write("\t");
    newFile.write("Count".rjust(5));
    newFile.write("\t");
    newFile.write("Miss%".rjust(5));
    newFile.write("\t");
    newFile.write("Card".rjust(5));
    newFile.write("\t");
    newFile.write("Min".rjust(5));
    newFile.write("\t");
    newFile.write("1stQuart".rjust(10));
    newFile.write("\t");
    newFile.write("Mean".rjust(8));
    newFile.write("\t");
    newFile.write("Median".rjust(8));
    newFile.write("\t");
    newFile.write("3rdQuart".rjust(10));
    newFile.write("\t");
    newFile.write("Max".rjust(10));
    newFile.write("\t");
    newFile.write("StdDev".rjust(10));
    newFile.write("\t");
    newFile.write("\n");
    newFile.write("---------------------------------------------------------------------------------------------------------------------------")
    newFile.write("\n");
    newFile.close()

    continuous(1)
    continuous(9)
    continuous(10)
    continuous(11)
    continuous(12)
    continuous(13)
    continuous(16)
    continuous(18)
    continuous(19)
    continuous(20)
    continuous(21)
    continuous(22)
    continuous(23)
    continuous(24)
    continuous(25)

if __name__ == '__main__':
    main()
