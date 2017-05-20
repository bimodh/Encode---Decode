#Send a list between two systems, by encoding and decoding
#Add the length of the word as the first and then append the word, concatinate the words to form the string, then send the string
#Recievers side, read the size of the string, then read the word.
#Word can contain numbers, special characters etc.
#So, add the length of the word, add a space, then add the word
#input = ['aa,.', 'iewrew546p', '6g70']
#Formated string will be "4 aa,.10 iewrew546p4 6g70"

def encode():
    inpList = ['aa,.', 'iewrew546p', '6g70']#'aa,.', ,
    totalString = ""   
    for i in range(0,len(inpList)):
        wordlen = len(inpList[i])
        totalString = totalString+str(wordlen)+" "+inpList[i]  
    return(totalString)

def decode(totalString):
    outArr = []
    while len(totalString) > 0 :
        wordlen = int(totalString[0:totalString.find(" ")])
        totalString = totalString[totalString.find(" ")+1:]
        outArr.append(totalString[0:wordlen])
        totalString = totalString[wordlen:]
    return outArr

print encode()
print decode(encode())
