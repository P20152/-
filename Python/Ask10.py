def dictionary(dic):
    a = str(dic)
    counter = 0 #Μετράω όλα τα σύμβολα {,} και [,] και τα αθροίζω σε ένα counter
    counter_max = 0 #Με αυτό μετράω το βάθος του λεξικού
    for i in a:
        if i == "{" or i == "[":
            counter += 1
            if counter_max < counter:
                counter_max = counter
        elif i == "}" or i == "]":
            counter -= 1
    return counter_max
import json #Κάνω προσθήκη της json που θα με βοηθήσει να μετρατρέψω ένα αντικείμενο της python σε ένα json string 
with open("dic.txt") as f: 
    data = f.read()
js = json.dumps(data)
print("Το μεγαλύτερο βάθος του λεξικού είναι " + str(dictionary(js)))
f.close()