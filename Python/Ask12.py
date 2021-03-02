def asciii(asc):
    asc1=[line.rstrip() for line in str(asc)]
    result=[]
    length = len(asc1)
    if (length == 1): #Για μια γραμμη 
        a = asc1[0]
        for i in range (len(a)):
            result.append(a[i])
    elif (length != 1): #Για πολλαπλές γραμμές
        a = asc[0:length]
        for i in range (len(a)):
            for j in range (len(a[i])):
                result.append(a[i][j]) 
    for i in range(len(result)):
        result[i] = chr(128 - ord(result[i])) #Εδω βρίσκω το κατοπτρικό
    result = result[::-1] #Αντιστρέφω όλα τα γράμματα
    result="".join(result) #Eνώνω όλους τους όρους χωρίς κενά
    return result
with open("asc.txt") as f: 
    data = f.read()
print (asciii(data))
f.close()