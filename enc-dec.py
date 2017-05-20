#Send a list between two systems, by encoding and decoding

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
