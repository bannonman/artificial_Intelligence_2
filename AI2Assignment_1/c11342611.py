#"Corey Bannon"
#"C11342611"
#"DT228 / 4"
#"14 - 02 - 2015"
#"corey.bannon@mydit.ie"
#"Assignment 1 AI2"
__author__ = "Corey Bannon"
__studentID__ = "C11342611"
__courseyear__ = "DT228 / 4"
__date__ = "14 - 02 - 2015"
__email__ = "corey.bannon@mydit.ie"
__status__ = "Assignment 1 AI2"

def main():
	#Importing the necessary modules 
    import math
    from statistics import mode, StatisticsError
    import sys

    # Creating lists to store the data during the file read.
    list1 = list()
    feat = list()
    
    #Creating the continuous and categorical files, this also overwrites existing one. 
    cat = open("data/c11342611CONT.csv", 'w')
    cat.close()
    con = open("data/c11342611CAT.csv", 'w')
    con.close()

    #Reads in the features names stores in the text file. 
    #Sotres them in a list called feat and replaces \n with "" to ensure clean data and formatting.
    with open("data/featureNames.txt") as f:
        for line in f:
            stri = line.replace("\n","");
            feat.append(stri)
    
    #Reads in the dataset inside of the data folders.
    #splits the data when it reads in ','. It then appends the data to the data list.
    with open("data/DataSet.txt") as f:
        for line in f:
            data = list()
            information = line.strip().split(',')
            for line in information:
                data.append(line)
            list1.append(data)

    ##categorical feature function, created for two benifits. It can be called to try all of the datasets.
   	## if it fails that the data must not be categorical.
    def categorical(i):
    	#List of all the needed variables. 
    	#Assign all of them to 1 to disgard the changes made to them in previous call.
        total = 0
        mean = 0
        count = 0
        count1 = 0
        notin = 0
        miss = 0
        card = 0
        modecount = 0
        secondmode = 0
        
        ##creating lists for cardinality, mode and the second mode.
        cardList = list()
        modeList = list()
        secmodeList = list()

        #getting the missing values and appending the list of data at i to the cardlist.
        #if the list consists of space ?  then it increments the cound and the count of missing values.
        for list2 in list1:
            if(list2[i]!=' ?'):
                cardList.append(list2[i])
                count = count + 1
                count1 = count - notin
            else:
                notin = notin + 1
                count = count + 1

        ##Assignment the correct values to the variable names and performing the equations to get the mode,card,missing values.
        ca = set(cardList)
        card = len(ca)
        miss = (notin / count)*100
        modes = mode(cardList)
        
        #appends the list2 execpt for the data that is assosiated with mode one. this helps get the second mode.    
        for list2 in list1:
            if(list2[i]!=modes):
                secmodeList.append(list2[i])

        #gets the first mode count
        modecount = cardList.count(modes)
        #gets the mode %
        modeper = (modecount / count1)*100

        #using statistics to get the mode of the remaining list.
        secondmode = mode(secmodeList)
        #getting the second mode count
        secmodecount = secmodeList.count(secondmode)
        #calculates the second mode %
        secmodeper = (secmodecount / count1)*100

        #creating string to improve write time to the files
        cat_str = "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s \n" % (feat[i], str(count1),str(round(miss,2)),
        	str(round(card,2)),str(modes),str(round(modecount,2)),str(round(modeper,2)),
        	str(secondmode),str(round(secmodecount,2)),str(round(secmodeper,2)))

        # Open a file
        cat = open("data/c11342611CAT.csv", "a")
        #write the string to the file. only uses one write to the file, which does it quicker.
        cat.write(cat_str)
        # Close opend file
        cat.close()
    #end of the categorical function.


    ##continuous feature function, created for two benifits. It can be called to try all of the datasets.
   	## if it fails that the data must not be continuous.
   	##this function is called first to check to see if the data is a float. if it fails then it is not. 
    def continuous(i):
    	#List of all the needed variables. 
    	#Assign all of them to 1 to disgard the changes made to them in previous call.
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

        ##creating lists for cardinality and median.
        medList = list()
        cardList = list()

        #for loop that gets off the data that is in list1 to list2.
        #It then looks for missing values and increments the notin variable by 1.
        #for loop is also used to assign the correct values to the cardlist and medlist. it also counts the total line in the data.
        #Also gets the square root value.
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

        ## applying the maths to assign the right values to the variales that have to be written to the file con.
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

        #creating string to improve write time to the files
        con_str = "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s \n" % (feat[i], str(count1),str(round(miss,2)),
        	str(round(card,2)),str(round(mini,2)), str(round(onestquart,2)),str(round(mean,2)),
        	str(round(median,2)),str(round(threerdquart,2)),str(round(maxi,2)),str(round(stand_dev,2)))

        # Open a file
        con = open("data/c11342611CONT.csv", "a")
        #Writing the continous feaure string to the file.
        con.write(con_str)
        # Close opend file
        con.close()
    #end of con function.


    #Writing the files header to the files before the data is writen to them.
    con = open("data/c11342611CONT.csv", 'a')
    con.write("FEATURENAME, COUNT, % MISS, CARD, MIN, 1st QUART, MEAN, MEDIAN, 3rd QUART, MAX, STD DEV\n")
    con.close()
 
    #Writing the files header to the files before the data is writen to them.
    cat = open("data/c11342611CAT.csv", 'a')
    cat.write("FEATURENAME, COUNT, % MISS, CARD, MODE, MODECOUNT, MODE%, 2nd MODE, 2nd MODE COUNT, 2nd MODE % \n")
    cat.close()
    
    ##creating the check variable for the while loop. 
    check = 0;
    
    ##The following while loop and try except functions tests each data set read in to check if it is either continous or categorical.
    ##Continuous is called first to check to see if the data is a float or not.
    ##If it throws an error then the data is not writen to file and is check to see if it might be categorical.
    ##If the data is not categorical and it throws either of the two excepts then if fails and does not write to a files.
    ##Check is then incremented to check the next data set as long as it is within the feature count.
    ##The while loop exits when the check count is == to the feat list length.
    #Staticts error had to by imported with the Statistics module. 
    while check != len(feat):
        try:
            try:
                continuous(check)
                check = check + 1 
            except ValueError:
                try:
                    categorical(check)
                    check = check + 1
                except StatisticsError:
                    check = check + 1
        except IndexError:
            check = check + 1

##calls the main method when the python script is called. 
if __name__ == '__main__':
    main()
