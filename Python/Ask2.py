n = int(input("Ορο ακολουθίας Fibonacci "))
b = [0,1,2]
if (n>2) : #Εδώ βρίσκω τον ν-οστο όρο της ακολουθίας Fibonacci
    for i in range (3,n):
        z=b[i-1]+b[i-2]
        b.append(int(z))
from random import randint #Κάνω προσθήκη της βοηθητικής συνάρτησης για να βρώ τις 20 τυχαίες επιλογές του a
c = True
for i in range(20): #Εδώ βλέπω άμα ο αριθμός είναι πρώτος
    a = randint(0, int(b[n-1]))
    if ((a**int(b[n-1]))%int(b[n-1])!=a%int(b[n-1])) : 
	    c=False
if c == True :
    print("Ο " + str(n) + "ος είναι ο " + str(b[n-1]) + " και είναι πρώτος")
elif c== False :
    print("Ο " + str(n) + "ος είναι ο " + str(b[n-1]) + " και δεν είναι πρώτος")