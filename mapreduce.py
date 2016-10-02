import string # to import some of string functionalities such as pucntuation signs etc.


def reformatText(text): # delete irregular exepressions
    # delete punctuation
    for p in string.punctuation: # going through all signs of punctuation
        text= text.replace(p,"")
    
    # delete return to the line (which is done by readline() method)
    text= text.replace("\n","")

    # transform words to lower case (for more practical results)
    text = text.lower();

    return text

def inputreadfunction(textname):
    lineslist = [] # we initialize an empty list which will contain each line
    testtext = open(textname, 'r') # only readable for the purpose of our problem
   
    a = testtext.readline() # read the first line

    while a: # as long as we find a new line
        a = reformatText(a) # we reformat the line
        lineslist.append(a) # add it to the list
        try:
            a = testtext.readline() # read the next line
        except :
            pass
        


    return lineslist

def mapfunction ( text ):
    wordspairslist = []  # we initialize an empty list which will 
                    # contain a list of key,value pairs (words, 1)
    
    wordslist = text.split(' ') # we separate every word into an array cell

    for word in wordslist:
        if len(word)>0 :  # to avoid spaces at the end of a line
            wordspairslist.append((word, 1)) #add a couple to the list

    return wordspairslist

def shufflefunction(wordspairlist):
    coupleslist = [] # empty list that will contain every word without their multiplicity
    
    for wordsperline in wordspairlist:                  # concatenate all the lists in the list
        coupleslist = coupleslist + wordsperline        # to one long list
    
    fullcoupleslist = [] # empty list that will contain every word with their multiplicity

    for index in range(len(coupleslist)):               # going through the list adding couples
        addcouple(fullcoupleslist, coupleslist[index])
    
    return fullcoupleslist

def addcouple(finalcoupleslist, couple): # function that add a couple if it does'nt already exists
                                         # else it add an occurence in the list

    for index in range(len(finalcoupleslist)):
        couples = finalcoupleslist[index]
        if couples[0] == couple[0]: # if already exists
            finalcoupleslist[index] = (finalcoupleslist[index][0], finalcoupleslist[index][1] + [1])
            return
    
    #if it doesn't already exist add a new one
    finalcoupleslist.append((couple[0], [1]))
    return

def reducefunction(coupleslist):
    outputlist = []

    for couple in coupleslist:
        outputlist = outputlist + [(couple[0], len(couple[1]))] # we can also sum up all the values in the list
    
    return outputlist

def outputprint(outputlist): # give a more beautiful output
    for word in outputlist:
        if word[1]>0:
            print('the word \'{}\' appears {} times.'.format(word[0], word[1]))
        else:
            print('the word \'{}\' appears {} time.'.format(word[0], word[1]))
                
    
# main

textbylines  = inputreadfunction('questions.txt')

textbywords = []

for line in textbylines:
    linebywords = mapfunction(line)
    textbywords.append(linebywords)

wordswithoutmultiplicity = shufflefunction(textbywords)

wordswithmultiplicity = reducefunction(wordswithoutmultiplicity)

outputprint(wordswithmultiplicity)