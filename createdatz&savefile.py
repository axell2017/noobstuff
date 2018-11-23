from random import shuffle

newlist = []

def datacreate():
    stringz = range(0,999)
      
    for x in stringz:
        if x % 2 == 0:
            pass
        else:
            newlist.append(x)
            shuffle(newlist)

def savewrite():
    fyle = open("dataset.txt", "w" )
    fyle.write(str(newlist))
    fyle.close
    


datacreate()
savewrite()
