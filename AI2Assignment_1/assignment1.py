##Corey Bannon
##C11342611
##DT228 / 4
##Github : bannonman

def main():
    import math
    from statistics import mode, StatisticsError
    import sys

    list1 = list()
    feat = list()
    
    fo = open("data/c11342611CONT.csv", 'w')
    fo.close()
    newFile = open("data/c11342611CAT.csv", 'w')
    newFile.close()

    with open("data/featureNames.txt") as f:
        for line in f:
            stri = line.replace("\n","");
            feat.append(stri)
            
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
        secondmode = 0
        
        cardList = list()
        modeList = list()
        secmodeList = list()

        for list2 in list1:
            if(list2[i]!=' ?'):
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
        fo = open("data/c11342611CAT.csv", "a")
        fo.write(feat[i])
        fo.write(",")
        fo.write(str(count1))
        fo.write(",")
        fo.write(str(round(miss,2)))
        fo.write(",")
        fo.write(str(round(card,2)))
        fo.write(",")
        fo.write(str(modes))
        fo.write(",")
        fo.write(str(round(modecount,2)))
        fo.write(",")
        fo.write(str(round(modeper,2)))
        fo.write(",")
        fo.write(str(secondmode))
        fo.write(",")
        fo.write(str(round(secmodecount,2)))
        fo.write(",")
        fo.write(str(round(secmodeper,2)))
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
            if(list2[i]!=' ?'):
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
        fo = open("data/c11342611CONT.csv", "a")
        fo.write(feat[i]);
        fo.write(",");
        fo.write(str(count1));
        fo.write(",");
        fo.write(str(round(miss,2)));
        fo.write(",");
        fo.write(str(round(card,2)));
        fo.write(",");
        fo.write(str(round(mini,2)));
        fo.write(",");
        fo.write(str(round(onestquart,2)));
        fo.write(",");
        fo.write(str(round(mean,2)));
        fo.write(",");
        fo.write(str(round(median,2)));
        fo.write(",");
        fo.write(str(round(threerdquart,2)));
        fo.write(",");
        fo.write(str(round(maxi,2)));
        fo.write(",");
        fo.write(str(round(stand_dev,2)));
        fo.write("\n")
        # Close opend file
        fo.close()

    newFile = open("data/c11342611CONT.csv", 'a')
    newFile.write("FEATURENAME, COUNT, % MISS, CARD, MIN, 1st QUART, MEAN, MEDIAN, 3rd QUART, MAX, STD DEV\n")
    newFile.close()
    
    fo = open("data/c11342611CAT.csv", 'a')
    fo.write("FEATURENAME, COUNT, % MISS, CARD, MODE, MODECOUNT, MODE%, 2nd MODE, 2nd MODE COUNT, 2nd MODE % \n")
    fo.close()
    i = 0;

    
    while i != len(feat):
        try:
            try:
                continuous(i)
                i = i + 1 
            except ValueError:
                try:
                    categorical(i)
                    i = i + 1
                except StatisticsError:
                    i = i + 1
        except IndexError:
            i = i + 1

if __name__ == '__main__':
    main()
