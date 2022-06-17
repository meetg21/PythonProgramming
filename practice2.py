import re
 
vowels = ["a","e","i","o","u"]
l= eval(input("l="))
def score_words(l1):
    global vowels
    d = 0
    for i in l1:
        c =0 
        for j in i:
           if j in vowels:
                  c+=1
        if c%2 == 0:
            d +=2
        else:
            d +=1
    print(d)       
score_words(l)
