from random import shuffle

listings = open("dataset.txt")
acendlist = []



def readata():
    values = open("dataset.txt")

    for x in values:
         acendlist.append(x)
            
    
def savewrite():
    fyle = open("order.txt", "w" )
    fyle.write(str(acendlist))
    fyle.close


readata()
savewrite()


print(acendlist)



#sorting algorythm. sort dataset by ascending and decending order
    #multi sorting algos choose which one 1) a-z  2) z-a
